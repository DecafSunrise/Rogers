"""
      ______    _______  _______  _______  ______    _______
     |    _ |  |       ||       ||       ||    _ |  |       |
    |   | ||  |   _   ||    ___||    ___||   | ||  |  _____|
   |   |_||_ |  | |  ||   | __ |   |___ |   |_||_ | |_____
  |    __  ||  |_|  ||   ||  ||    ___||    __  ||_____  |
 |   |  | ||       ||   |_| ||   |___ |   |  | | _____| |
|___|  |_||_______||_______||_______||___|  |_||_______|

- https://realpython.com/how-to-make-a-discord-bot-python/
- https://www.vultr.com/docs/how-to-run-a-python-discord-bot-on-a-docker-application/
"""

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
from insult import *

# intents = discord.Intents(messages=True, members=True)
intents = discord.Intents.all()

TOKEN = os.getenv('TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def joined(ctx, *, member: discord.Member):
    greeting = f"""Howdy {member}? They call me Roger the Robot. You can find out about my capabilities by sending `!help`, or use `!<command>` to task me."""
    await ctx.send(greeting)



# @commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@commands.cooldown(1, 15, commands.BucketType.user)
@bot.command(name='insult', help='Sends an insult')
async def insult(ctx):
    await ctx.send(get_insult())

@commands.cooldown(1, 15, commands.BucketType.user)
@bot.command(name='trump', help='Returns a stupid Trump quote')
async def trump(ctx):
    await ctx.send(get_trump())


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds')


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

bot.run(TOKEN)