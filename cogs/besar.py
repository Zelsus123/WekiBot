import discord
from discord.ext import commands
from pymongo import MongoClient
import os
import random
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE")
BESOS_COLLECTION_NAME = "besos"
ACEPTAR_EMOJI = "✅"
RECHAZAR_EMOJI = "❌"
GIFS_ACEPTAR_COLLECTION = "besosAceptadosgifs"  # Nueva colección para gifs de aceptar
GIFS_RECHAZAR_COLLECTION = "besosRechazadosgifs"  # Nueva colección para gifs de rechazar

class Besar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DATABASE_NAME]
        self.besos_collection = self.db[BESOS_COLLECTION_NAME]
        self.gifs_aceptar_collection = self.db[GIFS_ACEPTAR_COLLECTION]
        self.gifs_rechazar_collection = self.db[GIFS_RECHAZAR_COLLECTION]
        self.gifs_aceptar = []  # Inicializar lista vacía
        self.gifs_rechazar = []  # Inicializar lista vacía
        self.cargar_gifs()  # Cargar los gifs desde la base de datos

    def cog_unload(self):
        self.client.close()

    def cargar_gifs(self):
        """Carga los GIFs desde la base de datos."""
        self.gifs_aceptar = [gif["url"] for gif in self.gifs_aceptar_collection.find()]
        self.gifs_rechazar = [gif["url"] for gif in self.gifs_rechazar_collection.find()]

    @commands.command(name="besar", aliases=["wk.besar"])
    async def besar(self, ctx, miembro: discord.Member):
        """Pide un beso a otro usuario."""
        if ctx.author == miembro:
            await ctx.send("¡No puedes besarte a ti mismo!")
            return

        # Eliminar el mensaje del comando
        await ctx.message.delete()

        embed = discord.Embed(
            title="💋 ¡Petición de Beso! 💋",
            description=f"{ctx.author.mention} te está pidiendo un beso, {miembro.mention}. ¿Aceptas?",
            color=discord.Color.pink()
        )

        mensaje = await ctx.send(miembro.mention, embed=embed)
        await mensaje.add_reaction(ACEPTAR_EMOJI)
        await mensaje.add_reaction(RECHAZAR_EMOJI)

        def check(reaction, user):
            return user == miembro and reaction.message.id == mensaje.id and str(reaction.emoji) in [ACEPTAR_EMOJI, RECHAZAR_EMOJI]

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == ACEPTAR_EMOJI:
                # Beso Aceptado
                if not self.gifs_aceptar:
                    await ctx.send("No hay GIFs de aceptación disponibles.")
                    return
                gif_url = random.choice(self.gifs_aceptar)
                embed = discord.Embed(
                    title="💖 ¡Beso Aceptado! 💖",
                    description=f"{ctx.author.mention} y {miembro.mention} se han besado.",
                    color=discord.Color.red()
                )
                embed.set_image(url=gif_url)
                await mensaje.clear_reactions()
                await mensaje.edit(content="", embed=embed)

                # Actualizar la base de datos
                self.actualizar_base_de_datos(ctx.author.id, miembro.id)

            elif str(reaction.emoji) == RECHAZAR_EMOJI:
                # Beso Rechazado
                if not self.gifs_rechazar:
                    await ctx.send("No hay GIFs de rechazo disponibles.")
                    return
                gif_url = random.choice(self.gifs_rechazar)
                embed = discord.Embed(
                    title="💔 ¡Beso Rechazado! 💔",
                    description=f"{miembro.mention} ha rechazado el beso de {ctx.author.mention}.",
                    color=discord.Color.blue()
                )
                embed.set_image(url=gif_url)
                await mensaje.clear_reactions()
                await mensaje.edit(content="", embed=embed)

        except TimeoutError:
            await mensaje.clear_reactions()
            await mensaje.edit(content="¡La petición de beso ha expirado!", embed=None)

    def actualizar_base_de_datos(self, usuario1_id, usuario2_id):
        """Actualiza la base de datos con la información del beso."""
        # Crear un identificador único combinando los IDs de los usuarios (ordenados para evitar duplicados)
        id_pareja = tuple(sorted((usuario1_id, usuario2_id)))
        
        # Buscar si ya existe la pareja en la base de datos
        pareja = self.besos_collection.find_one({"_id": id_pareja})
        
        if pareja:
            # Si existe, incrementar el contador de besos
            self.besos_collection.update_one({"_id": id_pareja}, {"$inc": {"besos": 1}})
            print(f"Beso registrado entre {usuario1_id} y {usuario2_id}. Total besos: {pareja['besos'] + 1}")
        else:
            # Si no existe, crear una nueva entrada
            nueva_pareja = {
                "_id": id_pareja,
                "usuario1": usuario1_id,
                "usuario2": usuario2_id,
                "besos": 1
            }
            self.besos_collection.insert_one(nueva_pareja)
            print(f"Nueva pareja registrada: {usuario1_id} y {usuario2_id}. Besos: 1")

    @commands.Cog.listener()
    async def on_message(self, message):
        """Escucha los mensajes en los canales de GIFs y los guarda en la base de datos."""
        # Reemplaza 'ID_CANAL_ACEPTAR' y 'ID_CANAL_RECHAZAR' con los IDs de tus canales
        ID_CANAL_ACEPTAR = 1358998842170671144  # Reemplaza con el ID del canal de GIFs de aceptar
        ID_CANAL_RECHAZAR = 1358998899016208585  # Reemplaza con el ID del canal de GIFs de rechazar

        if message.channel.id == ID_CANAL_ACEPTAR:
            for attachment in message.attachments:
                if attachment.url.endswith((".gif", ".png", ".jpg", ".jpeg")):
                    # Guardar el GIF en la base de datos de GIFs de aceptar
                    await self.gifs_aceptar_collection.insert_one({"url": attachment.url})
                    self.gifs_aceptar.append(attachment.url)  # Actualizar la lista en memoria
                    print(f"GIF de aceptar guardado: {attachment.url}")
            if message.content.endswith((".gif", ".png", ".jpg", ".jpeg")):
                await self.gifs_aceptar_collection.insert_one({"url": message.content})
                self.gifs_aceptar.append(message.content)
                print(f"GIF de aceptar guardado: {message.content}")
            self.cargar_gifs()

        if message.channel.id == ID_CANAL_RECHAZAR:
            for attachment in message.attachments:
                if attachment.url.endswith((".gif", ".png", ".jpg", ".jpeg")):
                    # Guardar el GIF en la base de datos de GIFs de rechazar
                    await self.gifs_rechazar_collection.insert_one({"url": attachment.url})
                    self.gifs_rechazar.append(attachment.url)  # Actualizar la lista en memoria
                    print(f"GIF de rechazar guardado: {attachment.url}")
            if message.content.endswith((".gif", ".png", ".jpg", ".jpeg")):
                await self.gifs_rechazar_collection.insert_one({"url": message.content})
                self.gifs_rechazar.append(message.content)
                print(f"GIF de rechazar guardado: {message.content}")
            self.cargar_gifs()

async def setup(bot):
    await bot.add_cog(Besar(bot))
    print("Cog Besar cargado.")