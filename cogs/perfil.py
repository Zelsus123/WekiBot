import discord
from discord.ext import commands
from datetime import datetime

class Perfil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="perfil", aliases=["wk.perfil"])
    async def perfil(self, ctx, miembro: discord.Member = None):
        """Muestra el perfil de un usuario."""
        await ctx.message.delete() 
        miembro = miembro or ctx.author

        # Obtener la colección de la base de datos desde el cog de verificación
        verificacion_cog = self.bot.get_cog("Verificacion")
        if not verificacion_cog:
            await ctx.send("❌ El sistema de verificación no está disponible.")
            return

        collection = verificacion_cog.verificados_collection

        # Buscar al usuario en la base de datos
        user_data = collection.find_one({"sk_user": miembro.display_name})
        if not user_data:
            await ctx.send(f"❌ No se encontró información de perfil para {miembro.mention}.")
            return

        # Extraer datos del usuario
        sk_user = user_data.get("sk_user", "Desconocido")
        birthday = user_data.get("birthday")
        verification_time = user_data.get("verification_time")

        # Calcular tiempo hasta el cumpleaños
        today = datetime.utcnow()
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        days_until_birthday = (next_birthday - today).days

        # Crear el mensaje de cumpleaños
        if days_until_birthday == 0:
            birthday_message = "🎉 ¡Hoy es su cumpleaños! ¡Felicidades! 🎂"
        else:
            birthday_message = f"🎂 Faltan {days_until_birthday} días para su cumpleaños."

        # Crear el embed para el perfil
        embed = discord.Embed(
            title=f"Perfil de {miembro.display_name}",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=miembro.avatar.url if miembro.avatar else ctx.guild.icon.url)
        embed.add_field(name="Nombre en SK", value=sk_user, inline=False)
        embed.add_field(name="Fecha de nacimiento", value=birthday.strftime("%d/%m/%Y"), inline=False)
        embed.add_field(name="Tiempo hasta el cumpleaños", value=birthday_message, inline=False)
        embed.add_field(name="Fecha de verificación", value=verification_time.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.set_footer(text=f"Solicitado por {ctx.author.display_name}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Perfil(bot))
