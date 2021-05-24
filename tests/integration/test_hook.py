import unittest

from apod.apod_hook import get_hook
from utils.config import init_root_cfg
from tests import ENV_PATH, APOD_DATA_ARG, APODS_DATA_ARG


class TestHookFire(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._hook = get_hook()

    @unittest.skip('needs refactor to mock webhook')
    async def test_fire_single_embed(self):
        await self._hook.fire(data=APOD_DATA_ARG, multi=False)

    @unittest.skip('needs refactor to mock webhook')
    async def test_fire_multiple_embeds(self):
        await self._hook.fire(data=APODS_DATA_ARG, multi=True)
