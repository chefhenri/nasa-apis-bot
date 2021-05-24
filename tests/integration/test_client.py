import unittest

from apod.apod_client import get_apod_client
from utils.config import init_root_cfg
from tests import ENV_PATH, APOD_DATA_ARG, APODS_DATA_ARG
from tests.integration import ISO_DATE, \
    ISO_START_DATE, \
    ISO_END_DATE, \
    APOD_BY_DATE_QUERY, \
    APODS_BY_DATE_QUERY, \
    APODS_BY_COUNT_QUERY, \
    RESULT_NO_MATCH


class TestClientHandle(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        # TODO: Mock ApodClient components
        pass

    @unittest.skip('not implemented')
    async def test_handle(self):
        pass


class TestClientQueries(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls.maxDiff = None
        cls._client = get_apod_client()

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

    async def test_query_apod_by_date(self):
        test_val = await self._client._query_apod_by_date(ISO_DATE)
        exp_val = APOD_DATA_ARG

        # Check query result
        self.assertIn(APOD_BY_DATE_QUERY, test_val)
        self.assertDictEqual(test_val[APOD_BY_DATE_QUERY], exp_val, RESULT_NO_MATCH)

    async def test_query_apods_by_date(self):
        test_val = await self._client._query_apods_by_date(ISO_START_DATE, ISO_END_DATE)
        exp_val = APODS_DATA_ARG

        # Check query result
        self.assertIn(APODS_BY_DATE_QUERY, test_val)
        self.assertListEqual(test_val[APODS_BY_DATE_QUERY], exp_val, RESULT_NO_MATCH)

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
