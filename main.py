from discord import Client

from apod.client import ApodClient
from botutils.config import get_config
from botutils.logger import BotLogger
from botutils.parser import MsgParser

bot_config = get_config('.env')

client = Client()
logger = BotLogger(log_lvl=bot_config['LOG_LVL'], log_dir=bot_config['LOG_DIR'])
parser = MsgParser(prog=bot_config['PARSER_PROG'])
apod_client = ApodClient(config=bot_config, logger=logger)


@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user}')
    print(f'Logged in as {client.user}')


# TODO: Decorate with logging
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!nasa') and message.channel.id == int(bot_config['BOT_CHANNEL_ID']):
        # Parse message into commands
        commands = parser.parse(message.content[5:].split())

        logger.info('Command received')

        # Handle commands and fire webhook
        await apod_client.handle(commands)


def main():
    client.run(bot_config['BOT_TOKEN'])


if __name__ == '__main__':
    main()
