import discord
from discord.ext import commands
import random

class Borracho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="borracho", aliases=["wk.borracho"])
    async def borracho(self, ctx, miembro: discord.Member = None):
        """Calcula qué tan borracho está un usuario."""
        await ctx.message.delete() # Elimina el mensaje del comando
        miembro = miembro or ctx.author
        porcentaje = random.randint(0, 100)
       
        # Comentarios graciosos según el porcentaje
        if porcentaje == 0:
            comentario = "🍹 ¡Estás más sobrio que un monje en meditación!"
        elif porcentaje <= 25:
            comentario = "🍺 Apenas un par de cervezas, estás bien."
        elif porcentaje <= 50:
            comentario = "🍷 Ya empiezas a tambalearte, cuidado con las escaleras."
        elif porcentaje <= 75:
            comentario = "🥴 ¡Estás viendo doble! Mejor siéntate un rato."
        elif porcentaje < 100:
            comentario = "🤢 ¡Estás al borde de cantar karaoke! Alguien quítale el micrófono."
        else:
            comentario = "💀 ¡Estás tan borracho que ni recuerdas tu nombre! Llama a un taxi."

        # Enviar el resultado
        await ctx.send(f"🍻 {miembro.mention} está un **{porcentaje}% borracho**. {comentario}")

async def setup(bot):
    await bot.add_cog(Borracho(bot))