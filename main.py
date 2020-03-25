import discord
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(activity=discord.Game(name='tricks'))

@client.event
async def on_message(message):
    Channel=client.get_channel(627469330061328384)
    if message.author != client.user:
        if random.randint(1,7)==1:
          await message.channel.send('M'+'o'*random.randint(3,7)+'\n\n REMEMBER TO WASH YOUR HANDS OFTEN TO STOP COVID-19',tts=True)
          print ('Mooed')

token='NjI5MDU0Mjk2MTA4ODI2NjU3.XZUKzA.X7TjYEINMxyU0nijqtJmgatJ6sE'
#keepalive.start()
client.run(token)
