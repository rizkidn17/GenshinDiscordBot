import os
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
import requests
import json
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='$')

url = 'https://api.genshin.dev/characters/{}'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.command()
async def character(ctx, arg):
      response = requests.get(url.format(arg)).text
      data = json.loads(response)
      embeded = discord.Embed(title=data['name'],description=data['description'])
      await ctx.send(embed=embeded)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.event #print that the bot is ready to make sure that it actually logged on
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

    # if message.content == '$test':
    #     await message.channel.send('Bot is Active!')

    # if message.content == '$character':
    #     response = requests.get(url.format('albedo')).text
    #     data = json.loads(response)
    #     embed = discord.Embed(title=data['name'],description=data['description'])
    #     await message.channel.send(embed=embed)

keep_alive()
bot.run(TOKEN)