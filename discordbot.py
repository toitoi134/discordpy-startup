from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)

import os
import random
import discord
from discord.ext import commands
from typing import Optional

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.command()
async def darts(ctx: commands.Context,　一般: str, name: Optional[str] = None):
    if ctx.author.bot:
        return
    await ctx.message.delete()

    一般 = 一般.lstrip("#")
    channels = ctx.guild.voice_channels
    for ch in channels:
        if ch.name == 一般:
            if not ch.members:
                await ctx.send(f"#{一般}には誰もいません")
                return
            member = random.choice(ch.members)
            msg = f"{狂人}に選ばれました！" if name is not None else "あなたが選ばれました！"
            await member.send(msg)
            return

    await ctx.send(f"#{一般}が存在しません")


TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
