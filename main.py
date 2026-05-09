import os
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

TOKEN = os.environ.get('TOKEN')
app = Flask(__name__)

# 1. جهز البوت
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("اسعارنا 💲", callback_data='prices')],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data='contact')],
        [InlineKeyboardButton("عن البوت 🤖", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('أهلاً فيك بمتجر US Syria الرسمي 🔥', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'prices':
        await query.edit_message_text(text="أسعارنا:\n\n- حساب Netflix: 5$\n- حساب Spotify: 3$\n- شحن شدات ببجي: 10$\n\nلطلب تواصل معنا 👇")
    elif query.data == 'contact':
        await query.edit_message_text(text="تواصل معنا:\n\nتليجرام: @mo3ad_74")
    elif query.data == 'about':
        await query.edit_message_text(text="بوت متجر US Syria الرسمي\n\nلبيع الحسابات والشحن الآمن ✅")

application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))

# 2. تهيئة البوت قبل التشغيل - هاد السطر حل المشكلة
asyncio.run(application.initialize())

# 3. Flask Routes
@app.route('/')
def home():
    return "US Syria Bot is Running!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return 'ok'

@app.route('/setwebhook', methods=['GET'])
def set_webhook():
    url = f"https://ussyriabot.onrender.com/{TOKEN}"
    asyncio.run(application.bot.set_webhook(url))
    return f"Webhook set to {url}"

if __name__ == '__main__':
    print("Bot is running...")
    app.run(host='0.0.0.0', port=10000)
