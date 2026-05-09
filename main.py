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
bot.infinity_polling()
