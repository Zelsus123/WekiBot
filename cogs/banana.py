import discord
from discord.ext import commands
import random


class Banana(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="banana", aliases=["wk.banana"])
    async def banana(self, ctx, miembro: discord.Member = None):
        """Mide el tamano de la banana de un miembro."""
        await ctx.message.delete()
        
        miembro = miembro or ctx.author
        longitud_banana = random.randint(0, 40)
        
        embed = discord.Embed(
            title=f"🍌 La banana de {miembro.display_name} mide...",
            color=discord.Color.gold()
        )
        embed.set_image(url="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmV0aG81azRzcmhnM2FwOHRucmpsenIxOTNhZjNkMDI3dmZ3eHc0eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rwmf9vbCTtnCGdOD2G/giphy.gif")  # Reemplaza con la URL de tu GIF de banana
        embed.add_field(name="Longitud:", value=f"{longitud_banana} cm", inline=False)
        
        # Comentarios graciosos según el tamaño
        if longitud_banana <= 10:
            comentario = "¡Pequeña pero matona! 😉"
        elif longitud_banana <= 20:
            comentario = "¡Tamaño promedio, nada mal! 👌"
        elif longitud_banana <= 30:
            comentario = "¡Vaya, eso es considerable! 😮"
        else:
            comentario = "¡Tremenda banana! 😳"
        
        embed.set_footer(text=comentario)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Banana(bot))