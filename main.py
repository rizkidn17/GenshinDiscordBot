import os
import random
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$play':
        await message.channel.send('-play https://www.youtube.com/playlist?list=PLxlvGuyZavQ6tP3feNTrEb0PYdIq7qalg')

    if message.content == '$nucode':
        code = random.randrange(10000,341628)
        await message.channel.send('http://www.nhentai.net/g/{}'.format(code))

keep_alive()
client.run(TOKEN)