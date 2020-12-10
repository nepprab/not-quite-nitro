from discord.ext import commands
import discord

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents = intents)

@client.event
async def on_ready():
  print("The bot is ready!")

@client.command()
async def ping(ctx, message=True):
    message = await ctx.send("Pinging...")
    await message.edit(content = f"Pong! `{round(client.latency * 1000)}ms`")	

client.run("token")