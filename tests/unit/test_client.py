import os
import unittest

from apod.apod_client import ApodClient, get_apod_client, convert_date
from utils.config import init_root_cfg

ENV_PATH = os.path.join(os.path.dirname(__file__), '../../.env.stage')

DATE_ARG_SLASH_FMT_ONE = '06/28/1999'
DATE_ARG_SLASH_FMT_TWO = '28/06/1999'
DATE_ARG_DOT_FMT_ONE = '06.28.1999'
DATE_ARG_DOT_FMT_TWO = '28.06.1999'
DATE_ARG_DASH_FMT_ONE = '06-28-1999'
DATE_ARG_DASH_FMT_TWO = '28-06-1999'

ISO_DATE_DASH_FMT = '1999-06-28'
BAD_DATE_FMT = '1999--06--28'

OBJ_NO_MATCH = 'The two objects are not of the same instance.'
DATE_NO_MATCH = 'The tested date does not match the expected date.'


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._gql_client = get_apod_client()

    # @unittest.skip('not implemented')
    def test_get_apod_client(self):
        self.assertTrue(isinstance(self._gql_client, ApodClient), OBJ_NO_MATCH)

    # @unittest.skip('not implemented')
    def test_convert_date_slash_sep(self):
        test_date_one = convert_date(DATE_ARG_SLASH_FMT_ONE)
        test_date_two = convert_date(DATE_ARG_SLASH_FMT_TWO)

        self.assertEqual(test_date_one, ISO_DATE_DASH_FMT)
        self.assertEqual(test_date_two, ISO_DATE_DASH_FMT)

    # @unittest.skip('not implemented')
    def test_convert_date_dot_sep(self):
        test_date_one = convert_date(DATE_ARG_DOT_FMT_ONE)
        test_date_two = convert_date(DATE_ARG_DOT_FMT_TWO)

        self.assertEqual(test_date_one, ISO_DATE_DASH_FMT)
        self.assertEqual(test_date_two, ISO_DATE_DASH_FMT)

    # @unittest.skip('not implemented')
    def test_convert_date_dash_sep(self):
        test_date_one = convert_date(DATE_ARG_DASH_FMT_ONE)
        test_date_two = convert_date(DATE_ARG_DASH_FMT_TWO)

        self.assertEqual(test_date_one, ISO_DATE_DASH_FMT)
        self.assertEqual(test_date_two, ISO_DATE_DASH_FMT)

    def test_convert_date_bad_sep(self):
        with self.assertRaises(ValueError):
            convert_date(BAD_DATE_FMT)
