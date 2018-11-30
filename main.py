import discord
import os
import random
from keep_living import keep_alive

client = discord.Client()

insults = ["You have less class than my first project in computational thinking.","How can you live with yourself knowing that you made your mother take care of you?","Your personality is worse than a piece of soggy toast that's been left in a pile of cow feces.","I would say that I hate you but how can I hate someone who makes me look like a model whenever they're around.","I bet you like pineapple on your pizza.","Your voice reminds me of a gerbil being strangled by its 4 year old owner who doesn't know any better. I don't blame the kid.","You flat earther.","I'm only a bot but I feel more compassion than you ever have.","I have more eyes than the numbers in your IQ."]

@client.event
async def on_ready():
  print("I've joined the chat.")
  print(client.user)

@client.event
async def on_message(message):
  if message.author != client.user:
    await client.send_message(message.channel, random.choice(insults))

keep_alive()
token = os.environ.get("discord_bot_secret")
client.run(token)