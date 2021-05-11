import unittest

from apod.client import ApodClient
from utils.config import get_cfg
from utils.logger import BotLogger

DATE_ARG = '1999-06-28'
START_DATE_ARG = DATE_ARG
END_DATE_ARG = '1999-06-29'
COUNT_ARG = 2

APOD_BY_DATE_VAL = {
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
APODS_BY_DATE_VAL = [
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

APOD_BY_DATE_QUERY = 'apodByDate'
APODS_BY_DATE_QUERY = 'apodsByDate'
APODS_BY_COUNT_QUERY = 'randomApods'

RESULT_NO_MATCH = 'The expected result does not match the tested result.'


class TestClientQueries(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.maxDiff = None

    def setUp(self) -> None:
        self._config = get_cfg('../../.env')
        self._logger = BotLogger(log_lvl=self._config['TEST_LOG_LVL'], log_dir=self._config['TEST_LOG_DIR'])
        self._client = ApodClient(config=self._config, logger=self._logger)

    async def test_query_today(self):
        test_val = await self._client.query_today()

        # Check query result
        self.assertIn('today', test_val)

        # Check result data
        self.assertIn('copyright', test_val['today'])
        self.assertIn('explanation', test_val['today'])
        self.assertIn('hdurl', test_val['today'])
        self.assertIn('mediaType', test_val['today'])
        self.assertIn('title', test_val['today'])
        self.assertIn('url', test_val['today'])

    async def test_query_apod_by_date(self):
        test_val = await self._client.query_apod_by_date(DATE_ARG)
        exp_val = APOD_BY_DATE_VAL

        # Check query result
        self.assertIn(APOD_BY_DATE_QUERY, test_val)
        self.assertDictEqual(test_val[APOD_BY_DATE_QUERY], exp_val, RESULT_NO_MATCH)

    async def test_query_apods_by_date(self):
        test_val = await self._client.query_apods_by_date(START_DATE_ARG, END_DATE_ARG)
        exp_val = APODS_BY_DATE_VAL

        # Check query result
        self.assertIn(APODS_BY_DATE_QUERY, test_val)
        self.assertListEqual(test_val[APODS_BY_DATE_QUERY], exp_val, RESULT_NO_MATCH)

    async def test_query_random_apods(self):
        test_val = await self._client.query_random_apods(COUNT_ARG)

        # Check query result
        self.assertIn(APODS_BY_COUNT_QUERY, test_val)

        # Check result data
        for apod in test_val[APODS_BY_COUNT_QUERY]:
            self.assertIn('copyright', apod)
            self.assertIn('explanation', apod)
            self.assertIn('hdurl', apod)
            self.assertIn('mediaType', apod)
            self.assertIn('title', apod)
            self.assertIn('url', apod)
