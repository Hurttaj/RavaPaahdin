import random

from discord.ext.commands import Bot

BOT_PREFIX = "!"
TOKEN = "NDI2MzcxMDM1NzgxMTM2Mzg2.DZVAyw.6ih4fT3Mruql94dmlCIXpjeKpfU"

client = Bot(command_prefix=BOT_PREFIX)

counter = 0

@client.event
async def on_message(message):
    global counter
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('<:RavaPaahdin:414114101686435840>'):
        counter = counter + 1
        if counter == 6:
            msg = '<:RavaPaahdin:414114101686435840>'.format(message)
            await client.send_message(message.channel, msg)
            counter = 0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)