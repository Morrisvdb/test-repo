from discord.ext import commands
import os

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
client = commands.Bot(command_prefix = "!")

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		client.load_extension("cogs." + f[:-3])

client.run(DISCORD_TOKEN)
