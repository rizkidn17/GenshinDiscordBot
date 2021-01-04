import os
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
import requests
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

char = 'https://api.genshin.dev/characters/{}'
img = 'https://rerollcdn.com/GENSHIN/Characters/{}.png'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
      
  elif arg != None:
      charlist = requests.get('https://api.genshin.dev/characters').text
      cl = json.loads(charlist)
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