import discord
from discord.ext import commands

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Muestra la latencia del bot."""
        await ctx.send(f'Pong! Latencia: {round(self.bot.latency * 1000)}ms')

    @commands.command(aliases=['saludar'])
    async def hola(self, ctx, *, miembro: discord.Member = None):
        """Saluda a un miembro. Si no se menciona a nadie, te saluda a ti."""
        miembro = miembro or ctx.author
        await ctx.send(f'¡Hola, {miembro.mention}!')

    @commands.command()
    async def repetir(self, ctx, *, texto):
        """Hace que el bot repita lo que dices."""
        await ctx.send(texto)

async def setup(bot):
    await bot.add_cog(Comandos(bot))