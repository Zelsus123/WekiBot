import discord
from discord.ext import commands
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

# Cargar las variables de entorno desde el archivo .env
MONGODB_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
ID_NO_VERIFICADO_ROL = int(os.getenv("ID_NO_VERIFICADO_ROL"))
ID_CANAL_BIENVENIDA = int(os.getenv("ID_CANAL_BIENVENIDA"))
ID_CANAL_VERIFICACION = int(os.getenv("ID_CANAL_VERIFICACION"))

class Verificacion(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        self.rol_no_verificado_id = ID_NO_VERIFICADO_ROL
        self.canal_bienvenida_id = ID_CANAL_BIENVENIDA
        self.canal_verificacion_id = ID_CANAL_VERIFICACION
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DATABASE_NAME]
        self.verificados_collection = self.db[COLLECTION_NAME]
        
    def cog_unload(self):
        self.client.close()
        
    @commands.Cog.listener()
    async def on_ready(self):
        # Enviar un mensaje al canal de verificación al iniciar el bot
        canal_verificacion = self.bot.get_channel(self.canal_verificacion_id)
        if canal_verificacion:
            await canal_verificacion.send(
                "**¡Bienvenido al sistema de verificación!**\n\n"
                "Por favor, verifica tu cuenta para acceder a todas las funciones del servidor.\n"
                "Usa el siguiente formato para verificarte:\n"
                "`<SK_USER> <DD/MM/YYYY> <COLOR_HEX>`\n\n"
                "Por ejemplo: `Weki123 06/04/2000 #FF5733`\n\n"
                "El color debe ser un código hexadecimal válido (por ejemplo, `#FF5733`).\n"
                "Esto nos ayuda a mantener un ambiente seguro y organizado. ¡Gracias por tu cooperación! 😊"
            )
        else:
            print(f"El canal de verificación no se encontró: {self.canal_verificacion_id}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        rol_no_verificado = member.guild.get_role(self.rol_no_verificado_id)
        canal_bienvenida = self.bot.get_channel(self.canal_bienvenida_id)
        canal_verificacion = self.bot.get_channel(self.canal_verificacion_id)
        
        if rol_no_verificado:
            await member.add_roles(rol_no_verificado)
            if canal_bienvenida:
                await canal_bienvenida.send(f"¡Bienvenido/a {member.mention}! Por favor verifica tu cuenta en {canal_verificacion.mention}.")
            else:
                print(f"El canal de bienvenida no se encontró: {self.canal_bienvenida_id}")
        else:
            print(f"El rol de no verificado no se encontró: {self.rol_no_verificado_id}")
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id == self.canal_verificacion_id:
            partes = message.content.split()
            if len(partes) == 3:
                usuario_sk = partes[0]
                fecha_nacimiento_str = partes[1]
                color_hex = partes[2]

                # Validar el formato del color hexadecimal
                if not color_hex.startswith("#") or len(color_hex) != 7:
                    await message.channel.send(f"{message.author.mention} El color debe ser un código hexadecimal válido (por ejemplo, `#FF5733`).")
                    return

                try:
                    # Convertir el color hexadecimal a un entero
                    color = discord.Color(int(color_hex[1:], 16))
                except ValueError:
                    await message.channel.send(f"{message.author.mention} El color proporcionado no es válido.")
                    return

                try:
                    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
                    await message.delete()
                    rol_no_verificado = message.guild.get_role(self.rol_no_verificado_id)
                    
                    if rol_no_verificado:
                        await message.author.remove_roles(rol_no_verificado)
                        
                        # Crear un rol con el nombre de usuario de SK y asignarlo
                        try: 
                            new_role = await message.guild.create_role(name=usuario_sk, color=color)
                            await message.author.add_roles(new_role)
                            
                            # Cambiar el apodo del usuario
                            try:
                                await message.author.edit(nick=usuario_sk)
                                await message.author.send(f"¡Has sido verificado! Tu rol es: {usuario_sk}, tu apodo ha sido actualizado y tu color favorito ha sido aplicado.")
                            except discord.Forbidden:
                                await message.author.send("No tengo permiso para cambiar tu apodo.")
                            except discord.HTTPException as e:
                                await message.author.send(f"No se pudo cambiar el apodo: {e}")
                                print(f"No se pudo cambiar el apodo: {e}")
                        except discord.Forbidden:
                            await message.author.send("No tengo permiso para crear roles.")
                        except discord.HTTPException as e:
                            await message.author.send(f"No se pudo crear el rol: {e}")
                            print(f"No se pudo crear el rol: {e}")
                            
                        # Guardar la información en la db
                        verificadoData = {
                            "sk_user": usuario_sk,
                            "birthday": fecha_nacimiento,
                            "color": color_hex,
                            "verification_time": datetime.utcnow(),
                        }
                        self.verificados_collection.insert_one(verificadoData)
                        print(f"Usuario verificado: {usuario_sk}, Fecha de nacimiento: {fecha_nacimiento}, Color: {color_hex}")
                    else:
                        print(f"El rol de no verificado no se encontró: {self.rol_no_verificado_id}")
                except ValueError:
                    await message.channel.send(f"{message.author.mention} Formato de fecha inválido. Usa el formato DD/MM/YYYY.")
            else: 
                await message.channel.send("Formato inválido. Usa el formato: `<SK_USER> <DD/MM/YYYY> <COLOR_HEX>`")

async def setup(bot):
    await bot.add_cog(Verificacion(bot))
    print("Cog Verificacion cargada.")
