import discord
from discord.ext import commands
import random

class Muerte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="muerte", aliases=["wk.muerte"])
    async def muerte(self, ctx, miembro: discord.Member = None):
        """Genera una manera graciosa de morir para un usuario."""
        await ctx.message.delete() 
        miembro = miembro or ctx.author

        # Obtener una lista de miembros aleatorios (excluyendo bots)
        miembros = [m for m in ctx.guild.members if not m.bot and m != miembro]
        otro_miembro = random.choice(miembros) if miembros else None

        # Lista de maneras graciosas de morir
        maneras = [
            "Se tropezó con una piedra imaginaria y cayó al vacío.",
            "Intentó lamer un enchufe para ver si sabía a electricidad.",
            "Se ahogó comiendo sopa con tenedor.",
            "Murió de risa viendo memes de gatos.",
            "Se quedó atrapado en una máquina expendedora intentando sacar un snack.",
            "Fue derrotado en combate por un pato muy agresivo.",
            "Se resbaló con una cáscara de plátano como en las caricaturas.",
            "Intentó pelear con su reflejo en el espejo y perdió.",
            "Se quedó atrapado en un ascensor con música de ascensor... para siempre.",
            "Murió intentando abrir un frasco de pepinillos.",
            "Fue aplastado por una pila de libros que nunca leyó.",
            "Se quedó dormido en una cama de clavos... literalmente.",
            "Intentó atrapar un rayo con un paraguas.",
            "Se ahogó en una piscina inflable para niños.",
            "Fue abducido por aliens y nunca regresó.",
            "Se perdió en el supermercado y nunca encontró la salida.",
            "Murió de vergüenza al enviar un mensaje al grupo equivocado.",
            "Se cayó de la cama y rodó hasta el fin del mundo.",
            "Intentó correr más rápido que un tren... y perdió.",
            "Fue derrotado por un ventilador de techo en modo turbo.",
            "Se quedó atrapado en un torbellino de confeti.",
            "Murió intentando bailar breakdance sin saber cómo.",
            "Se quedó atrapado en una montaña rusa que nunca paró.",
            "Fue aplastado por una pila de ropa sucia.",
            "Intentó comer 100 tacos en una sola sentada.",
            "Se perdió en un laberinto de espejos y nunca salió.",
            "Fue derrotado por un ejército de hormigas muy organizadas.",
            "Se quedó atrapado en un sillón reclinable y nunca pudo salir.",
            "Murió intentando hacer un reto viral de internet.",
            "Se resbaló con jabón en la ducha y terminó en otro universo.",
            "Fue aplastado por un globo gigante en un desfile.",
            "Se quedó atrapado en un videojuego y nunca volvió al mundo real.",
            f"Fue empujado accidentalmente por {otro_miembro.mention} mientras intentaba tomarse una selfie." if otro_miembro else "Murió intentando tomarse una selfie.",
            f"Se perdió en el bosque porque {otro_miembro.mention} le dio malas indicaciones." if otro_miembro else "Se perdió en el bosque y nunca regresó.",
            f"Intentó robarle comida a {otro_miembro.mention} y fue derrotado en combate." if otro_miembro else "Intentó robar comida y fue derrotado.",
            f"Fue aplastado por un piano que {otro_miembro.mention} dejó caer desde un edificio." if otro_miembro else "Fue aplastado por un piano que cayó del cielo.",
            f"Murió de risa después de escuchar un chiste malo de {otro_miembro.mention}." if otro_miembro else "Murió de risa después de escuchar un chiste muy malo.",
            f"Se quedó atrapado en una pelea de almohadas con {otro_miembro.mention} y nunca salió con vida." if otro_miembro else "Murió en una épica pelea de almohadas."
        ]

        # Elegir una manera aleatoria
        manera = random.choice(maneras)

        # Enviar el resultado
        await ctx.send(f"💀 {miembro.mention} murió de la siguiente manera: **{manera}**")

async def setup(bot):
    await bot.add_cog(Muerte(bot))