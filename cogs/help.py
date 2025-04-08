import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["wk.help"])
    async def help(self, ctx):
        """Muestra la lista de comandos disponibles y sus descripciones."""
        # Eliminar el mensaje del usuario
        await ctx.message.delete()

        embed = discord.Embed(
            title="📜 **Lista de Comandos de WekiBot**",
            description=(
                "¡Bienvenido a la guía de comandos! Aquí encontrarás todo lo que puedes hacer con este bot. "
                "Usa los comandos como se indica para disfrutar de todas las funciones. 🌟\n\n"
                "```fix\nPrefijo: wk.\n```"
            ),
            color=discord.Color.purple()
        )

        # Comandos Divertidos (en línea)
        comandos_divertidos = (
            "`gay [@usuario]` - 🌈 | "
            "`feo [@usuario]` - 🤡 | "
            "`borracho [@usuario]` - 🍻 | "
            "`muerte [@usuario]` - 💀 | "
            "`pelea [@usuario1] [@usuario2]` - 🥊 | "
            "`banana [@usuario]` - 🍌 | "
            "`ship [@usuario]` - 💖 | "
            "`chiste` - 😂 | "
            "`besar [@usuario]` - 💋"  # Agregado el comando besar
        )
        embed.add_field(name="🎭 **Comandos Divertidos**", value=comandos_divertidos, inline=False)

        # Comandos de Información (en línea)
        comandos_info = (
            "`perfil [@usuario]` - 🧑‍💻 | "
            "`help` - ❓"
        )
        embed.add_field(name="📋 **Comandos de Información**", value=comandos_info, inline=False)

        # Comandos de Mensajes (en línea)
        comandos_mensajes = (
            "`anonimo <mensaje>` - 📩"
        )
        embed.add_field(name="📩 **Comandos de Mensajes**", value=comandos_mensajes, inline=False)

        # Pie de página y diseño adicional
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else "")
        embed.set_footer(
            text=f"Solicitado por {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url
        )
        embed.set_image(url="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif")  # Imagen decorativa

        # Enviar el embed
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))