from aiohttp import ClientSession
from discord import Webhook, AsyncWebhookAdapter, Embed

from utils.config import get_hook_cfg
from utils.logging import get_logger, wrap, entering, exiting


# TODO: Add 'help' function, docstrings
class ApodHook:
    def __init__(self):
        self._config = get_hook_cfg()
        # self._logger = get_logger()

        # TODO: Extract to log wrapper
        # self._logger.debug(f'''
        # ApodWebhook initialized;
        # webhook_url: {self._config['url']}
        # ''')
        # self._logger.info('ApodWebhook initialized')

    # @wrap(entering, exiting)
    def _get_embed(self, data):
        embed = Embed(description=data['explanation'], title=data['title'], url=data['url'])

        # self._logger.info('Embed created')
        # self._logger.debug(f'Embed: {embed}')

        if data['mediaType'] == 'video':
            # FIXME: not able to set attribute
            # embed.__setattr__('video', data['url'])
            embed.set_image(url=data['url'])

            # self._logger.info('Embed image set')
            # self._logger.debug(f"Embed image url: {data['url']}")
        else:
            embed.set_image(url=data['url'])

            # self._logger.info('Embed image set')
            # self._logger.debug(f"Embed image url: {data['url']}")

            embed.add_field(name='HD Image Link', value=data['hdurl'])

            # self._logger.info('Embed HD image field added')
            # self._logger.debug(f"Embed HD image url: {data['hdurl']}")

        if data['copyright']:
            embed.set_author(name=data['copyright'])

            # self._logger.info('Embed copyright set')
            # self._logger.debug(f"Embed copyright: {data['copyright']}")

        # self._logger.debug(f'Embed: {embed.to_dict()}')

        return embed

    # @wrap(entering, exiting)
    def _get_embeds(self, data):
        # self._logger.info('Generating multiple embeds')
        if len(data) > 10:
            return [self._get_embed(val) for val in data[:10]]
        else:
            # self.logger.info('Generating single embed')
            return [self._get_embed(val) for val in data]

    # @wrap(entering, exiting)
    async def fire(self, data, multi):
        async with ClientSession() as session:
            webhook = Webhook.from_url(self._config['url'], adapter=AsyncWebhookAdapter(session))
            # self._logger.info('Webhook created')
            # self._logger.debug(f'Webhook: {webhook}')

            if multi:
                # self._logger.info('Sending multiple results')
                await webhook.send(username='NASA Bot', embeds=self._get_embeds(data))
            else:
                # self._logger.info('Sending single result')
                await webhook.send(username='NASA Bot', embed=self._get_embed(data))
