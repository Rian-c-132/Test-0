import discord
from discord.ext import commands
import random
from scrapeifunny import get_urls

client = commands.Bot(command_prefix = '.')
token = "NzU5ODAxNzI0OTE4NjkzOTA5.X3Cyfw.ZLNYu1qQRW_wm5xbfY2L7hQppB4"

@client.event
async def on_ready():
	print("Ready!")

@client.command()
async def ping(ctx):
	await ctx.send(f"Pong! {client.latency * 1000} ms.")

@client.command()
async def clear(ctx, amount = 5):
	await ctx.channel.purge(limit = amount)

@client.command()
async def meme(ctx, site = "memedroid"):
	embed = discord.Embed()
	imgs = get_urls(site)
	temp = random.choice(imgs)
	embed.set_image(url= temp)
	await ctx.send(embed = embed)



client.run(token) # token

