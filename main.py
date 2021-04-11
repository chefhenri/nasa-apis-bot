from discord import Client
from setup import load_config

config = load_config()
client = Client()


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
    client.run(config['BOT_TOKEN'])


if __name__ == '__main__':
    main()
