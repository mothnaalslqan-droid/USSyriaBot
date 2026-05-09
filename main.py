import os
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# جلب التوكن من Environment بـ Render
TOKEN = os.environ.get('TOKEN')

# تشغيل Flask عشان Render ما يطفي
app = Flask(__name__)

@app.route('/')
def home():
    return "US Syria Bot is Running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# أوامر بوت التليجرام
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

def main():
    print("Bot is running...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    # شغل Flask بثريد منفصل
    threading.Thread(target=run_flask).start()
    # شغل بوت التليجرام
    main()
