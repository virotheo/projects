import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_permissions
from datetime import datetime
import pytz
load_dotenv()

local_timezone = pytz.timezone("Europe/Paris")

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all()) # give to bot all rights

@bot.event
async def on_ready():
        await bot.tree.sync()
        print(f"bot started")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user: # ignore hisself message
        return

    channel = bot.get_channel(1565126360299741264)
    message_channel = message.channel.id
    author = message.author
    content = message.content
    current_time = datetime.now(local_timezone)
    await channel.send(f"`Author : {author}\nMessage : {content}\nChannelID : {message_channel}\nTime : {current_time}`")
    
    if message.channel.id == 1564674535494651944: # setup the anti-bot verify
        if message.content == "VERIF":
            author = message.author
            role = discord.utils.get(message.guild.roles, name="Cookie") # Cookie = Member Role 
            await message.delete()
            await author.add_roles(role)
            await message.channel.send(f"{author} sucessfully verified", delete_after=4)
        else:
            author = message.author
            try:
                await message.delete()
            except:
                await message.channel.send("Error I think I have not enough permissions",delete_after=4)    
            await message.channel.send(f"{author} the verify failed, try again", delete_after=4)
            try: 
                await author.kick(reason="Captcha Failed")
            except:
                await message.channel.send("Error : I think I have not enough permissions",delete_after=4)    


@bot.tree.command(name='ping')
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(f"Pong : {round(bot.latency*1000)}ms")
            
@bot.tree.command(name='message_creator')
@has_permissions(administrator=True)
async def message_creator(interaction:discord.Interaction,message:str):
    await interaction.response.send_message(message)

bot.run(os.getenv('DISCORD_TOKEN')) # Your Token here
 
