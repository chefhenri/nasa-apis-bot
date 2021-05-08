from discord import Client

from apod.client import ApodClient
from botutils.logger import BotLogger
from botutils.parser import MsgParser
from botutils.setup import load_config

config = load_config()
client = Client()
logger = BotLogger(log_lvl=config['LOG_LVL'])
parser = MsgParser(prog=config['PARSER_PROG'])
apod_client = ApodClient(endpoint=config['APOD_GQL_ENDPOINT'],
                         api_key=config['APOD_API_KEY'],
                         channel_id=config['BOT_CHANNEL_ID'],
                         channel_url=config['WEBHOOK_URL'],
                         logger=logger)


@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user}')
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!nasa') and message.channel.id == int(config['BOT_CHANNEL_ID']):
        # Parse message and fire webhook
        commands = parser.parse(message.content[5:].split())

        logger.info('Command received')

        await apod_client.handle(commands)


def main():
    client.run(config['BOT_TOKEN'])


if __name__ == '__main__':
    main()
