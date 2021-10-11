import discord
import os
import random
from stay_awake import stay_awake

bot = discord.Client()

bunny_list = [
  "https://soranews24.com/wp-content/uploads/sites/3/2014/07/anigif_enhanced-buzz-6846-1372172023-3.gif",
  "https://c.tenor.com/BI5IrlWrkTMAAAAd/bunny-too-cute.gif",
  "https://c.tenor.com/9fOKcwHcGMkAAAAM/bluenathmade-blue-nath.gif"
]

@bot.event
async def on_ready():
  print("Logged on as {0.user}".format(bot))

@bot.event
async def on_message(msg):
  print("Received message")

  if msg.author == bot.user:
    return
  if msg.content.startswith("hi") or msg.content.startswith("Hi"):
    await msg.channel.send("Hi, " + msg.author.name + "!")
  elif msg.content.startswith("who"):
    await msg.channel.send("Who am I? I am mlh test bot")
    await msg.channel.send("https://news.mlh.io/wp-content/uploads/2017/07/bot_v2-08-296x300.png")
  elif msg.content.startswith("bunny") or msg.content.startswith("兔子"):
    await msg.channel.send(random.choice(bunny_list))
  else:
    print(msg)
    await msg.channel.send("Why don't you greet me")

# open flask app and call function to keep program running
stay_awake()
# run the bot
bot.run(os.getenv('TOKEN'))