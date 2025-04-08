import discord
from discord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE")
BESOS_COLLECTION_NAME = "besos"

class TopBesos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DATABASE_NAME]
        self.besos_collection = self.db[BESOS_COLLECTION_NAME]

    def cog_unload(self):
        self.client.close()

    @commands.command(name="besos", aliases=["wk.besos"])
    async def topbesos(self, ctx):
        """Muestra el top 5 de parejas que más se han besado."""

        # Eliminar el mensaje del comando
        await ctx.message.delete()

        # Obtener las 5 parejas con más besos
        top_parejas = self.besos_collection.find().sort("besos", -1).limit(5)

        embed = discord.Embed(
            title="🏆 Top 5 Parejas Más Besuconas 🏆",
            color=discord.Color.red()
        )

        i = 1
        for pareja in top_parejas:
            usuario1_id = pareja["usuario1"]
            usuario2_id = pareja["usuario2"]
            besos = pareja["besos"]

            # Obtener los objetos User de Discord a partir de los IDs
            usuario1 = self.bot.get_user(usuario1_id)
            usuario2 = self.bot.get_user(usuario2_id)

            # Verificar si los usuarios existen en el servidor
            if usuario1 and usuario2:
                embed.add_field(
                    name=f"#{i}:",
                    value=f"{usuario1.mention} ❤️ {usuario2.mention} - {besos} besos",
                    inline=False
                )
                i += 1
            else:
                embed.add_field(
                    name=f"#{i}:",
                    value=f"Usuario no encontrado ❤️ Usuario no encontrado - {besos} besos",
                    inline=False
                )
                i += 1

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(TopBesos(bot))
    print("Cog TopBesos cargado.")