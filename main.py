import os
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
import requests
import json
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

char = 'https://api.genshin.dev/characters/{}'
art = 'https://api.genshin.dev/artifacts/{}'
wp = 'https://api.genshin.dev/weapons/{}'
imgc = 'https://rerollcdn.com/GENSHIN/Characters/{}.png'
imga = 'https://rerollcdn.com/GENSHIN/Gear/{}.png'
imgw = 'https://rerollcdn.com/GENSHIN/Weapon/NEW/{}.png'

charlist = requests.get('https://api.genshin.dev/characters').text
cl = json.loads(charlist)
artlist = requests.get('https://api.genshin.dev/artifacts').text
al = json.loads(artlist)
wplist = requests.get('https://api.genshin.dev/weapons').text
wl = json.loads(wplist)


@bot.command()
async def character(ctx, *, arg=None):
  if arg == None:
      embeded = discord.Embed(title="Character List")
      for i in cl:
        response = requests.get(char.format(i)).text
        data = json.loads(response)
        embeded.add_field(name=i.title().replace("-", " "), value="{} Star | {}".format(data['rarity'],data['vision']), inline=True)
      await ctx.send(embed=embeded)

  # elif arg == "traveler geo":
  #     response = requests.get(char.format("traveler-geo")).text
  #     data = json.loads(response)
  #     embeded = discord.Embed(title=data['name'],description=data['description'])
  #     embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png') 
  #     embeded.add_field(name="Vision", value=data['vision'], nline=True)
  #     embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
  #     embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
  #     await ctx.send(embed=embeded)
    
  # elif arg == "traveler anemo":
  #     response = requests.get(char.format("traveler-anemo")).text
  #     data = json.loads(response)
  #     embeded = discord.Embed(title=data['name'],description=data['description'])
  #     embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
  #     embeded.add_field(name="Vision", value=data['vision'], inline=True)
  #     embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
  #     embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
  #     await ctx.send(embed=embeded)

  elif arg != None:
      arg = arg.replace(" ", "-")
      if arg in cl:
        response = requests.get(char.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'.replace("-", "")],description=data['description'])
        if arg == "traveler-geo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Geo).png')
        elif arg == "traveler-anemo":
          embeded.set_thumbnail(url='https://rerollcdn.com/GENSHIN/Characters/Traveler%20(Anemo).png') 
        else:
          embeded.set_thumbnail(url=imgc.format(data['name'])) 
        embeded.add_field(name="Vision", value=data['vision'], inline=True)
        embeded.add_field(name="Weapon", value=data['weapon'], inline=True)
        embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))



@bot.command()
async def artifact(ctx, *, arg=None): 
    if arg == None:
      def listToString(wl):  
        str1 = "\n" 
        return (str1.join(wl))  
      artlist = requests.get('https://api.genshin.dev/artifacts').text
      al = json.loads(artlist) 
      embeded = discord.Embed(title="Artifact List", description=listToString(al).title().replace("-", " "))
      await ctx.send(embed=embeded)

      
      # embeded = discord.Embed(title="Artifact List")
      # artlist = requests.get('https://api.genshin.dev/artifacts').text
      # al = json.loads(artlist)
      # for i in al:
      #   response = requests.get(art.format(i)).text
      #   data = json.loads(response)
      #   embeded.add_field(name=i.title().replace("-", " "), value="2P: {}\n4P: {}".format(data['2-piece_bonus'], data['4-piece_bonus']), inline=True)
      # await ctx.send(embed=embeded)

    elif arg != None:
      arg = arg.replace(" ", "-")
      artlist = requests.get('https://api.genshin.dev/artifacts').text
      al = json.loads(artlist)
      if arg in al:
        response = requests.get(art.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'])
        embeded.set_thumbnail(url=imga.format(data['name'].lower().replace(" ", "_")))
        embeded.add_field(name="Rarity", value=data['max_rarity'], inline=True) 
        embeded.add_field(name="2 Pieces", value=data['2-piece_bonus'], inline=False)
        embeded.add_field(name="4 Pieces", value=data['4-piece_bonus'], inline=False)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))

@bot.command()
async def weapon(ctx, *, arg=None): 
    if arg == None:
      def listToString(wl):  
        str1 = "\n" 
        return (str1.join(wl))  
      wplist = requests.get('https://api.genshin.dev/weapons').text
      wl = json.loads(wplist)  
      embeded = discord.Embed(title="Weapon List", description=listToString(wl).title().replace("-", " "))
      await ctx.send(embed=embeded)
      # for i in wl:
      #   response = requests.get(wp.format(i)).text
      #   data = json.loads(response)
      #   embeded.add_field(name=i.title().replace("-", " "), value="Type: {}".format(data['type']), inline=True)
      # await ctx.send(embed=embeded)

    elif arg != None:
      arg = arg.replace(" ", "-")
      if arg in wl:
        response = requests.get(wp.format(arg)).text
        data = json.loads(response)
        embeded = discord.Embed(title=data['name'])
        embeded.set_thumbnail(url=imgw.format(data['name'].replace(" ", "_")))
        embeded.add_field(name="Type", value=data['type'], inline=True)
        embeded.add_field(name="Rarity", value=data['rarity'], inline=True)
        embeded.add_field(name="Base ATK", value=data['baseAttack'], inline=True) 
        embeded.add_field(name="Sub Stat", value=data['subStat'], inline=False)
        embeded.add_field(name="Passive: {}".format(data['passiveName']), value=data['passiveDesc'], inline=False)
        await ctx.send(embed=embeded)
      else:
        await ctx.send("{} not Found!".format(arg).title().replace("-", " "))

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