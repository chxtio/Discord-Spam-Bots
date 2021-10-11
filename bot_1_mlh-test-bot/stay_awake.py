from flask import Flask
from threading import Thread

app = Flask("")

@app.route('/')
def home():
  return "Hey, I'm awake!"

# Run development server
# https://flask.palletsprojects.com/en/2.0.x/server/#development-server
def run():
  app.run(host='0.0.0.0', port=8080)

# repl.it shuts down code after 1 hr of inactivity
# uptime robot will keep hitting the web server every 5 min to prevent from sleeping
# https://uptimerobot.com/
def stay_awake():
  t = Thread(target=run)
  t.start()