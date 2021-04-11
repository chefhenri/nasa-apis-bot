from discord import Client
from parser.parser import MsgParser
from setup import load_config

config = load_config()
client = Client()
parser = MsgParser(config['PARSER_PROG'])


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/nasa') and message.channel.id == config['BOT_CHANNEL_ID']:
        # Parse message and fire webhook
        pass


def main():
    # client.run(config['BOT_TOKEN'])
    print(parser.parse('apod -d 06/28/1999'.split()))


if __name__ == '__main__':
    main()
