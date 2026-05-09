import os
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

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
    await update.message.reply_text('اهلا فيك بمتجرنا', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'prices':
        await query.edit_message_text(text="حساب ببجي 50$\nحساب فري فاير 30$")
    elif query.data == 'contact':
        await query.edit_message_text(text="تواصل معنا عالتلغرام: @username")
    elif query.data == 'about':
        await query.edit_message_text(text="نحن متجر الكتروني موثوق")

application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))

# 2. Flask Routes للـ Webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return 'ok'

@app.route('/')
def index():
    return 'Bot is running...'

# 3. شغل البوت مع السيرفر - هاد السطر حل المشكلة
if __name__ == '__main__':
    import asyncio
    async def run():
        await application.initialize()
        await application.start()
        await application.updater.start_webhook(
            listen="0.0.0.0",
            port=int(os.environ.get('PORT', 10000)),
            url_path=TOKEN,
            webhook_url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
        )
    asyncio.run(run())
