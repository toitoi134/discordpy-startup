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

@bot.command()
async def darts(ctx: commands.Context, channel_name: str):
    if ctx.author.bot:
        return

    await ctx.message.delete()

    channel_name = channel_name.lstrip("#")
    channels = ctx.guild.voice_channels  # ボイスチャンネルリストを取得
    for ch in channels:
        if ch.name == channel_name:
            if not ch.members:
                await ctx.send(f"#{channel_name}には誰もいません")
                return
            member = random.choice(ch.members)
            await member.send("あなたが狂人に選ばれました！")
            return

    await ctx.send(f"#{channel_name}が存在しません")
