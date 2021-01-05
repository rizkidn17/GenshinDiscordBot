import os
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
import requests
import json
from discord.ext import commands
import numpy as np

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

char = 'https://api.genshin.dev/characters/{}'
art = 'https://api.genshin.dev/artifacts/{}'
img = 'https://rerollcdn.com/GENSHIN/Characters/{}.png'

charlist = requests.get('https://api.genshin.dev/characters').text
cl = json.loads(charlist)
# arr = np.array(cl)

# print("The Numpy Array is : ")
# for i in arr:
#   print(i, end = ' ')




@bot.command()
async def character(ctx, *, arg):
  if arg == "traveler geo":
      response = requests.get(char.format("traveler-geo")).text
      data = json.loads(response)
      embeded = discord.Embed(title=data['name'],description=data['description'])
      embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png') 
      embeded.add_field(name="Vision", value=data['vision'], inline=True)
      embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
      embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
      await ctx.send(embed=embeded)
    
  elif arg == "traveler anemo":
      response = requests.get(char.format("traveler-anemo")).text
      data = json.loads(response)
      embeded = discord.Embed(title=data['name'],description=data['description'])
      embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
      embeded.add_field(name="Vision", value=data['vision'], inline=True)
      embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
      embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
      await ctx.send(embed=embeded)
  elif arg is None:
      await ctx.send(cl)

  elif arg != None:
      if arg in cl:
        response = requests.get(char.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'],description=data['description'])
        embeded.set_thumbnail(url=img.format(data['name'])) 
        embeded.add_field(name="Vision", value=data['vision'], inline=True)
        embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
        embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).capitalize())



@bot.command()
async def artifact(ctx, *, arg):
    narg = arg.replace(" ", "-")
    if narg != None:
      artlist = requests.get('https://api.genshin.dev/artifacts').text
      al = json.loads(artlist)
      if narg in al:
        response = requests.get(art.format(narg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'])
        # embeded.set_thumbnail(url=img.format(data['name']))
        embeded.add_field(name="Rarity", value=data['max_rarity'], inline=True) 
        embeded.add_field(name="2 Pieces", value=data['2-piece_bonus'], inline=False)
        embeded.add_field(name="4 Pieces", value=data['4-piece_bonus'], inline=False)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).capitalize())


@bot.command()
async def about(ctx):
    embeded = discord.Embed(title='GI Bot',description="Currently we only provide Character's Brief Details. Feel free to support us with idea in [Github](https://github.com/rizkidn17/GenshinDiscordBot)")
    embeded.set_footer(text='Disclaimer: This bot only for personal use and not related with Official Genshin Impact and Mihoyo')
    await ctx.send(embed=embeded)


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