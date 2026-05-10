import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# =================
# ضع توكن البوت هنا
# =================
TOKEN = "8318531021:AAFTTePdd6GqWPw-d80lSDdoYm-47-tXnUI"

# =================
# ضع رابط Webhook الخاص بـ Render
# =================
WEBHOOK_URL = "https://ussyriabot-3.onrender.com/"

app = Flask(__name__)

# =================
# تعريف أوامر البوت
# =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! البوت يعمل بنجاح ✅")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"رسالتك: {update.message.text}")

# =================
# إعداد البوت مع Webhook
# =================
bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# =================
# Webhook route
# =================
@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot_app.bot)
    asyncio.run(bot_app.process_update(update))
    return "ok"

# =================
# تشغيل Flask + Webhook
# =================
if __name__ == "__main__":
    bot_app.bot.delete_webhook()
    bot_app.bot.set_webhook(WEBHOOK_URL)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
