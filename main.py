import telebot
import os

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلين يا وحش! بوت US سوريا شغال 24/7 🔥\nأرسل /help للمساعدة")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "الأوامر:\n/start - ترحيب\n/help - المساعدة\n\nالبوت مجاني وشغال دايماً")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "استلمت: " + message.text)

print("Bot is running...")

# === كود الضحك على Render ===
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "USSyriaBot شغال ✅"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_flask).start()
# === خلصنا ضحك ===

bot.infinity_polling()
