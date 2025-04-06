import discord
from discord.ext import commands
import random

class Pelea(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pelea", aliases=["wk.pelea"])
    async def pelea(self, ctx, miembro1: discord.Member = None, miembro2: discord.Member = None):
        """Simula una pelea épica entre dos miembros del servidor."""
        await ctx.message.delete()

        # Si no se especifican miembros, selecciona aleatoriamente
        miembros = [m for m in ctx.guild.members if not m.bot]
        if not miembro1:
            miembro1 = random.choice(miembros)
        if not miembro2:
            miembro2 = random.choice([m for m in miembros if m != miembro1])

        # Lista de resultados graciosos
        resultados = [
            f"{miembro1.mention} lanzó un plátano a {miembro2.mention}, pero resbaló y perdió. 🍌",
            f"{miembro1.mention} intentó usar un ataque especial, pero {miembro2.mention} lo esquivó con estilo y ganó. 🌀",
            f"{miembro1.mention} y {miembro2.mention} terminaron la pelea con un abrazo. ¡Todos ganan! 🤗",
            f"{miembro2.mention} invocó un ejército de patos y derrotó a {miembro1.mention}. 🦆",
            f"{miembro1.mention} ganó la pelea con un golpe final digno de una película de acción. 🎬",
            f"{miembro2.mention} usó una almohada como arma secreta y dejó fuera de combate a {miembro1.mention}. 🛏️",
            f"{miembro1.mention} y {miembro2.mention} se cansaron de pelear y decidieron jugar videojuegos juntos. 🎮",
            f"{miembro1.mention} intentó usar un hechizo mágico, pero se confundió y terminó perdiendo contra {miembro2.mention}. ✨",
            f"{miembro1.mention} tropezó mientras corría hacia {miembro2.mention} y quedó fuera de combate. 🤦‍♂️",
            f"{miembro2.mention} sacó un pastel y lo lanzó directo a la cara de {miembro1.mention}. ¡Victoria dulce! 🎂",
            f"{miembro1.mention} intentó intimidar a {miembro2.mention}, pero terminó asustándose de su propia sombra. 👻",
            f"{miembro2.mention} usó un ventilador gigante para soplar a {miembro1.mention} fuera del ring. 🌬️",
            f"{miembro1.mention} y {miembro2.mention} comenzaron a pelear, pero se unieron para derrotar a un bot malvado. 🤖",
            f"{miembro2.mention} lanzó un chiste tan malo que {miembro1.mention} se rindió por vergüenza. 😂",
            f"{miembro1.mention} intentó usar una espada de juguete, pero {miembro2.mention} tenía un escudo de cartón. 🛡️",
            f"{miembro2.mention} invocó un gato ninja que derrotó a {miembro1.mention} en segundos. 🐱‍👤",
            f"{miembro1.mention} intentó usar una técnica secreta, pero se quedó dormido en el proceso. 😴",
            f"{miembro2.mention} ganó la pelea con un movimiento de baile épico que dejó a {miembro1.mention} sin palabras. 💃",
            f"{miembro1.mention} y {miembro2.mention} decidieron resolver sus diferencias con una competencia de comer tacos. 🌮",
            f"{miembro2.mention} usó un globo de agua y dejó empapado a {miembro1.mention}. ¡Victoria refrescante! 💦",
            f"{miembro1.mention} intentó usar un ataque sorpresa, pero tropezó con una cáscara de plátano. 🍌",
            f"{miembro2.mention} invocó un ejército de hormigas y dejó a {miembro1.mention} sin opciones. 🐜",
            f"{miembro1.mention} y {miembro2.mention} terminaron la pelea con una batalla de rap. 🎤",
            f"{miembro2.mention} usó un hechizo de confusión y {miembro1.mention} comenzó a pelear contra una silla. 🪑",
            f"{miembro1.mention} intentó usar un ataque aéreo, pero quedó atrapado en una lámpara. 💡",
            f"{miembro2.mention} ganó la pelea al distraer a {miembro1.mention} con un meme épico. 😂",
            f"{miembro1.mention} y {miembro2.mention} decidieron que pelear era aburrido y se fueron a comer pizza. 🍕",
            f"{miembro2.mention} usó un ataque de cosquillas y dejó a {miembro1.mention} fuera de combate por la risa. 🤣",
            f"{miembro1.mention} intentó usar un truco ninja, pero se enredó en su propia capa. 🥷",
        ]

        # Elegir un resultado aleatorio
        resultado = random.choice(resultados)

        # Crear un embed para la pelea
        embed = discord.Embed(
            title="🥊 ¡Pelea Épica! 🥊",
            description=resultado,
            color=discord.Color.red()
        )
        embed.set_footer(text="¡Todo es por diversión, no se lo tomen en serio! 😄")

        # Enviar el embed
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Pelea(bot))