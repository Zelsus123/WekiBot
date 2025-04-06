import discord
from discord.ext import commands

class Anonimo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="anonimo", aliases=["wk.anonimo"])
    async def anonimo(self, ctx, *, mensaje: str):
        """Permite a un usuario enviar un mensaje anónimo."""
        await ctx.message.delete()  # Elimina el mensaje del comando para mantener el anonimato

        # Crear un embed para el mensaje anónimo
        embed = discord.Embed(
            title="📩 Mensaje Anónimo 📩",
            description=mensaje,
            color=discord.Color.blue()
        )
        embed.set_footer(text="Mensaje enviado de forma anónima")

        # Enviar el mensaje al canal donde se ejecutó el comando
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Anonimo(bot))