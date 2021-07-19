import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='.')
status = cycle(['.info', '頑 張る', '화이팅'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot nya udh bangun bos.')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Commend nya salah bro. Coba cek ketik .info :D | (SEMANGAT YA <3)')

# @clear.error()
# async def clear_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('salah.')


@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# ---------------------------------------------------------------------------------------------------------


@client.command()
async def pas_kamis(ctx):
    await ctx.send("Jadwal P.A.S hari Kamis : IPS (07.30 - 09.00) | Sunda (09.30 - 11.00) | Penjas (11.30 - 13.00)  Semangat belajar yaa...")


@client.command()
async def pas_jumat(ctx):
    await ctx.send("Jadwal P.A.S hari Jumat : MTK (07.30 - 09.30) | TIK (10.00 - 11.30) Semangat belajar yaa...")


@client.command()
async def pas_senin(ctx):
    await ctx.send("Jadwal P.A.S hari Senin : INDO (07.30 - 09.30) | PAI (10.00 - 11.30) Semangat belajar yaa...")


@client.command()
async def pas_selasa(ctx):
    await ctx.send("Jadwal P.A.S hari Selasa : Inggris (07.30 - 09.30) | Sunda (10.00 - 11.30) Semangat belajar yaa...")


@client.command()
async def pas_rabu(ctx):
    await ctx.send("Jadwal P.A.S hari Rabu : IPA (07.30 - 09.30) | PKN (10.00 - 11.30) Semangat belajar yaa...")

# ---------------------------------------------------------------------------------------------------------


@client.command()
async def jadwal_senin(ctx):
    await ctx.send("Jadwal hari Senin : Pai (08.00 - 09.30) | Indo (10.00 - 11.30)   Semangat belajar yaa...")


@client.command()
async def jadwal_selasa(ctx):
    await ctx.send("Jadwal hari Selasa : B.Inggris (08.00 - 09.30) | Seni Budaya (10.00 - 11.30)   Semangat belajar yaa...")


@client.command()
async def jadwal_rabu(ctx):
    await ctx.send("Jadwal hari Rabu : IPA (08.00 - 09.30) | PKN (10.00 - 11.30)   Semangat belajar yaa...")


@client.command()
async def jadwal_kamis(ctx):
    await ctx.send("Jadwal hari Kamis : IPS (08.00 - 09.30) | Sunda (10.00 - 11.30)   Semangat belajar yaa...")


@client.command()
async def jadwal_jumat(ctx):
    await ctx.send("Jadwal hari Jum'at : Penjas (07.30 - 08.30) | MTK (09.00 - 10.30) | TIK (10.30 - 11.30)  Semangat belajar yaa...")


@client.command()
async def info(ctx):
    await ctx.send("List Command buat ini bot \n 1. .jadwal_senin \n 2. .jadwal_selasa \n 3. .jadwal_rabu \n 4. .jadwal_kamis \n 5. .jadwal_jumat \n BOT INI DI BIKIN OLEH LUKARINKI (@fahmi.hafiansyah)")


client.run('#Discord_Token')
