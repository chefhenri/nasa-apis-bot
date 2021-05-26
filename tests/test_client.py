import unittest
from unittest.mock import AsyncMock

from apod.apod_client import ApodClient, get_apod_client, convert_date
from tests import DATE_ARG_SLASH_FMT_ONE, \
    DATE_ARG_SLASH_FMT_TWO, \
    DATE_ARG_DOT_FMT_ONE, \
    DATE_ARG_DOT_FMT_TWO, \
    DATE_ARG_DASH_FMT_ONE, \
    DATE_ARG_DASH_FMT_TWO, \
    ISO_DATE_DASH_FMT, \
    BAD_DATE_FMT, \
    OBJ_NO_MATCH
from tests import ENV_PATH
from utils.config import init_root_cfg


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._gql_client = get_apod_client()

    def test_get_apod_client(self):
        self.assertTrue(isinstance(self._gql_client, ApodClient), OBJ_NO_MATCH)

    @unittest.skip('not implemented')
    def test_get_schema(self):
        pass

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
        cls._client = get_apod_client()

    async def test_handle(self):
        # Init mocks
        self._client._get_query = AsyncMock(return_value=('test', {'test': None}))
        self._client._hook.fire = AsyncMock()

        # Make call
        await self._client.handle({})

        # Verify
        self._client._get_query.assert_called_once()
        self._client._hook.fire.assert_called_once()


# TODO: Refactor to mock GQL client
class TestClientQueries(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls.maxDiff = None
        cls._client = get_apod_client()

    @unittest.skip('not implemented')
    def test_build_query(self):
        pass

    @unittest.skip('not implemented')
    async def test_query_today(self):
        pass

    @unittest.skip('not implemented')
    async def test_query_apod_by_date(self):
        pass

    @unittest.skip('not implemented')
    async def test_query_apods_by_date(self):
        pass

    @unittest.skip('not implemented')
    async def test_query_random_apods(self):
        pass
