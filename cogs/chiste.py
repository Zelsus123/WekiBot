import discord
from discord.ext import commands
import random

class Chistes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chiste", aliases=["wk.chiste"])
    async def chiste(self, ctx):
        """Cuenta un chiste aleatorio."""
        await ctx.message.delete()

        # Lista de chistes
        chistes = [
            "¿Por qué los pájaros vuelan hacia el sur en invierno? ¡Porque es demasiado lejos para caminar!",
            "¿Qué le dice un semáforo a otro? ¡No me mires, me estoy cambiando!",
            "¿Por qué los peces viven en el agua salada? ¡Porque la pimienta los hace estornudar!",
            "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
            "¿Cuál es el pez más presumido? El pez-tardo.",
            "¿Qué le dijo un árbol a otro? ¡Nos dejaron plantados!",
            "¿Por qué los fantasmas son malos mintiendo? ¡Porque se les ve a través!",
            "¿Qué hace un pez en el cine? ¡Ver una película de mer-maid!",
            "¿Qué hace una vaca en la discoteca? ¡Muuuucha fiesta!",
            "¿Qué le dice un jaguar a otro jaguar? Jaguar you?",
            "¿Qué hace un pato en una ferretería? ¡Está buscando tuercas!",
            "¿Por qué los esqueletos no van a fiestas? ¡Porque no tienen cuerpo!",
            "¿Qué hace un tomate en el banco? ¡Está ahorrando para la ensalada!",
            "¿Qué le dice un 0 a un 8? ¡Qué bonito cinturón!",
            "¿Qué hace una gallina meditando? ¡Está incubando una idea!",
            "¿Qué hace una impresora en la cárcel? ¡Está sacando copias!",
            "¿Qué hace un mudo bailando? ¡Mímica!",
            "¿Qué hace un perro con un taladro? ¡Taladrando!",
            "¿Qué hace un pez con una bufanda? ¡Nada!",
            "¿Qué hace un calcetín en un banco? ¡Esperando un préstamo!",
            "¿Cuál es el colmo de un jardinero? Que le dejen plantado.",
            "¿Qué hace un vampiro en un huerto? Esperando la noche para sacar-nabos.",
            "¿Qué le dice un pato a otro pato? Estamos empatados.",
            "¿Qué hace una oveja jugando al fútbol? Hace beeeeenales.",
            "¿Qué le dice un gusano a otro gusano? Me voy a dar la vuelta a la manzana.",
            "¿Qué le dice un semáforo a una bicicleta? No me mires, que me estoy cambiando.",
            "¿Qué le dice un plátano a otro plátano? No te separes de la manada.",
            "¿Qué le dice un uno a un diez? Para ser como yo, tienes que ser sincero.",
            "¿Qué le dice un jardinero a una flor? ¡Qué planta tienes!",
            "¿Qué le dice un enano a una enana? ¡Qué poco me conoces!",
            "¿Qué le dice un cable a otro cable? ¡Estamos enrollados!",
            "¿Qué le dice un pez a otro pez? ¡Nada!",
            "¿Qué le dice un libro a otro libro? ¡Tenemos la misma historia!",
            "¿Qué le dice un ojo a otro ojo? ¡Algo huele mal entre nosotros!",
            "¿Qué le dice un zapato a otro zapato? ¡Qué vida más suela!",
            "¿Qué le dice un semáforo a otro? ¡No me mires, me estoy cambiando!",
            "¿Qué le dice un plátano a otro plátano? ¡No te separes de la manada!",
            "¿Qué le dice un uno a un diez? ¡Para ser como yo, tienes que ser sincero!",
            "¿Qué le dice un jardinero a una flor? ¡Qué planta tienes!",
            "¿Qué le dice un enano a una enana? ¡Qué poco me conoces!",
            "¿Qué le dice un cable a otro cable? ¡Estamos enrollados!",
            "¿Qué le dice un pez a otro pez? ¡Nada!",
            "¿Qué le dice un libro a otro libro? ¡Tenemos la misma historia!",
            "¿Qué le dice un ojo a otro ojo? ¡Algo huele mal entre nosotros!",
            "¿Qué le dice un zapato a otro zapato? ¡Qué vida más suela!",
            "¿Por qué los buzos se tiran de espaldas al agua? ¡Porque si se tiran de frente, se caen dentro de la barca!",
            "¿Qué hace un perro cuando tiene fiebre? ¡Tiene una temperatura de perro!",
            "¿Qué le dice un pato a otro pato? ¡Tenemos una cita en el parque!",
            "¿Qué le dice un semáforo a otro? ¡No me mires, me estoy cambiando!",
            "¿Qué le dice un plátano a otro plátano? ¡No te separes de la manada!",
            "¿Qué le dice un uno a un diez? ¡Para ser como yo, tienes que ser sincero!",
            "¿Qué le dice un jardinero a una flor? ¡Qué planta tienes!",
            "¿Qué le dice un enano a una enana? ¡Qué poco me conoces!",
            "¿Qué le dice un cable a otro cable? ¡Estamos enrollados!",
            "¿Qué le dice un pez a otro pez? ¡Nada!",
            "¿Qué le dice un libro a otro libro? ¡Tenemos la misma historia!",
            "¿Qué le dice un ojo a otro ojo? ¡Algo huele mal entre nosotros!",
            "¿Qué le dice un zapato a otro zapato? ¡Qué vida más suela!",
            "¿Por qué los buzos se tiran de espaldas al agua? ¡Porque si se tiran de frente, se caen dentro de la barca!",
            "¿Qué hace un perro cuando tiene fiebre? ¡Tiene una temperatura de perro!",
            "¿Qué le dice un pato a otro pato? ¡Tenemos una cita en el parque!",
            "¿Por qué los programadores prefieren el modo oscuro? Porque la luz atrae a los bugs.",
            "¿Qué hace un pez en el gimnasio? ¡Está haciendo pesas!",
            "¿Por qué los fantasmas son tan malos mintiendo? Porque se les ve a través.",
            "¿Qué le dice un átomo a otro átomo? ¡Te estoy vigilando!",
            "¿Por qué los esqueletos no van a fiestas? Porque no tienen cuerpo para bailar.",
            "¿Qué hace una impresora en la cárcel? Está sacando copias.",
            "¿Por qué los matemáticos son tan buenos en la cama? Porque saben cómo hacer que los números cuenten.",
            "¿Por qué los divorcios son tan caros? Porque valen lo que pesan.",
            "¿Por qué los caníbales no comen payasos? Porque saben raro.",
            "¿Por qué los vampiros necesitan abogados? Porque siempre están chupando sangre.",
            "¿Por qué los cementerios tienen muros tan altos? Porque la gente se muere por entrar.",
            "¿Por qué los nazis eran tan malos jugando al golf? Porque siempre querían un hoyo en uno.",
            "¿Por qué los niños autistas no pueden jugar al escondite? Porque siempre los encuentran.",
            "¿Por qué los bebés no pueden jugar al póker? Porque siempre tienen una mano ganadora.",
            "¿Por qué los judíos tienen la nariz tan grande? Porque el aire es gratis.",
        ]

        # Elegir un chiste aleatorio
        chiste = random.choice(chistes)

        # Enviar el chiste en un embed
        embed = discord.Embed(
            title="😂 ¡Aquí tienes un chiste! 😂",
            description=chiste,
            color=discord.Color.green()
        )
        embed.set_footer(text="¡Espero que te haya hecho reír! 😄")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Chistes(bot))