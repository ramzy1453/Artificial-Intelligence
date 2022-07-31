
from discord import VoiceChannel

def get_channel_by_name(VoiceChannels, ChannelName) : 
    for channel in  VoiceChannels : 
        if channel.name == ChannelName : 
            return channel
    return None

async def send_private(User, VoiceChannel, Guild) : 
    dm = await User.create_dm()
    await dm.send(f"Hi {User.mention} unfortunately you did not have join the meeting of {VoiceChannel} in {Guild} today")

def write_in_file(file, p) : 
    if p < 1 and p >= 0.7 : 
        file.write("nTres bien, 7adro nas bzaf sa fait plaisir !")
    elif p < 0.7 and p >= 0.4 : 
        file.write("\nca va bien intik kayen comme meme li 7adro c'est tres bien")
    elif p == 0 : 
        file.write("\n7ta wa7ed maja RIP HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    elif p == 1 : 
        file.write("\nAh non, ge3 ram 7adro il parait que nta ma7boub ljamahir hhh")
    else : 
        file.write("\nMafhmtch 3lach makach ghachi t9oulchi may7boukch XD")

