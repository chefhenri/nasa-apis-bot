import functools
import sys

from datetime import date, datetime
from discord.ext import commands

from apod.client import ApodClient
from utils.config import init_root_cfg, get_client_cfg
from utils.logger import BotLogger
bot_client = commands.Bot(command_prefix='/')


# TODO: Decorate with logging
@bot_client.event
async def on_ready():
    print(f'Logged in as {bot_client.user}')


@bot_client.command(name='apod', aliases=['today'])
async def _apod(ctx, _date=date.today().strftime('%m/%d/%Y')):
    await get_apod_client().handle({'date': convert_date(_date)})


def convert_date(_date):
    return datetime.strptime(_date, '%m/%d/%Y').strftime('%Y-%m-%d')


@functools.lru_cache(maxsize=None)
def get_logger():
    return BotLogger()


@functools.lru_cache(maxsize=None)
def get_apod_client():
    return ApodClient(logger=get_logger())


def main():
    init_root_cfg(f".env.{sys.argv[1]}")
    bot_client.run(get_client_cfg()['token'])


if __name__ == '__main__':
    main()
