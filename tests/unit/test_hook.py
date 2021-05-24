import unittest

from apod.apod_hook import ApodHook, get_hook
from utils.config import init_root_cfg
from tests import ENV_PATH, APOD_DATA_ARG, APODS_DATA_ARG
from tests.unit import OBJ_NO_MATCH


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
