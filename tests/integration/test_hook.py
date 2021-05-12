# FIXME: Fix imports
import unittest

from apod.webhook import ApodHook
from utils.config import get_cfg
from utils.logger import BotLogger

ENV_PATH = '/.env.prod'

SINGLE_EMBED_DATA_ARG = {
    "copyright": None,
    "explanation": "Are Martians trying to tell us something?  An indentation has been recently photographed on Mars "
                   "that resembles a heart, a common human symbol for love.  Because intelligent Martians have never "
                   "been known to exist, and because formations with similarities have been found that clearly result "
                   "from natural phenomena, the pit shown above is thought not to be a form of interplanetary "
                   "communication.  Many scientists believe instead that the right-most wall of the two-kilometer "
                   "wide heart-shaped pit was created by a naturally occurring graben, a surface drop caused by "
                   "expansion along a fault-line.  Perhaps love is easier to find here on Earth.",
    "hdurl": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs_big.gif",
    "mediaType": "image",
    "title": "From Mars with Love",
    "url": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs.jpg"
}

MULTI_EMBED_DATA_ARG = [
    {
        "copyright": None,
        "explanation": "Are Martians trying to tell us something?  An indentation has been recently "
                       "photographed on Mars that resembles a heart, a common human symbol for love.  Because "
                       "intelligent Martians have never been known to exist, and because formations with similarities "
                       "have been found that clearly result from natural phenomena, the pit shown above is thought not "
                       "to be a form of interplanetary communication.  Many scientists believe instead that the "
                       "right-most wall of the two-kilometer wide heart-shaped pit was created by a naturally "
                       "occurring graben, a surface drop caused by expansion along a fault-line.  Perhaps love is "
                       "easier to find here on Earth.",
        "hdurl": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs_big.gif",
        "mediaType": "image",
        "title": "From Mars with Love",
        "url": "https://apod.nasa.gov/apod/image/9906/marsheart_mgs.jpg"
    },
    {
        "copyright": None,
        "explanation": "A new mammoth telescope has begun to inspect the northern sky.  The 8-meter Gemini North "
                       "telescope, pictured above, was dedicated last week in Hawaii, with images documenting its "
                       "unprecedented abilities being released.  Within two years, sister telescope Gemini South will "
                       "begin similar observations of the southern sky from Chile.  The Gemini telescopes will collect "
                       "an enormous amount of visible and infrared light. In the infrared, a Gemini can resolve "
                       "objects that even appear blurred to the Hubble Space Telescope.  To achieve such high "
                       "resolution, the Gemini's use adaptive optics, a technique that continually flexes Gemini's "
                       "main mirrors to counteract the defocusing effects of Earth's turbulent atmosphere.  A "
                       "seven-nation collaboration is completing the Geminis under the direction of the US National "
                       "Science Foundation.",
        "hdurl": "https://apod.nasa.gov/apod/image/9906/gemini_pfa_big.jpg",
        "mediaType": "image",
        "title": "Gemini North Telescope Inaugurated",
        "url": "https://apod.nasa.gov/apod/image/9906/gemini_pfa.jpg"
    }
]


# FIXME: Fix constructors
class TestHookFire(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._config = get_cfg(ENV_PATH)
        cls._logger = BotLogger(log_lvl=cls._config['TEST_LOG_LVL'], log_dir=cls._config['TEST_LOG_DIR'])
        cls._hook = ApodHook(config=cls._config,
                             api_key=cls._config['APOD_API_KEY'],
                             hook_url=cls._config['TEST_HOOK_URL'],
                             logger=cls._logger)

    # @unittest.skip('not implemented')
    async def test_fire_single_embed(self):
        await self._hook.fire(data=SINGLE_EMBED_DATA_ARG, multi=False)

    # @unittest.skip('not implemented')
    async def test_fire_multiple_embeds(self):
        await self._hook.fire(data=MULTI_EMBED_DATA_ARG, multi=True)


# FIXME: Fix constructors
class TestHookEmbeds(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._config = get_cfg(ENV_PATH)
        cls._logger = BotLogger(log_lvl=cls._config['TEST_LOG_LVL'], log_dir=cls._config['TEST_LOG_DIR'])
        cls._hook = ApodHook(config=cls._config,
                             api_key=cls._config['APOD_API_KEY'],
                             hook_url=cls._config['TEST_HOOK_URL'],
                             logger=cls._logger)

    def test_get_embed(self):
        test_val = self._hook._get_embed(SINGLE_EMBED_DATA_ARG)

        # Check embed
        self.assertIsNotNone(test_val)

        test_val = test_val.to_dict()

        # Check embed data
        self.assertIn('image', test_val)
        self.assertIn('fields', test_val)
        self.assertIn('description', test_val)
        self.assertIn('url', test_val)
        self.assertIn('title', test_val)

    # @unittest.skip('not implemented')
    def test_get_embeds(self):
        test_val = self._hook._get_embeds(MULTI_EMBED_DATA_ARG)

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
