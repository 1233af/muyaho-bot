import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        for channel in guild.channels:
            try:
                await channel.send("저희가 많이 보죠")
            except:
                print(f"maybe {guild.name} - {channel.name} is not a text channel")

@client.event
async def on_message(message):
    if '무야호' in message.content or '무한도전 혹시 보신적이' in message.content or '선생님 보셨습니까' in message.content or '액션이 어떻게 되는지 아세요' in message.content or '무한~' in message.content:
        voiceChannel = discord.utils.get(message.guild.voice_channels, name='일반')

        try:
            await voiceChannel.connect()
        except:
            pass

        voice = discord.utils.get(client.voice_clients, guild=message.guild)

        voice.play(discord.FFmpegPCMAudio("muyaho.mp3"))



client.run(os.environ['bot-token'])