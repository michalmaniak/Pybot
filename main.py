import discord
from discord.ext import commands
import urllib
import json
import asyncio
from datetime import date
from discord_tokens import secret
bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def info(ctx):
    reply = "Check out my source code at https://github.com/michalmaniak/Pybot"
    await ctx.send(reply)

@bot.command()
async def cat(ctx):
    with urllib.request.urlopen("https://api.thecatapi.com/v1/images/search") as url:
        s = url.read()
        loaded_json = json.loads(s)
        e = discord.Embed()
        e.set_image(url=loaded_json[0]['url'])
        await ctx.send(embed=e)


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect(force=True)

@bot.command()
async def plan(ctx):
    weekNumber = date.today().isocalendar()[1]
    if (weekNumber % 2 == 0):
        address = "https://i.imgur.com/jAfPryR.png"
    else:
        address = "https://i.imgur.com/bhUd1sQ.png"
    g = discord.Embed()
    g.set_image(url=address)
    g.set_footer(text="Timetable for this week")

    await ctx.send(embed=g)

bot.run(secret)
