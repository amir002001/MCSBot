import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('ready')


@client.command()
async def say(context, *, string):
    await context.send(string)


client.run('<Placeholder for Token>')
