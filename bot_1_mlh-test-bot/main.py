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
  if msg.content.lower().startswith("hi"):
    await msg.channel.send("Hi, {0}!".format(msg.author.name))
  elif msg.content.startswith("who"):
    await msg.channel.send("Who am I? I am mlh test bot")
    await msg.channel.send("https://news.mlh.io/wp-content/uploads/2017/07/bot_v2-08-296x300.png")
  elif "bunny" in msg.content.lower() or "兔子" in msg.content:
    await msg.channel.send(random.choice(bunny_list))
  elif "python" in msg.content:
    await msg.add_reaction("\U0001F40D")
  elif "lol" in msg.content.lower():
    await msg.add_reaction("\U0001F923")
  else:
    print(msg)
    await msg.channel.send("Why don't you greet me")

@bot.event
async def on_raw_reaction_add(payload):
  if payload.emoji.name == "✅":
    channel = discord.utils.get(bot.get_all_channels(), id=payload.channel_id)
    user = payload.member
    await channel.send("Nice job, {0}!".format(user.mention))

# open flask app and call function to keep program running
stay_awake()
# run the bot
bot.run(os.getenv('TOKEN'))