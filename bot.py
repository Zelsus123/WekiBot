import discord
import os
import webserver
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Definicion de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='wk.', intents=intents, help_command=None)  # Desactiva el comando predeterminado de ayuda

#Evento que se ejecuta cuando el bot esta listo
@bot.event
async def on_ready():
    print(f'{bot.user} ha iniciado sesión en Discord!')
    try:
        synced = await bot.tree.sync()
        print(f'Comandos sincronizados: {len(synced)}')
    except Exception as e:
        print(f'Error al sincronizar comandos: {e}')
        

#comando para cargar un cog
@bot.command()
@commands.is_owner()
async def cargar(ctx, extension):
   try:
       await bot.load_extension(f'cogs.{extension}')
       await ctx.send(f'Cog {extension} cargado correctamente.')
   except Exception as e:
         await ctx.send(f'Error al cargar el cog {extension}: {e}')
         print(f'Error al cargar el cog {extension}: {e}')
         
# Comando para recargar un cog
@bot.command()
@commands.is_owner()
async def recargar(ctx, extension):
    try:
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cog {extension} recargado.')
    except Exception as e:
        await ctx.send(f'Error al recargar {extension}: {e}')

# Evento para manejar errores de comandos
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ese comando no existe. ¡Revisa la ortografía o usa !ayuda!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Falta un argumento necesario: {error}")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("¡No tienes permiso para usar este comando!")
    else:
        print(f"Error en el comando '{ctx.command}': {error}")
        await ctx.send("¡Ocurrió un error al ejecutar ese comando!")

# Carga inicial de los cogs al iniciar el bot
async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

bot.setup_hook = setup_hook

webserver.keep_alive()

# Inicia el bot
bot.run(TOKEN)