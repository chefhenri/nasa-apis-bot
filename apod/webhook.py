from aiohttp import ClientSession
from discord import Webhook, AsyncWebhookAdapter, Embed


class ApodWebhook:
    def __init__(self, gql_endpoint, api_key, channel_id, channel_url):
        self.gql_endpoint = gql_endpoint
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_url = channel_url

    @classmethod
    def _get_embed(cls, data):
        embed = Embed(description=data['explanation'], title=data['title'], url=data['url'])
        if data['mediaType'] == 'video':
            # FIXME: not able to set attribute
            # embed.__setattr__('video', data['url'])
            embed.set_image(url=data['url'])
            pass
        else:
            embed.set_image(url=data['url'])
            embed.add_field(name='HD Image Link', value=data['hdurl'])

        if data['copyright']:
            embed.set_author(name=data['copyright'])
        return embed

    @classmethod
    def _get_embeds(cls, data):
        if len(data) > 10:
            return [cls._get_embed(val) for val in data[:10]]
        else:
            return [cls._get_embed(val) for val in data]

    async def fire(self, data, multi):
        async with ClientSession() as session:
            webhook = Webhook.from_url(self.channel_url, adapter=AsyncWebhookAdapter(session))

            if multi:
                await webhook.send(username='NASA Bot', embeds=self._get_embeds(data))
            else:
                await webhook.send(username='NASA Bot', embed=self._get_embed(data))
