from discord.ext import commands
import discord
import os

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@client.slash_command(name="test", guild_ids=[977513866097479760, 1047234879743611034])
async def test(ctx, arg):
	await ctx.respond(arg)

client.run(DISCORD_TOKEN)
