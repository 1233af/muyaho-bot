import discord
import requests

# url = 'https://doc-08-0g-docs.googleusercontent.com/docs/securesc/hls29morhqatimc1fnrd95d58c12jheb/rb0or1prfhektg84tqgnfjfb4c86aadj/1617198600000/13421179815168591309/13421179815168591309/1qChEstVFFUVvCoW0rqwNEwk020LXEryV?e=download&authuser=0'
# r = requests.get(url, allow_redirects=True)
# open('ffmpeg.exe', 'wb').write(r.content)

# url = 'https://doc-00-0g-docs.googleusercontent.com/docs/securesc/hls29morhqatimc1fnrd95d58c12jheb/ccq7glapj8r65eqno7j413l0r7pr73l8/1617198675000/13421179815168591309/13421179815168591309/10C-dJIf0Ktd9MWElS-eFCbCP1YfIjWFj?e=download&authuser=0'
# r = requests.get(url, allow_redirects=True)
# open('muyaho.mp3', 'wb').write(r.content)

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



client.run('ODI2NTI0MDc4NTk2MTYxNTk3.YGNuiA.IgsiU3XBpHhODRRcgRHZ521KiEk')