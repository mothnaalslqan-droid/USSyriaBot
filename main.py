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
import threading

def run_bot():
    print("Bot started...")
        bot.infinity_polling()

        def run_flask():
            app.run(host="0.0.0.0", port=10000)

            if __name__ == '__main__':
                # 1. شغل Flask بخيط لحاله
                    threading.Thread(target=run_flask).start()
                        # 2. شغل البوت بالخيط الرئيسي
                            run_bot()