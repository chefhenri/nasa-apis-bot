import argparse
from datetime import datetime


class MsgParser:
    def __init__(self, prog):
        self.parser = argparse.ArgumentParser(prog=prog)
        self.subparsers = self.parser.add_subparsers()
        self.apod_parser = self.subparsers.add_parser('apod')

        self.apod_param_group = self.apod_parser.add_mutually_exclusive_group()
        self.apod_param_group.add_argument('-c', '--count', type=int, dest='count')

        self.apod_date_group = self.apod_param_group.add_mutually_exclusive_group()
        self.apod_date_group.add_argument('-d', '--date', type=str, dest='date')

        self.apod_date_range_group = self.apod_date_group.add_argument_group()
        self.apod_date_range_group.add_argument('-s', '--start-date', type=str, dest='start_date')
        self.apod_date_range_group.add_argument('-e', '--end-date', type=str, dest='end_date')

        self.apod_parser.set_defaults(func=self._parse_apod_args)

    def _parse_apod_args(self, args):
        return {attr: self.convert_date(val) for (attr, val) in args.__dict__.items()}

    def parse(self, args):
        args = self.parser.parse_args(args)
        return args.func(args)

    @classmethod
    def convert_date(cls, arg):
        if isinstance(arg, str):
            date = datetime.strptime(arg, '%m/%d/%Y')
            date = date.strftime('%Y-%m-%d')
            return date
        else:
            return arg
