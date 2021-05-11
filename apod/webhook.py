from aiohttp import ClientSession
from discord import Webhook, AsyncWebhookAdapter, Embed


# TODO: Add 'help' function, decorate with logging, add unit tests
class ApodHook:
    def __init__(self, config, api_key, hook_url, logger):
        self.api_key = api_key
        self.hook_url = hook_url
        self.logger = logger

        self.logger.info('ApodWebhook initialized')
        self.logger.debug(f'''
        ApodWebhook initialized;
        api_key: {self.api_key},
        webhook_url: {self.hook_url}
        ''')

    def _get_embed(self, data):
        embed = Embed(description=data['explanation'], title=data['title'], url=data['url'])

        self.logger.info('Embed created')
        self.logger.debug(f'Embed: {embed}')

        if data['mediaType'] == 'video':
            # FIXME: not able to set attribute
            # embed.__setattr__('video', data['url'])
            embed.set_image(url=data['url'])

            self.logger.info('Embed image set')
            self.logger.debug(f"Embed image url: {data['url']}")
        else:
            embed.set_image(url=data['url'])

            self.logger.info('Embed image set')
            self.logger.debug(f"Embed image url: {data['url']}")

            embed.add_field(name='HD Image Link', value=data['hdurl'])

            self.logger.info('Embed HD image field added')
            self.logger.debug(f"Embed HD image url: {data['hdurl']}")

        if data['copyright']:
            embed.set_author(name=data['copyright'])

            self.logger.info('Embed copyright set')
            self.logger.debug(f"Embed copyright: {data['copyright']}")

        self.logger.debug(f'Embed: {embed.to_dict()}')

        return embed

    def _get_embeds(self, data):
        self.logger.info('Generating multiple embeds')
        if len(data) > 10:
            return [self._get_embed(val) for val in data[:10]]
        else:
            # self.logger.info('Generating single embed')
            return [self._get_embed(val) for val in data]

    async def fire(self, data, multi):
        async with ClientSession() as session:
            webhook = Webhook.from_url(self.hook_url, adapter=AsyncWebhookAdapter(session))
            self.logger.info('Webhook created')
            self.logger.debug(f'Webhook: {webhook}')

            if multi:
                self.logger.info('Sending multiple results')
                await webhook.send(username='NASA Bot', embeds=self._get_embeds(data))
            else:
                self.logger.info('Sending single result')
                await webhook.send(username='NASA Bot', embed=self._get_embed(data))
