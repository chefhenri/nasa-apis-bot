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
            # TODO: Construct video embed
            embed.__setattr__('video', data['url'])
        else:
            embed.set_image(url=data['url'])
            embed.add_field(name='HD Image Link', value=data['hdurl'])

        if data['copyright']:
            embed.set_author(name=data['copyright'])
        return embed

    async def fire(self, data):
        async with ClientSession() as session:
            embed = self._get_embed(data)

            webhook = Webhook.from_url(self.channel_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(embed=embed)
