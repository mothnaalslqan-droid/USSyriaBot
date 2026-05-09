import os
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get('TOKEN')
app = Flask(__name__)

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

# اعداد البوت
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))

@app.route('/', methods=['GET'])
def home():
    return "US Syria Bot is Running!"

@app.route(f'/{TOKEN}', methods=['POST'])
async def webhook():
    await application.update_queue.put(Update.de_json(request.get_json(force=True), application.bot))
    return 'ok'

@app.route('/set_webhook', methods=['GET'])
async def set_webhook():
    url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    await application.bot.set_webhook(url)
    return f"webhook setup to {url}"

if __name__ == '__main__':
    print("Bot is running...")
    app.run(host='0.0.0.0', port=10000)
