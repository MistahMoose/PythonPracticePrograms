import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NTI3ODc1MjIzNzI3Mzc0MzQ2.Xuv0Mw.fA2sfBMraXsZfb0ZEJ-Q1cMVaOY')