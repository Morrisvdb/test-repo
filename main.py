from discord.ext import commands
import discord
import os

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@client.command()
async def test(ctx, arg):
	await ctx.send(arg)

client.run(DISCORD_TOKEN)
