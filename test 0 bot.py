import discord
from discord.ext import commands
import random
from scrapeifunny import get_urls

client = commands.Bot(command_prefix = '.')
token = "NzU5ODAxNzI0OTE4NjkzOTA5.X3Cyfw.lS3iskNmK_sis46Jift--_lvNGg"

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
async def meme(ctx):
	embed = discord.Embed()
	imgs = get_urls()
	temp = random.choice(imgs)
	embed.set_image(url= temp)
	await ctx.send(embed = embed)


@client.command()
async def roast(ctx, member : discord.Member):
	responses = [ "If I wanted to suicide, I would climb your ego and jump onto your iq.",
				"You are as useless as the 'ueue' in 'queue'.",
				"If I had a face like yours, I'd sue my parents.",
				"Some day you'll go far and I hope you stay there.",
				"You are a prime candidate for natural de-selection.",
				"The trash will get picked up tomorrow, be ready.",
				"You are not useless because you can still be used as a bad example."]
	await ctx.send(f"{member.mention} {random.choice(responses)}")

@client.command()
async def pp(ctx, member : discord.Member):
	sz = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	msg = discord.Embed(title = f"{member}'s pp\n",
		description = f"8{random.choice(sz)*'='}D")
	await ctx.send(embed = msg)

client.run(token) # token

