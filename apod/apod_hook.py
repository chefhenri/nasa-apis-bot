import functools

from aiohttp import ClientSession
from discord import Webhook, AsyncWebhookAdapter, Embed

from utils.config import get_hook_cfg
from utils.logging import wrap, entering, exiting


@functools.lru_cache(maxsize=None)
def get_hook():
    """ Gets the webhook object and caches it """
    config = get_hook_cfg()
    return ApodHook(config=config)


# TODO: Add 'help' function, update unit tests
class ApodHook:
    def __init__(self, config):
        """ Initializes the webhook object """
        self._config = config

    @wrap(entering, exiting)
    def _get_webhook(self, session):
        return Webhook.from_url(self._config['url'], adapter=AsyncWebhookAdapter(session))

    @wrap(entering, exiting)
    def _get_embed(self, data):
        """ Creates and configures embed """
        embed = Embed(description=data['explanation'], title=data['title'], url=data['url'])

        if data['mediaType'] == 'video':
            # FIXME: not able to set attribute
            # embed.__setattr__('video', data['url'])
            embed.set_image(url=data['url'])

        else:
            embed.set_image(url=data['url'])

            embed.add_field(name='HD Image Link', value=data['hdurl'])

        if data['copyright']:
            embed.set_author(name=data['copyright'])

        return embed

    @wrap(entering, exiting)
    def _get_embeds(self, data):
        """ Handles constructing multiple embeds """
        if len(data) > 10:
            return [self._get_embed(val) for val in data[:10]]
        else:
            return [self._get_embed(val) for val in data]

    @wrap(entering, exiting)
    async def fire(self, data, multi):
        """ Gathers embeds and sends them to the channel """
        async with ClientSession() as session:
            webhook = self._get_webhook(session)

            if multi:
                await webhook.send(username='NASA Bot', embeds=self._get_embeds(data))
            else:
                await webhook.send(username='NASA Bot', embed=self._get_embed(data))
