import unittest.mock

from apod.apod_hook import Webhook, get_hook
from tests import ENV_PATH, APODS_DATA_ARG
from utils.config import init_root_cfg

BOT_USERNAME = 'NASA Bot'
TEST_EMBED_DATA = {
    'copyright': '',
    'explanation': '',
    'hdurl': '',
    'mediaType': '',
    'title': '',
    'url': ''
}


class TestHookFire(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._hook = get_hook()

    @unittest.skip('needs refactor to mock webhook')
    @unittest.mock.patch('apod.apod_hook.ApodHook')
    @unittest.mock.patch.object(Webhook, 'send', autospec=True)
    async def test_fire_single_embed(self, mock_send_obj, mock_hook):
        # Setup mock
        mock_hook._get_embed.return_value = {}

        # Make call
        await self._hook.fire(data=TEST_EMBED_DATA, multi=False)

        # Verify
        mock_send_obj.assert_called_with(username=BOT_USERNAME, embeds={})

    @unittest.skip('needs refactor to mock webhook')
    async def test_fire_multiple_embeds(self):
        await self._hook.fire(data=APODS_DATA_ARG, multi=True)
