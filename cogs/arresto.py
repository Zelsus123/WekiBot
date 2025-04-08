import discord
from discord.ext import commands
import random

class Arresto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.motivos_arresto_solo = [
            "por intentar robarle el corazón a alguien.",
            "por exceso de ternura en la vía pública.",
            "por usar calcetines con sandalias.",
            "por bailar cumbia a las 3 AM.",
            "por creerse Batman sin tener un Batmóvil.",
            "por intentar pagar con billetes de Monopoly.",
            "por acaparar todos los memes de gatitos.",
            "por declararle la guerra a las tostadoras.",
            "por intentar domesticar una paloma.",
            "por confundir un semáforo con un árbol de Navidad.",
            "por intentar venderle un peine a un calvo.",
            "por usar el WiFi del vecino sin permiso.",
            "por organizar una fiesta de cumpleaños para su planta.",
            "por intentar cruzar la calle en patines durante la hora pico.",
            "por intentar sobornar a un policía con galletas.",
            "por retar a duelo de miradas a un maniquí.",
            "por intentar volar con una capa hecha de servilletas.",
            "por intentar clonar ovejas en el Minecraft.",
            "por intentar vender agua del grifo como agua mineral.",
            "por intentar convencer a la gente de que la Tierra es plana.",
            "por intentar cambiarle el nombre a un perro por 'Firulais'.",
        ]
        self.motivos_arresto_con_otro = [
            "por intentar venderle un unicornio a {otro_usuario}.",
            "por intentar robarle el peluquín a {otro_usuario}.",
            "por intentar hipnotizar a {otro_usuario} con un reloj de bolsillo.",
            "por intentar venderle un puente a {otro_usuario}.",
            "por intentar convencer a {otro_usuario} de que es un extraterrestre.",
            "por intentar cambiarle el color de pelo a {otro_usuario} con un plumón.",
            "por intentar venderle un terreno en la Luna a {otro_usuario}.",
            "por intentar convencer a {otro_usuario} de que es invisible.",
            "por intentar robarle el almuerzo a {otro_usuario}."
        ]

    @commands.command(name="arresto", aliases=["wk.arresto"])
    async def arrestar(self, ctx, miembro: discord.Member = None):
        """Arresta a un usuario por un motivo gracioso."""

        await ctx.message.delete()  # Elimina el mensaje del autor

        if miembro is None:
            miembro = ctx.author  # Si no se menciona a nadie, el arrestado es el autor

        # Elige aleatoriamente si el motivo involucra a otro usuario o no
        if random.random() < 0.5 and len(ctx.guild.members) > 1:  # 50% de probabilidad de involucrar a otro usuario
            # Motivo que involucra a otro usuario
            otro_miembro = random.choice([m for m in ctx.guild.members if m != miembro])
            motivo = random.choice(self.motivos_arresto_con_otro).format(otro_usuario=otro_miembro.mention)
        else:
            # Motivo en solitario
            motivo = random.choice(self.motivos_arresto_solo)

        embed = discord.Embed(
            title="🚨 ¡ARRESTO! 🚨",
            description=f"{miembro.mention} ha sido arrestado {motivo}",
            color=discord.Color.red()
        )
        embed.set_image(url="https://media.giphy.com/media/MHZGn06IC4qC8NW15b/giphy.gif?cid=ecf05e47ebp0o5yp5wld9jvd4btgzazmddjfde9mf62cejma&ep=v1_gifs_search&rid=giphy.gif&ct=g")  # GIF de arresto
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Arresto(bot))
    print("Cog Arresto cargado.")