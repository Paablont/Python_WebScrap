import os
import datetime
import discord
from discord.ext import tasks,commands
import PeliculasDiarias


TOKEN = 'MTE3MjQ1Nzc4ODc5OTE4OTAwMg.GPKsym.2XTECbWcgZBzOFFPxsUPeZsrqelo1KF7gbG2vU'


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Habilitar la intención de contenido de mensaje

bot = commands.Bot(command_prefix='!', intents=intents)


#
# @bot.command(name='saludar',help='Saluda al bot')
# async def saludar(ctx):
#     await ctx.send(f'Hola, {ctx.author.mention}!')
# bot.run(TOKEN)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    event_Film.start()

@tasks.loop(hours=24)
async def event_Film():
    fecha = datetime.date.today()
    fechaActual = fecha.strftime('%d de %m de %Y')
    urlDiarias = "https://www.filmaffinity.com/es/rdcat.php?id=new_th_es"

    movies_result = PeliculasDiarias.peliculasDiarias(urlDiarias, fechaActual)
    channel = bot.get_channel(int("1171870938636226592"))

    try:
        if channel is not None:
            if movies_result:
                for result in movies_result:
                    await channel.send(embed=result.to_embed())
            else:
                await channel.send("No hay pelis hoy")
        else:
            print("Error: El canal no se encontró.")
    except Exception as e:
        await channel.send(f"Error al enviar mensajes al canal: {e}")
bot.run(TOKEN)