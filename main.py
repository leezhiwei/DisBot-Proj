# Changelog:
# 

# Comments:
# Overall imports seem all good
# Code in on_message is rather unreadable, and the logic might have bugs
# I don't have time to do it rn so this should be good enough for now
# I might rework all of it when I have the time

import discord
import random
import os
import time
import variables
import functions #Don't need to import functions twice, but since you need this for the global vars...
# You can import multiple stuff from one import statement
from functions import sen_gen, start_time, teamfind, add_pts, riddle_gen, riddle, typing

from keep_alive import keep_alive

key = random.randint(1000000000, 9999999999) # Uhhhhhh don't use random for keys
key2 = random.randint(1000000000, 9999999999) # Either use the builtin secrets module or uuid
print("The key for mystery box is {}".format(key))
print("The key for spot the difference is {}".format(key2))



sengen()

client = discord.Client()
keep_alive(key,key2)

@client.event
async def on_ready():
    print('Logged on as {}'.format(client.user))


@client.event
async def on_message(msg):
    i = 0
    AlreadyIn = False
    if msg.author == client.user:
        return
    else:
        author = msg.author
        if msg.content.startswith('/'):
            if 'choose' in msg.content:
                for roletemp in msg.author.roles: # Use for-loop
                    if 'Team' in str(roletemp):
                        AlreadyIn = True
                if AlreadyIn == True:
                    await msg.channel.send('Error: You are already in a Team')
                else:
                    if msg.content[-1].isnumeric() == True:
                        role = discord.utils.get(msg.author.guild.roles,
                                                 name="Team {}".format(
                                                     msg.content[-1]))
                        await author.add_roles(role)
                    else:
                        await msg.channel.send("Error: {} inputted {}".format(
                            msg.author, msg.content))
            elif 'start' in msg.content:
                if msg.channel.id == variables.channelids[0]:
                    await msg.channel.send(riddlegen())
                    riddle(msg.author)
                elif msg.channel.id == variables.channelids[1]:
                    await msg.channel.send(file=discord.File('foodclub.jpg'))
                elif msg.channel.id == variables.channelids[2]:
                    await msg.channel.send('Type the following sentence in 30 Seconds:')
                    await msg.channel.send("Typing challenge : {}".format(functions.sentence))
                    typing(msg.author)
                    start_time()
                elif msg.channel.id == variables.channelids[3]:
                    await msg.channel.send("Mystery Box is not ready yet.")
                else:
                    await msg.channel.send(
                        'Sorry, {} you are in the wrong channel. Please head to station channels to use this command.'
                        .format(msg.author))
        elif functions.sentence == msg.content and msg.channel.id == variables.channelids[2] and msg.author == functions.typingauthor:
            endtime = time.time()
            dur = endtime - functions.starttime
            WPS = len(functions.senlist) / dur
            await msg.channel.send(
                "WPS: {:.2f} Words per second  \nTime taken: {:.2f}s".format(
                    WPS, dur))
            await msg.channel.send("Team {} :".format(teamfind(msg.author.roles))+ str(addpts(teamfind(msg.author.roles),20)))
            await msg.channel.send("Head to #station-4")
            sengen()
        elif variables.riddlelist[functions.randnum][1] == msg.content and msg.channel.id == variables.channelids[0] and msg.author == functions.riddleauthor:
            await msg.channel.send("Correct for riddles")
            await msg.channel.send("Team {} :".format(teamfind(msg.author.roles))+str(addpts(teamfind(msg.author.roles),20)))
            await msg.channel.send("Head to #station-2")

        elif msg.channel.id == variables.channelids[0] and variables.riddlelist[
                functions.randnum][1] != msg.content:
            await msg.channel.send("Incorrect.")
        elif str(key2) == msg.content and msg.channel.id == variables.channelids[1]: # No need to be accross multiple lines
            await msg.channel.send("Correct for spot the difference")
            await msg.channel.send("Team {} :".format(teamfind(msg.author.roles))+str(addpts(teamfind(msg.author.roles),20)))
            await msg.channel.send("Head to #station-3")
        elif str(key) == msg.content and msg.channel.id == variables.channelids[3]: # same as above
            await msg.channel.send("Correct for mystery box")
            await msg.channel.send("Team {} :".format(teamfind(msg.author.roles))+str(addpts(teamfind(msg.author.roles),20)))


client.run(os.getenv('TOKEN'))
