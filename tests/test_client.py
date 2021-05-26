import unittest

from apod.apod_client import ApodClient, get_apod_client, convert_date
from tests import ENV_PATH, APOD_DATA_ARG, APODS_DATA_ARG
from tests import ISO_DATE, \
    ISO_START_DATE, \
    ISO_END_DATE, \
    APOD_BY_DATE_QUERY, \
    APODS_BY_DATE_QUERY, \
    APODS_BY_COUNT_QUERY, \
    RESULT_NO_MATCH
from tests import DATE_ARG_SLASH_FMT_ONE, \
    DATE_ARG_SLASH_FMT_TWO, \
    DATE_ARG_DOT_FMT_ONE, \
    DATE_ARG_DOT_FMT_TWO, \
    DATE_ARG_DASH_FMT_ONE, \
    DATE_ARG_DASH_FMT_TWO, \
    ISO_DATE_DASH_FMT, \
    BAD_DATE_FMT, \
    OBJ_NO_MATCH
from utils.config import init_root_cfg


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._gql_client = get_apod_client()

    def test_get_apod_client(self):
        self.assertTrue(isinstance(self._gql_client, ApodClient), OBJ_NO_MATCH)

    def test_convert_date_slash_sep(self):
        test_date_one = convert_date(DATE_ARG_SLASH_FMT_ONE)
        test_date_two = convert_date(DATE_ARG_SLASH_FMT_TWO)

        self.assertEqual(test_date_one, ISO_DATE_DASH_FMT)
        self.assertEqual(test_date_two, ISO_DATE_DASH_FMT)

    def test_convert_date_dot_sep(self):
        test_date_one = convert_date(DATE_ARG_DOT_FMT_ONE)
        test_date_two = convert_date(DATE_ARG_DOT_FMT_TWO)

        self.assertEqual(test_date_one, ISO_DATE_DASH_FMT)
        self.assertEqual(test_date_two, ISO_DATE_DASH_FMT)

    def test_convert_date_dash_sep(self):
        test_date_one = convert_date(DATE_ARG_DASH_FMT_ONE)
        test_date_two = convert_date(DATE_ARG_DASH_FMT_TWO)

        self.assertEqual(test_date_one, ISO_DATE_DASH_FMT)
        self.assertEqual(test_date_two, ISO_DATE_DASH_FMT)

    def test_convert_date_bad_sep(self):
        with self.assertRaises(ValueError):
            convert_date(BAD_DATE_FMT)


class TestClientHandle(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        # TODO: Mock ApodClient components
        pass

    @unittest.skip('not implemented')
    async def test_handle(self):
        pass


# TODO: Refactor to mock GQL client
class TestClientQueries(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls.maxDiff = None
        cls._client = get_apod_client()

    @unittest.skip('needs refactor to use mock')
    async def test_query_today(self):
        test_val = await self._client._query_today()

        # Check query result
        self.assertIn('today', test_val)

        # Check result data
        self.assertIn('copyright', test_val['today'])
        self.assertIn('explanation', test_val['today'])
        self.assertIn('hdurl', test_val['today'])
        self.assertIn('mediaType', test_val['today'])
        self.assertIn('title', test_val['today'])
        self.assertIn('url', test_val['today'])

    @unittest.skip('needs refactor to use mock')
    async def test_query_apod_by_date(self):
        test_val = await self._client._query_apod_by_date(ISO_DATE)
        exp_val = APOD_DATA_ARG

        # Check query result
        self.assertIn(APOD_BY_DATE_QUERY, test_val)
        self.assertDictEqual(test_val[APOD_BY_DATE_QUERY], exp_val, RESULT_NO_MATCH)

    @unittest.skip('needs refactor to use mock')
    async def test_query_apods_by_date(self):
        test_val = await self._client._query_apods_by_date(ISO_START_DATE, ISO_END_DATE)
        exp_val = APODS_DATA_ARG

        # Check query result
        self.assertIn(APODS_BY_DATE_QUERY, test_val)
        self.assertListEqual(test_val[APODS_BY_DATE_QUERY], exp_val, RESULT_NO_MATCH)

    @unittest.skip('needs refactor to use mock')
    async def test_query_random_apods(self):
        test_val = await self._client._query_random_apods(len(APODS_DATA_ARG))

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
