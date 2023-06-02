from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, client):
		self.client = client # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Ready Boss!")

	@commands.command(name="command", guild_ids=[977513866097479760, 1047234879743611034])
	async def command(self, ctx):
		await ctx.respond("Command")

def setup(client):
	client.add_cog(Test(client))