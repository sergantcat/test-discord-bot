import discord
import os
from discord.ext import commands

# Load the token from an environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Setup intents (required to read messages)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!')

@bot.command()
async def hi(ctx):
    await ctx.send("hi i just want to test the just run my app")

if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: No DISCORD_TOKEN found in environment variables.")
