import functools

from datetime import datetime

from utils.config import init_root_cfg
from utils.logger import BotLogger
from apod.client import ApodClient


def init(mode):
    init_root_cfg(f".env.{mode}")


def convert_date(_date):
    for fmt in ('%m/%d/%Y', '%d/%m/%Y', '%m.%d.%Y', '%d.%m.%Y', '%m-%d-%Y', '%d-%m-%Y', '%Y-%m-%d'):
        try:
            return datetime.strptime(_date, fmt).strftime('%Y-%m-%d')
        except ValueError:
            pass

    raise ValueError('No valid date format found')


@functools.lru_cache(maxsize=None)
def get_logger():
    return BotLogger()


@functools.lru_cache(maxsize=None)
def get_apod_client():
    return ApodClient(logger=get_logger())
