import discord
from discord.ext import commands
import random

class Feo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="feo", aliases=["wk.feo"])
    async def feo(self, ctx, miembro: discord.Member = None):
        """Calcula qué tan feo es un usuario."""
        await ctx.message.delete() 
        miembro = miembro or ctx.author
        porcentaje = random.randint(0, 100)

        # Comentarios graciosos según el porcentaje
        if porcentaje == 0:
            comentario = "😎 ¡Eres un modelo de revista! Nada de feo aquí."
        elif porcentaje <= 25:
            comentario = "😊 Apenas un poquito, pero sigue siendo adorable."
        elif porcentaje <= 50:
            comentario = "🤔 Bueno, digamos que tienes 'belleza única'."
        elif porcentaje <= 75:
            comentario = "😬 Tal vez no ganes concursos de belleza, pero tienes buena personalidad."
        elif porcentaje < 100:
            comentario = "😱 ¡Wow! Eres un caso especial, pero te queremos igual."
        else:
            comentario = "💀 ¡Felicidades! Has alcanzado el nivel máximo de fealdad."

        # Crear un embed para el mensaje
        embed = discord.Embed(
            title="🤡 Medidor de Fealdad 🤡",
            description=f"{miembro.mention} es un **{porcentaje}% feo**.\n{comentario}",
            color=discord.Color.orange()
        )
        embed.set_footer(text="¡La belleza está en el interior! 🌟")
        embed.set_thumbnail(url="https://i.imgur.com/3ZQ3ZKq.png")  # Cambia esta URL si deseas otra imagen

        # Enviar el embed
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Feo(bot))