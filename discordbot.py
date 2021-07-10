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

@bot.command()
async def rimaru(ctx):
    await ctx.send('りまるはあほ')
    
    
import os
import random
import discord
from discord.ext import commands
from typing import Optional

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command()
async def da(ctx: commands.Context, channel_name: str, name: Optional[str] = None):
    if ctx.author.bot:
        return
    await ctx.message.delete()

    channel_name = channel_name.lstrip("#")
    channels = ctx.guild.voice_channels
    for ch in channels:
        if ch.name == channel_name:
            if not ch.members:
                await ctx.send(f"#{channel_name}には誰もいません")
                return
            member = random.choice(ch.members)
            msg = f"{狂人}に選ばれました！" if name is not None else "あなたが狂人に選ばれました！あなた以外が全員タスクを終わらせてた場合インポスター側の負けになります。"
            await member.send(msg)
            return

    await ctx.send(f"#{channel_name}が存在しません")


TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
