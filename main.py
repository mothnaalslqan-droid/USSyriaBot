import os
import threading
from flask import Flask
import telebot

# --- الاعدادات ---
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- صفحة الويب عشان Render ما يطفي ---
@app.route('/')
def home():
    return "Bot is running"

    # --- اوامر البوت ---
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "أهلاً! البوت شغال ✅")

        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            bot.reply_to(message, message.text)

            # --- تشغيل البوت والسيرفر سوا ---
            def run_bot():
                print("Bot started...")
                    bot.infinity_polling()

                    def run_flask():
                        app.run(host="0.0.0.0", port=10000)

                        if __name__ == '__main__':
                            threading.Thread(target=run_flask).start()
                                run_bot()