import discord
from discord.ext import commands
import os

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
bot = commands.Bot()

@bot.slash_commands(name="test", description="Test", guild_ids=[977513866097479760, 1047234879743611034])
async def test(ctx, arg):
	await ctx.send(arg)

bot.run(DISCORD_TOKEN)
