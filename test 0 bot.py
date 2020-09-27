import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
token = ""
@client.event
async def on_ready():
	print("Ready!")

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! {client.latency * 1000} ms.")

@client.command()
async def clear(ctx, amount = 5):
	await ctx.channel.purge(limit = 5)

client.run(token) # token

