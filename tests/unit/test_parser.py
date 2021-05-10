import unittest

from datetime import date, datetime

from utils.parser import MsgParser

DATE_ARG = '06/28/1999'
DATE_VAL = datetime.strptime(DATE_ARG, '%m/%d/%Y').strftime('%Y-%m-%d')
COUNT_VAL = 10

APOD_ARGS = 'apod'
APOD_WITH_DATE_ARGS = f'apod -d {DATE_ARG}'
APOD_WITH_COUNT_ARGS = 'apod -c 10'

DATE_NO_MATCH = 'Expected date does not match the tested date.'
ARGS_NO_MATCH = 'Expected args do not match the tested args.'
VAL_NO_MATCH = 'Expected value does not match the tested value.'


# TODO: Add error handling test cases, implement stubs
class ParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._parser = MsgParser(prog='Test')

    def setUp(self) -> None:
        self._today = date.today().strftime('%m/%d/%Y')

    def test_parse_apod_with_no_date(self):
        test_args = self._parser.parse(APOD_ARGS.split())

        # Check values
        self.assertIsNone(test_args['count'])
        self.assertIsNone(test_args['date'])
        self.assertIsNotNone(test_args['end_date'])
        self.assertIsNotNone(test_args['func'])
        self.assertIsNone(test_args['start_date'])

    def test_parse_apod_with_date(self):
        test_args = self._parser.parse(APOD_WITH_DATE_ARGS.split())
        test_val = test_args['date']
        exp_val = DATE_VAL

        # Check values
        self.assertIsNone(test_args['count'])
        self.assertIsNotNone(test_args['end_date'])
        self.assertIsNotNone(test_args['func'])
        self.assertIsNone(test_args['start_date'])

        # Check date
        self.assertIsNotNone(test_val)
        self.assertEqual(test_val, exp_val, DATE_NO_MATCH)

    def test_parse_apod_with_count(self):
        test_args = self._parser.parse(APOD_WITH_COUNT_ARGS.split())
        test_val = test_args['count']
        exp_val = COUNT_VAL

        # Check values
        self.assertIsNone(test_args['date'])
        self.assertIsNotNone(test_args['end_date'])
        self.assertIsNotNone(test_args['func'])
        self.assertIsNone(test_args['start_date'])

        # Check count
        self.assertIsNotNone(test_args['count'])
        self.assertEqual(test_val, exp_val, VAL_NO_MATCH)

    @unittest.skip('not implemented')
    def test_parse_apod_with_start_date(self):
        pass

    @unittest.skip('not implemented')
    def test_parse_apod_with_end_date(self):
        pass

    def test_get_today(self):
        test_val = self._parser.get_today()
        exp_val = self._today

        self.assertEqual(test_val, exp_val, DATE_NO_MATCH)

    def test_convert_date_with_date(self):
        test_val = self._parser.convert_date(DATE_ARG)
        exp_val = DATE_VAL

        self.assertEqual(test_val, exp_val, DATE_NO_MATCH)

    def test_convert_date_with_int(self):
        test_val = self._parser.convert_date(42)
        exp_val = 42

        self.assertEqual(test_val, exp_val, VAL_NO_MATCH)

    def test_convert_date_with_func(self):
        test_val = type(self._parser.convert_date(lambda a: a))
        exp_val = type(lambda b: b)

        self.assertEqual(test_val, exp_val, VAL_NO_MATCH)
