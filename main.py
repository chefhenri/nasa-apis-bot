import functools
import sys

from discord import Client

from apod.client import ApodClient
from utils.logger import BotLogger
from utils.parser import MsgParser
from utils.config import init_root_cfg, get_client_cfg

client = Client()


@client.event
async def on_ready():
    get_logger().info(f'Logged in as {client.user}')
    print(f'Logged in as {client.user}')


# TODO: Decorate with logging
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!nasa'):
        # Parse message into commands
        commands = get_parser().parse(message.content[5:].split())

        get_logger().info('Command received')

        # Handle commands and fire webhook
        await get_apod_client().handle(commands)


@functools.lru_cache(maxsize=None)
def get_parser():
    return MsgParser()


@functools.lru_cache(maxsize=None)
def get_logger():
    return BotLogger()


@functools.lru_cache(maxsize=None)
def get_apod_client():
    return ApodClient(logger=get_logger())


def main():
    init_root_cfg(f".env.{sys.argv[1]}")
    client.run(get_client_cfg()['token'])


if __name__ == '__main__':
    main()
