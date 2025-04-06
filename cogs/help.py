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

        # Categorías de comandos
        embed.add_field(
            name="🎭 **Comandos Divertidos**",
            value=(
                "`gay [@usuario]` - Calcula qué tan gay es un usuario con un porcentaje aleatorio. 🌈\n\n"
                "`feo [@usuario]` - Calcula qué tan feo es un usuario con un porcentaje aleatorio. 🤡\n\n"
                "`borracho [@usuario]` - Calcula qué tan borracho está un usuario con un porcentaje aleatorio. 🍻\n\n"
                "`muerte [@usuario]` - Genera una manera graciosa de morir para un usuario. 💀"
            ),
            inline=False
        )

        embed.add_field(
            name="📋 **Comandos de Información**",
            value=(
                "`perfil [@usuario]` - Muestra el perfil de un usuario, incluyendo su nombre en SK, cumpleaños y más. 🧑‍💻\n\n"
                "`help` - Muestra esta lista de comandos y sus descripciones. ❓"
            ),
            inline=False
        )

        embed.add_field(
            name="📩 **Comandos de Mensajes**",
            value=(
                "`anonimo <mensaje>` - Permite enviar un mensaje anónimo al canal. 📩"
            ),
            inline=False
        )

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