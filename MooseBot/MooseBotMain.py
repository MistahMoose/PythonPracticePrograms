# bot.py
#pip install -U discord.py
#pip install -U python-dotenv
import os

import discord
from dotenv import load_dotenv
#https://github.com/theskumar/python-dotenv
#https://pypi.org/project/python-dotenv/

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()#Client represents a connection to discord

@client.event
async def on_ready(): #On ready establishes connection and prepares data from discord. Login/Guild/Channel
    #TODO Add Check for valid data (If name isnt in env, dont crash)
    guild = discord.utils.get(client.guilds, name=GUILD) #This line will only work if GUILD in .env file is findable, If not causes error
    # https://discordpy.readthedocs.io/en/latest/api.html#discord.utils.get


    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name} (id: {guild.id})'
        )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
@client.event
async def on_member_join(member):#Minimal code for interacting with users
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name,} welcome to my Discord Server!'
    )

@client.event
async def on_message(message):#Listens to messages in all channels/chats
    if message.author == client.user:
        return
    Bot_Response = 'Hello this is a reply from me, Moosebot.'
    if message.content == '!Verify':
        response = Bot_Response
        await message.channel.send(response)
    if message.content == 'Are you pooping?':
        response = 'Always.'
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise



#End of MooseBot Practice, Will be creating new file to change everything over to bot
#Bot is subset of client, May be easier to work with.


client.run(TOKEN)#Runs client using discord token
