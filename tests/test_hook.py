import unittest.mock

from apod.apod_hook import ApodHook, Webhook, get_hook
from tests import ENV_PATH, APOD_DATA_ARG, APODS_DATA_ARG
from tests import OBJ_NO_MATCH
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


class TestHook(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._hook = get_hook()

    @unittest.skip('not implemented')
    def test_get_webhook(self):
        self.assertTrue(isinstance(self._hook, ApodHook), OBJ_NO_MATCH)


class TestHookEmbeds(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._hook = get_hook()

    def test_get_embed(self):
        test_val = self._hook._get_embed(APOD_DATA_ARG)

        # Check embed
        self.assertIsNotNone(test_val)

        test_val = test_val.to_dict()

        # Check embed data
        self.assertIn('image', test_val)
        self.assertIn('fields', test_val)
        self.assertIn('description', test_val)
        self.assertIn('url', test_val)
        self.assertIn('title', test_val)

    def test_get_embeds(self):
        test_val = self._hook._get_embeds(APODS_DATA_ARG)

        # Check embed
        self.assertIsNotNone(test_val)

        # Check embed data
        for embed in test_val:
            embed = embed.to_dict()
            self.assertIn('image', embed)
            self.assertIn('fields', embed)
            self.assertIn('description', embed)
            self.assertIn('url', embed)
            self.assertIn('title', embed)


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
