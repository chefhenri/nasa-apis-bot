import sys
from datetime import date

from discord.ext import commands

from apod.client import get_apod_client, convert_date
from utils.config import get_client_cfg, init_root_cfg, get_logger_cfg
from utils.logging import init_logger

bot_client = commands.Bot(command_prefix='/')


# TODO: Wrap logging, integration tests
@bot_client.event
async def on_ready():
    print(f'Logged in as {bot_client.user}')


# TODO: Wrap logging, integration tests
@bot_client.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandNotFound):
        pass


# TODO: Wrap logging, integration tests
@bot_client.command(name='apod', aliases=['today'])
async def _apod(ctx, _date: str = date.today().strftime('%m/%d/%Y')):
    try:
        _date = convert_date(_date)
    except ValueError:
        await ctx.send('Sorry, I don\'t recognize that date format.')

    await get_apod_client().handle({'date': _date})


def init(mode):
    init_root_cfg(f".env.{mode}")
    logger_cfg = get_logger_cfg()
    init_logger(log_lvl=logger_cfg['log_lvl'], log_dir=logger_cfg['log_dir'])


def main():
    init(sys.argv[1])
    bot_client.run(get_client_cfg()['token'])


if __name__ == '__main__':
    main()
