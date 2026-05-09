import os
import logging
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import threading

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def home():
    return "البوت شغال تمام"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 شحن شدات ببجي", callback_data='uc')],
        [InlineKeyboardButton("💎 شحن جواهر فري فاير", callback_data='diamonds')],
        [InlineKeyboardButton("👑 اشتراكات", callback_data='subs')],
        [InlineKeyboardButton("📞 الدعم الفني", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "اهلا فيك بمتجر US Syria Store 🇺🇸🇸🇾\nاختر الخدمة:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "uc":
        text = """🔥 **شحن شدات ببجي** 🔥

الأسعار:
- 60 شدة = 1$
- 325 شدة = 5$  
- 660 شدة = 10$
- 1800 شدة = 25$

للطلب تواصل مع الدعم 👨‍💻
@mo3ad_74
"""
        await query.edit_message_text(text=text, parse_mode='Markdown')
    
    elif query.data == "diamonds":
        text = "💎 **شحن جواهر فري فاير** قريباً..."
        await query.edit_message_text(text=text)
    
    elif query.data == "subs":
        text = "👑 **الاشتراكات** قريباً..."
        await query.edit_message_text(text=text)
    
    elif query.data == "support":
        text = "📞 **للدعم الفني تواصل مع:**\n@mo3ad_74"
        await query.edit_message_text(text=text)

def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 10000)))).start()
    run_bot()
