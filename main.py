import telebot
import os
from flask import Flask
import threading

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running!")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

        app = Flask(__name__)

        @app.route('/')
        def home():
            return "USSyriaBot Running"

            def run():
                app.run(host="0.0.0.0", port=10000)

                threading.Thread(target=run).start()

                print("Bot started...")
                bot.infinity_polling()