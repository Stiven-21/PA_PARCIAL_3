from controllers.validations.validations_controller import Val_url_youtube
from urllib import parse, request
from discord.ext import commands
from discord.utils import get
from config import settings
import youtube_dl
import datetime
import discord
import shutil
import sys
import os
import re

bot = commands.Bot(command_prefix="?> ", description="Este es un bot para musica")#EL PREFIX ES PARA RECONOCER LOS COMANDOS "?>"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Ingresa \'?> ayuda\' para conocer los comandos"))#EL BOT APAREZCA CON UNA ACTIVIDAD
    print('Bot corriendo')

@bot.command()
async def ayuda(ctx):
    await ctx.send('?> ayuda => Lista los comandos disponibles')
    await ctx.send('?> server => Obtiene la informacion del servidor')
    await ctx.send('?> conectar => Conecta al bot en un canal de voz')
    await ctx.send('?> desconectar => Desonecta al bot en un canal de voz')
    await ctx.send('?> play [URL DE YOUTUBE] => Reproduce el audio del la url ingresada')
    await ctx.send('?> pause => Pausa la reproduccion de audio')
    await ctx.send('?> resume => Reanuda la reproduccion de audio')
    await ctx.send('?> stop => Finaliza la reproduccion de audio')
    await ctx.send('?> mp3 [URL DE YOUTUBE] [calidad de sonido] => Envia el audio mp3 por mensaje privado')
    await ctx.send('[calidad de sonido] => 12, 32, 96, 128, 192 y 320')
    
@bot.command()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server for partial 3", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="Server create at", value=f"{ctx.guild.created_at}")#cuando fue creado el servidor de discord
    embed.add_field(name="Server id", value=f"{ctx.guild.id}")#id del servidor
    await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def conectar(ctx):
    try:
        canal = ctx.message.author.voice.channel  #extrae el canal donde esta el que ingresa el mensaje
    except:
        message = "No estas conectado a un canal de voz"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    voz = get(bot.voice_clients, guild = ctx.guild)
    try:
        if voz and voz.is_connected():    
            await voz.move_to(canal) #MUEVE ELBOT SI ESTA CONECTADO A ALGUN CANAL DE VOZ
        else:
            voz = await canal.connect() #CONECTA EL BOT AL CANAL SI NO ESTA CONECTADO
            message = "Bot conectado al canal "+str(canal)+" exitosamente!"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
            await ctx.send(embed=embed)
    except:
        message = "Problemas al conectar el bot al canal de voz "+str(canal)+" --- "+str(sys.exc_info()[0])
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
       
@bot.command(pass_context = True)
async def desconectar(ctx):
    try:
        voz = get(bot.voice_clients, guild = ctx.guild)
        await voz.disconnect()
        message = "Bot desconectado del canal exitosamente!"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    except:
        message = "El bot no esta conectado a un canal de voz"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    await ctx.send(embed=embed)
    
@bot.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voz = get(bot.voice_clients, guild=ctx.guild)
        
    try:
        if Val_url_youtube(url):
            if not voz.is_playing():
                with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(url, download=False)
                URL = info['url']
                name_cancion = info['title']
                voz.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                voz.is_playing()
                message = "Reproduciendo: "+str(name_cancion)
                embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
                await ctx.send(embed=embed)
            else:
                message = "Ya hay una reproduccion de audio ejecutandose, espere a que finalice o ingrese el comando \'?> stop\'"
                embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
                await ctx.send(embed=embed)
                return
        else:
            message = "Error: esta url no es valida o no es de youtube"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
            await ctx.send(embed=embed)
            return
    except:
        message = "Primero ejecute el comando \'?> conectar\' para conectar el bot a un canal de audio"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return

@bot.command()
async def pause(ctx):
    voz = get(bot.voice_clients, guild=ctx.guild)

    try:
        if voz.is_playing():
            voz.pause()
            message = "Reproduccion de musica pausada"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
        else:
            message = "No estas reproduciendo ninguna cancion"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    except:
        message = "Primero ejecute el comando \'?> conectar\' para conectar el bot a un canal de audio"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
@bot.command()
async def resume(ctx):
    voz = get(bot.voice_clients, guild=ctx.guild)
    try:
        if not voz.is_playing():
            voz.resume()
            if voz.is_playing():
                message = "Reproduccion de musica reanudada"
                embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
            else:
                message = "No estas reproduciendo ninguna cancion"
                embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        else:
            message = "La reproduccion de musica no ha sido pausada, ejecute el comando \'?> pause\' para pausar la reproduccion"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    except:
        message = "Primero ejecute el comando \'?> conectar\' para conectar el bot a un canal de audio"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
@bot.command()
async def stop(ctx):
    voz = get(bot.voice_clients, guild=ctx.guild)
    try:
        if voz.is_playing():
            voz.stop()
            message = "Reproduccion de musica detenida"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
        else:
            message = "No estas reproduciendo ninguna cancion"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    except:
        message = "Primero ejecute el comando \'?> conectar\' para conectar el bot a un canal de audio"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
@bot.command(pass_context = True)
async def mp3(ctx, url, calidad):
    if Val_url_youtube(url):
        if calidad=='16' or calidad=='32' or calidad=='96' or calidad=='128' or calidad=='192' or calidad=='320':
            ydl_op = {
                'format': 'bestaudio/best',
                'noplaylist': 'True',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': calidad,
                }],    
            }
            with youtube_dl.YoutubeDL(ydl_op) as ydl:
                info = ydl.extract_info(url, download=False)
                await ctx.author.send("Trabajando en proceso de descarga: "+str(info['title'])+", calidad de sonido: "+calidad+" Kbps, esto puede tardar unos segundos tenga paciencia!")
                
                new_name_mp3 = str(info['title'])+"-"+calidad+".mp3"
                if not os.path.isfile('./static/music/'+str(new_name_mp3)):
                    ydl.download([url])
                    
                    for file in os.listdir('./'):
                        if file.endswith('.mp3'):
                            print(f"Renombrar archivo: {file}")
                            os.rename(file,new_name_mp3)
                    shutil.move(new_name_mp3, './static/music/'+str(new_name_mp3))
            await ctx.author.send(file=discord.File('./static/music/'+str(new_name_mp3)))
        else:
            message = "Error: las calidades de audio permitidas son 12, 32, 96, 128, 192 y 320 Kbps"
            embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
            await ctx.send(embed=embed)
            return
    else:
        message = "Error: esta url no es valida o no es de youtube"
        embed = discord.Embed(title=f"{ctx.guild.name}", description=message, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        await ctx.send(embed=embed)
        return

#LO COMENTADO BUSCABA EN YOUTUBE Y RETORNABA EL PRIMER ENLACE DE LA BUSQUEDA
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_result = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    if not search_result:
        await ctx.send("No se encontraron resultados")
    else:
        print(search_result)
        await ctx.send('http://www.yotube.com/watch?v='+search_result[0])
    
bot.run(settings.TOKEN_DISCORD)