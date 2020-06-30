#bot.py
import os
import random
from dotenv import load_dotenv


from discord.ext import commands#bot imported from discord.ext.commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to discord! \n')

@bot.command(name = 'poop', help='Responds with a random quote about poop')
async def poop(ctx): #Any Command function (technically called a callback) must accept at least one parameter, called ctx, which is the Context surrounding the invoked Command.
    poop_quotes = [
        'yeet',
        'amazing',
        'poop',
        (
            'Bigger quote here?'
        ),
    ]
    response = random.choice(poop_quotes)
    await ctx.send(response)
    
@bot.command(name='roll', help='Rolls a d20')
async def roll(ctx, number_of_dice: int, number_of_sides: int):#Added int annotations to change str numbers to int
    dice = [
        str(random.choice(range(1,number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]#creates a list of dice based on number of dice rolled !roll 1 10
    #would need to parse out the d if I wanted it to be !roll 1d10
    await ctx.send(','.join(dice))




bot.run(TOKEN)

