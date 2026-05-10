import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

# ==========
# ضع 8318531021:AAFTTePdd6GqWPw-d80lSDdoYm-47-tXnUI
# ==========
TOKEN = "@USSyriastore_bot"

# ==========
# ضع هنا رابط Webhook الخاص بـ Render
# https://ussyriabot-3.onrender.com/
# ==========
WEBHOOK_URL = "PUT_YOUR_RENDER_URL_HERE"

# ==========
# إعداد البوت والـ Flask
# ==========
bot = Bot(token=TOKEN)
app = Flask(__name__)
dp = Dispatcher(bot, None, workers=0, use_context=True)

# ==========
# أوامر البوت
# ==========
def start(update: Update, context: CallbackContext):
    update.message.reply_text("أهلاً! البوت يعمل بنجاح ✅")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"رسالتك: {update.message.text}")

# تسجيل الأوامر
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# ==========
# Webhook route
# ==========
@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    asyncio.run(dp.process_update(update))
    return "ok"

# ==========
# تشغيل البوت مع Flask
# ==========
if __name__ == "__main__":
    # تفعيل Webhook عند بدء التشغيل
    bot.delete_webhook()
    bot.set_webhook(WEBHOOK_URL)

    # تشغيل Flask على Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
