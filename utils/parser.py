import argparse
from datetime import date, datetime

from utils.config import get_root_cfg


# TODO: Add error handling
class MsgParser:
    def __init__(self):
        self._config = get_root_cfg()

        self._parser = argparse.ArgumentParser(prog=self._config['prog'])
        self._subparsers = self._parser.add_subparsers()
        self._apod_parser = self._subparsers.add_parser('apod')

        self._apod_param_group = self._apod_parser.add_mutually_exclusive_group()
        self._apod_param_group.add_argument('-c', '--count', type=int, dest='count')

        self._apod_date_group = self._apod_param_group.add_mutually_exclusive_group()
        self._apod_date_group.add_argument('-d', '--date', type=str, dest='date')

        self._apod_date_range_group = self._apod_date_group.add_argument_group()
        self._apod_date_range_group.add_argument('-s', '--start-date', type=str, dest='start_date')
        self._apod_date_range_group.add_argument('-e', '--end-date', nargs='?', const=self.get_today(),
                                                 default=self.get_today(), type=str, dest='end_date')

        self._apod_parser.set_defaults(func=self._parse_apod_args)

    def _parse_apod_args(self, args):
        return {attr: self.convert_date(val) for (attr, val) in args.__dict__.items()}

    def parse(self, args):
        args = self._parser.parse_args(args)
        return args.func(args)

    @classmethod
    def get_today(cls):
        return date.today().strftime('%m/%d/%Y')

    @classmethod
    def convert_date(cls, arg):
        if isinstance(arg, str):
            date_ = datetime.strptime(arg, '%m/%d/%Y')
            date_ = date_.strftime('%Y-%m-%d')
            return date_
        else:
            return arg
