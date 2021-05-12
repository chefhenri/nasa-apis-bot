import sys
from datetime import date

from discord.ext import commands

from utils.config import get_client_cfg
from utils.root import init, convert_date, get_apod_client

bot_client = commands.Bot(command_prefix='/')


# TODO: Add logging
@bot_client.event
async def on_ready():
    print(f'Logged in as {bot_client.user}')


# TODO: Add logging
@bot_client.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.CommandNotFound):
        pass


# TODO: Add logging
@bot_client.command(name='apod', aliases=['today'])
async def _apod(ctx, _date: str = date.today().strftime('%m/%d/%Y')):
    try:
        _date = convert_date(_date)
    except ValueError:
        await ctx.send('Sorry, I don\'t recognize that date format.')

    await get_apod_client().handle({'date': _date})


def main():
    init(sys.argv[1])
    bot_client.run(get_client_cfg()['token'])


if __name__ == '__main__':
    main()
