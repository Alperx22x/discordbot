from keep_alive import keep_alive
keep_alive()

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # Mesaj içeriğine erişim izni

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
print(f"Bot aktif: {bot.user}")

@bot.command()
async def selam(ctx):
await ctx.send("Selam! Ben 7/24 aktifim. 🟢")

bot.run("BOT_TOKEN")
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
return "Bot çalışıyor!"

def run():
app.run(host='0.0.0.0', port=8080)

def keep_alive():
t = Thread(target=run)
t.start()