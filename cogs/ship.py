import discord
from discord.ext import commands
import random

class Ship(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ship", aliases=["wk.ship"])
    async def ship(self, ctx, miembro1: discord.Member = None):
        """Shipea a un usuario con otro usuario aleatorio del servidor."""
        await ctx.message.delete()

        miembro1 = miembro1 or ctx.author

        # Obtener una lista de miembros aleatorios (excluyendo bots y al miembro1)
        miembros = [m for m in ctx.guild.members if not m.bot and m != miembro1]
        if not miembros:
            await ctx.send("No hay suficientes miembros para shipear. 😔")
            return

        miembro2 = random.choice(miembros)

        # Calcular el porcentaje de compatibilidad
        compatibilidad = random.randint(0, 100)

        # Crear el nombre del ship
        nombre_ship = self.generar_nombre_ship(miembro1.display_name, miembro2.display_name)

        embed = discord.Embed(
            title="💖 ¡El amor está en el aire! 💖",
            description=f"¡Estamos shipeando a {miembro1.mention} con {miembro2.mention}!",
            color=discord.Color.magenta()
        )
        embed.add_field(name="Nombre del Ship:", value=nombre_ship, inline=False)
        embed.add_field(name="Porcentaje de Compatibilidad:", value=f"{compatibilidad}%", inline=False)

        # Comentarios graciosos según la compatibilidad
        if compatibilidad <= 25:
            comentario = "¡Uy, esto va a ser difícil! 😅"
        elif compatibilidad <= 50:
            comentario = "¡Hay potencial, pero necesitan trabajar en ello! 🤔"
        elif compatibilidad <= 75:
            comentario = "¡Las cosas pintan bien! 😊"
        else:
            comentario = "¡Destinados a estar juntos! 😍"

        embed.set_footer(text=comentario)
        embed.set_thumbnail(url="https://media.giphy.com/media/ZOStzpF9H5syI/giphy.gif?cid=790b7611gbks1nbswom889dpu54m81e0896zmd4oeoacq8s3&ep=v1_gifs_search&rid=giphy.gif&ct=g")  # Reemplaza con una imagen de ship

        await ctx.send(embed=embed)

    def generar_nombre_ship(self, nombre1, nombre2):
        """Genera un nombre de ship combinando los nombres de los usuarios."""
        longitud_minima = min(len(nombre1), len(nombre2))
        
        # Tomar una parte del primer nombre y una parte del segundo nombre
        parte1 = nombre1[:longitud_minima // 2]
        parte2 = nombre2[longitud_minima // 2:]
        
        return parte1 + parte2

async def setup(bot):
    await bot.add_cog(Ship(bot))