import os
import datetime
import discord
from discord.ext import tasks,commands



TOKEN = 'MTE3MTg3MTQ0NzQ3MjQxODgxNg.GdwLU5.UmLJYp8DiwXToSHEB_ckKIJjG5F29BUoUv8eok'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Habilitar la intención de contenido de mensaje

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command(name='saludar',help='Saluda al bot')
async def saludar(ctx):
    await ctx.send(f'Hola, {ctx.author.mention}!')

#prueba
bot.run(TOKEN)
# @tasks.loop(hours=24) # Se ejecutará cada 24 horas
# async def event_Film():
#     fecha = datetime.date.today()
#     fechaActual = fecha.strftime('%d de %m de %Y')
#     urlDiarias = "https://www.filmaffinity.com/es/rdcat.php?id=new_th_es"
#
#     movies_result =  main.peliculasDiarias(urlDiarias,fechaActual)
#     channel = bot.get_channel(int("1171870938636226592")) # PASAMOS LA ID DEL CHAT DE DISCORD
#     try:
#         for result in movies_result:
#             await channel.send(str(result))
#     except Exception as e:
#         await channel.send("No hay pelis hoy")
#         print(f"Error al enviar mensajes al canal: {e}")
#
# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')
#     event_Film.start()
# bot.run(TOKEN)