Token = "OTE3MTkzNDY4MDQyOTQ0NTgz.Ya1I-w.F_E-LBhy-3aWIPD-68hb0HWo5O0"



import os
import discord
from discord.ext import commands, tasks
import MyFunctions
DI = discord.Intents.default()
DI.members = True
bot = commands.Bot(command_prefix="mc ",intents=DI)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.command()
async def give(ctx, channelName : str = "") : 
    if ctx.author == bot.user or ctx.author.bot : 
        return
    if channelName == "" : 
        await ctx.channel.send("You writed nothing.")
        return
    MeetingChannel = MyFunctions.get_channel_by_name(ctx.guild.voice_channels, channelName)
    if MeetingChannel == None : 
        await ctx.channel.send("There is no voice channel with this name.")
        return
    currentlyMembers = MeetingChannel.members
    path = f"logs/absents_{channelName}_{ctx.guild.name}.txt"
    with open(path,"w") as my_file : 
        my_file.write("Voila les personne qui n'ont pas pu participe, un DM leur a ete envoye. \n\n")
        for member in ctx.guild.members : 
            if member not in currentlyMembers and not member.bot :
                my_file.write("{}#{}".format(member.name, member.discriminator))
                try:
                    await MyFunctions.send_private(member, channelName , ctx.guild.name)
                except : 
                    my_file.write(" (dm closed can't send message).")
                my_file.write("\n")
        MyFunctions.write_in_file(my_file,len(currentlyMembers)/len([m for m in ctx.guild.members if not m.bot]))
    with open(path,"rb") as my_file :
        print(my_file)
        await ctx.channel.send(file = discord.File(my_file, filename=f"absents_{channelName}_{ctx.guild.name}.txt"))
    

for f in os.listdir() : 
    print(f)

bot.run(Token)

