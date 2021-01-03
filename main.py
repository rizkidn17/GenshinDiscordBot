import os
import random
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
import requests
import json


response = requests.get('https://api.genshin.dev/characters').text
response_info = json.loads(response)


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

    if message.content == '$test':
        await message.channel.send('Bot is Active!')

    if message.content == '$nucode':
        code = random.randrange(10000,341628)
        await message.channel.send('http://www.nhentai.net/g/{}'.format(code))

    if message.content == '$character':
        await message.channel.send(response_info)

keep_alive()
client.run(TOKEN)