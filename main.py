import os
import asyncio
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# ====== إعدادات البوت ======
TOKEN = "YOUR_BOT_TOKEN_HERE"  # استبدل هنا بالتوكن الفعلي من BotFather
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
app = Flask(__name__)

# Dispatcher لإدارة التحديثات
dispatcher = Dispatcher(bot, None, use_context=True)

# ====== تعريف الأوامر ======
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="أهلاً! البوت شغال ✅")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# تسجيل الأوامر في الـ dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# ====== Flask route للـ webhook ======
@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# ====== تشغيل البوت ======
if __name__ == "__main__":
    # إزالة أي webhook قديم
    bot.delete_webhook()
    # تعيين webhook الجديد
    bot.set_webhook(url=WEBHOOK_URL)
    # تشغيل Flask على Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
