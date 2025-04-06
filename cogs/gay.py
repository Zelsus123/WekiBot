import discord
from discord.ext import commands
import random

class Gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gay", aliases=["wk.gay"])
    async def gay(self, ctx, miembro: discord.Member = None):
        """Calcula qué tan gay es un usuario."""
        await ctx.message.delete() 
        miembro = miembro or ctx.author
        porcentaje = random.randint(0, 100)

        # Comentarios graciosos según el porcentaje
        if porcentaje == 0:
            comentario = "😱 ¡Imposible! ¿Seguro que eres humano?"
        elif porcentaje <= 25:
            comentario = "🌈 Apenas un toque de arcoíris, pero ahí está."
        elif porcentaje <= 50:
            comentario = "🌈✨ ¡Tienes potencial, sigue brillando!"
        elif porcentaje <= 75:
            comentario = "🌈🔥 ¡Eres un arcoíris en llamas!"
        elif porcentaje < 100:
            comentario = "🌈💖 ¡Eres prácticamente la definición de fabuloso!"
        else:
            comentario = "🌈👑 ¡Eres el rey/reina del arcoíris! ¡Felicidades!"

        # Enviar el resultado
        await ctx.send(f"🏳️‍🌈 {miembro.mention} es un **{porcentaje}% gay**. {comentario}")

async def setup(bot):
    await bot.add_cog(Gay(bot))