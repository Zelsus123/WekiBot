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
            "Murió por aplastamiento accidental con una colección excesiva de juguetes sexuales.",
            f"Murió asfixiado por una peluca mal colocada durante un juego de roles con {otro_miembro.mention}.",
            "Murió por un resbalón fatal en un charco de lubricante de sabor exótico.",
            "Murió de un paro cardíaco causado por una electrocución leve de un vibrador defectuoso en la ducha.",
            f"Murió tras intentar impresionar a {otro_miembro.mention} con una contorsión sexual y quedarse atascado en el sofá hasta morir de vergüenza.",
            f"Murió al resbalar con el lubricante que {otro_miembro.mention} dejó en el suelo mientras huía desnudo/a del cartero y morir de hipotermia.",
            f"Murió tras confundir la crema depilatoria de {otro_miembro.mention} con lubricante y su intento de 'depilación íntima extrema' resultar fatal.",
            f"Murió al intentar usar la lencería de {otro_miembro.mention} como paracaídas al caer de la cama y, bueno, no funcionar.",
            f"Murió de un ataque de risa tan fuerte al ver a {otro_miembro.mention} intentar un baile sensual que su corazón simplemente dijo 'basta'.",
            f"Murió al intentar sorprender a {otro_miembro.mention} con un striptease improvisado usando solo calcetines y tropezar, golpeándose la cabeza con una lámpara de lava.",
            f"Murió electrocutado cómicamente al usar accidentalmente el vibrador de {otro_miembro.mention} para batir huevos para un desayuno 'íntimo'.",
            f"Murió tras intentar preparar una cena 'afrodisíaca' siguiendo un tutorial de YouTube de {otro_miembro.mention} y la explosión de la cocina ser inesperada.",
            f"Murió sofocado bajo el glaseado tras esconderse en un pastel gigante para sorprender a {otro_miembro.mention} en su cumpleaños 'picante'.",
            f"Murió al intentar imitar una pose sexual de una estatua griega que {otro_miembro.mention} admiraba y romperse tantas cosas que la ambulancia no llegar a tiempo.",
            f"Murió tras beber accidentalmente la 'poción del amor' que {otro_miembro.mention} había preparado (era lejía con colorante rojo).",
            f"Murió al intentar usar el cinturón de castidad de broma de {otro_miembro.mention} y la cerradura atascarse... permanentemente.",
            f"Murió electrocutado al intentar cargar su juguete sexual con el mismo cargador de su tostadora mientras tomaba un baño 'relajante'.",
            f"Murió de un susto mortal tras intentar hacerle una broma sexual a {otro_miembro.mention} con un globo con forma fálica que explotó justo en su cara.",
            f"Murió atragantado con una cereza al intentar una pose 'tonta pero sexy' que {otro_miembro.mention} le había descrito.",
            f"Murió al caer por un hueco inesperado en el suelo tras intentar usar el antifaz de encaje de {otro_miembro.mention} para vendarse los ojos.",
            f"Murió tras tener una reacción alérgica al 'aceite de pasión con aroma a unicornio' que {otro_miembro.mention} compró en una tienda dudosa.",
            f"Murió al apuñalarse accidentalmente en el pie (la infección fue terrible) tras intentar abrir una botella de champán con una espada para impresionar a {otro_miembro.mention}.",
            f"Murió tras quedarse dormido/a en una posición tan ridícula después de una noche de 'diversión' con {otro_miembro.mention} que su cuerpo simplemente se rindió.",
            f"Murió atacado/a por una ardilla territorial tras intentar usar el disfraz de 'plátano gigante sexy' que {otro_miembro.mention} había olvidado."
        ]

        # Elegir una manera aleatoria
        manera = random.choice(maneras)

        # Crear un embed para el mensaje
        embed = discord.Embed(
            title="💀 Muerte Épica 💀",
            description=f"{miembro.mention} murió de la siguiente manera:\n**{manera}**",
            color=discord.Color.red()
        )
        embed.set_footer(text="¡Qué tragedia tan graciosa!")
        embed.set_thumbnail(url="https://media.giphy.com/media/B313NwxrHpzUs/giphy.gif?cid=790b76114gg13s3aw98a6x2p72hlxduc0cgam958v2gelz9h&ep=v1_gifs_search&rid=giphy.gif&ct=g")  # Puedes cambiar esta URL por otra imagen

        # Enviar el embed
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Muerte(bot))