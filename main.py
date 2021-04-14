from discord import Client

from apod.client import ApodClient
from parser.parser import MsgParser
from setup import load_config

config = load_config()
client = Client()
parser = MsgParser(prog=config['PARSER_PROG'])
apod_client = ApodClient(endpoint=config['APOD_GQL_ENDPOINT'],
                         api_key=config['APOD_API_KEY'],
                         channel_id=config['BOT_CHANNEL_ID'],
                         channel_url=config['WEBHOOK_URL'])


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # TODO: lock to '#nasa-bot' channel
    if message.content.startswith('/nasa'):
        # Parse message and fire webhook
        commands = parser.parse(message.content[5:].split())

        await apod_client.handle(commands)


def main():
    client.run(config['BOT_TOKEN'])


if __name__ == '__main__':
    main()
