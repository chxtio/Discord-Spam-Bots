import discord
import os
import random
from stay_awake import stay_awake

intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)

test_channel_id = 920441829722292274


# Greet incoming members
@bot.event
async def on_member_join(member):
  print('member joined')
  channel_id = 850235699981844513
  # channel_id = 753590323011256375 # For testing
  channel = bot.get_channel(channel_id)

  if not channel:
    return

  # await channel.send(f"Hi, {member.name}!")
  embed = discord.Embed(
    title=f"Welcome {member.name}!", description="Say hi!"
  )  #description=f"Thanks for joining {member.guild.name}!")
  embed.set_thumbnail(
    url=member.avatar_url
  )  # Set the embed's thumbnail to the member's avatar image
  await channel.send(embed=embed)


bunny_list = [
  "https://soranews24.com/wp-content/uploads/sites/3/2014/07/anigif_enhanced-buzz-6846-1372172023-3.gif",
  "https://c.tenor.com/BI5IrlWrkTMAAAAd/bunny-too-cute.gif",
  "https://c.tenor.com/9fOKcwHcGMkAAAAM/bluenathmade-blue-nath.gif",
  "https://44.media.tumblr.com/74061f5bc168f012d5c4281176a97b28/tumblr_n5leqjUYea1qc4uvwo1_500.gif"
]


@bot.event
async def on_ready():
  print("Logged on as {0.user}".format(bot))


# Handle messages
@bot.event
async def on_message(msg):
  print("Received message")

  if msg.author == bot.user:
    return

  pythonFile = False
  javaFile = False

  if msg.attachments:
    attachment = msg.attachments[0].url
    print("received attachment: ", attachment)
    if attachment.endswith(".py"):
      pythonFile = True
    if attachment.endswith(".java"):
      javaFile = True

  if "python" in msg.content or pythonFile:
    await msg.add_reaction("🐍")
  elif "java" in msg.content or javaFile:
    await msg.add_reaction("☕")
  #lc-progress-pt-2 channel
  if msg.channel.id == 1106739534764458106 and "Daily LeetCoding Challenge" in msg.content:
    await msg.channel.send("https://leetcode.com/static/images/coin.gif")

  if msg.content.lower().startswith("hi"):
    # await msg.channel.send("Hi, {0}!".format(msg.author.name))
    await msg.channel.send("Hi, {0}!".format(msg.author.mention))
  elif msg.content.startswith("who"):
    await msg.channel.send("Who am I? I am mlh test bot")
    await msg.channel.send(
      "https://news.mlh.io/wp-content/uploads/2017/07/bot_v2-08-296x300.png")
  elif "bunny" in msg.content.lower() or "兔子" in msg.content:
    await msg.channel.send(random.choice(bunny_list))
  elif "lol" in msg.content.lower():
    await msg.add_reaction("😄")
  elif msg.channel.id == 857746001226235927 and msg.author.id == 638275704986796032:  # React in gaming channel
    await msg.add_reaction("💯")
  elif msg.channel.id == 1010750702336880690:  # React in 2023 postings channel
    await msg.add_reaction("✅")
  else:
    pass
    # print(msg)
    # await msg.channel.send("Why don't you greet me")


@bot.event
async def on_raw_reaction_add(payload):
  user = payload.member
  guild_id = payload.guild_id
  channel_id = payload.channel_id
  msg_id = payload.message_id
  msg_link = f"https://discord.com/channels/{guild_id}/{channel_id}/{payload.message_id}"

  # When a user reacts to indicate completion of task, the bot responds w/ a link to the msg
  if payload.emoji.name == "✅" and user.name != "mlh-test-bot":
    channel = discord.utils.get(bot.get_all_channels(), id=payload.channel_id)
    # Slow warn Vincent
    if channel.id == 1077742468965093487 and user.id == 429463598629257227:
      await channel.send(
        f'¡Ay Dios mio {user.mention}! Slow down speedy Gonzalez! {msg_link}')
      if random.randint(0, 1) == 1:
        await channel.send(
          "https://gifdb.com/images/high/speedy-gonzales-running-t0uvc86wu0vlqdwv.gif"
        )
    else:
      await channel.send(f"Nice job, {user.mention}! {msg_link}")


# open flask app and call function to keep program running
stay_awake()
# run the bot
bot.run(os.getenv('TOKEN'))
""" helpful links
UptimeRobot:
https://uptimerobot.com/dashboard#mainDashboard

Emoji list:
https://unicode.org/emoji/charts/full-emoji-list.html
"""
