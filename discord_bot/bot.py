import discord
import os
from dotenv import load_dotenv
import datetime
load_dotenv()


bot = discord.Client(intents=discord.Intents.all()) # give to bot all rights

@bot.event
async def on_ready():
    print("bot started")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user: # ignore hisself message
        return
    
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
            

bot.run(os.getenv('DISCORD_TOKEN')) # Your Token here
 
