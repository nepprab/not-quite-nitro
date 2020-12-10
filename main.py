from discord.ext import commands
import discord

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents = intents)

try:
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			client.load_extension(f"cogs.{filename[:-3]}")
except Exception as e:
	print("Cogs error: Cannot load cogs")
	print("\033[5;37;40m\033[1;33;40mWARNING\033[1;33;40m\033[0;37;40m", end=' ')
	print("Functionality limited!\n")
	print(f"exception thrown:\n{e}")

@client.event
async def on_ready():
  print("The bot is ready!")

@client.command()
async def ping(ctx, message=True):
    message = await ctx.send("Pinging...")
    await message.edit(content = f"Pong! `{round(client.latency * 1000)}ms`")	

client.run("TOKEN")
