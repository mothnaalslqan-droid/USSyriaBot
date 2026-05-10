import os
import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# قراءة التوكن من متغير البيئة
TOKEN = os.environ.get('TOKEN')

# تهيئة Flask
app = Flask(__name__)

# تهيئة البوت
application = Application.builder().token(TOKEN).build()


# دالة البداية مع لوحة أزرار
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("اسعارنا 💲", callback_data='prices')],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data='contact')],
        [InlineKeyboardButton("عن البوت 🤖", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('أهلا فيك! اختار من القائمة:', reply_markup=reply_markup)


# دالة التعامل مع الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'prices':
        await query.edit_message_text(text="هذه قائمة الأسعار لدينا...")
    elif query.data == 'contact':
        await query.edit_message_text(text="يمكنك التواصل معنا عبر @username")
    elif query.data == 'about':
        await query.edit_message_text(text="هذا بوت تجريبي يعمل على Render.")


# إضافة الـ Handlers للبوت
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))


# Flask route لاستقبال Webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "OK"


# تفعيل Webhook عند تشغيل البوت
async def set_webhook():
    url = f"https://<your-service-name>.onrender.com/{TOKEN}"
    await application.bot.set_webhook(url)
    print("Webhook set to:", url)


# تشغيل Flask + تهيئة Webhook
if __name__ == '__main__':
    asyncio.run(set_webhook())
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
