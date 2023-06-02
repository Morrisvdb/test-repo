from discord.ext import commands
import discord
import os

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		client.load_extension("cogs." + f[:-3])

client.run(DISCORD_TOKEN)
