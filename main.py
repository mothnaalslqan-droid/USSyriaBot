import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask
import threading

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Running"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("اسعارنا 💲", callback_data='prices')],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data='contact')],
        [InlineKeyboardButton("عن البوت 🤖", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً فيك بمتجر US Syria الرسمي 🔥\n\n"
        "✅ شحن شدات ببجي موبايل بأرخص الأسعار\n"
        "✅ زيادة متابعين إنستغرام حقيقيين\n"
        "✅ زيادة مشاهدات ريلز وإعجابات\n"
        "✅ الدفع الآمن عبر شام كاش\n\n"
        "اختر من القائمة:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'prices':
        await query.edit_message_text(
            "💲 *قائمة أسعارنا:*\n\n"
            "🎮 *ببجي موبايل:*\n"
            "• 60 شدة - 1$\n"
            "• 325 شدة - 5$\n"
            "• 660 شدة - 10$\n"
            "• 1800 شدة - 25$\n\n"
            "📱 *إنستغرام:*\n"
            "• 1000 متابع - 3$\n"
            "• 5000 متابع - 12$\n"
            "• 10000 مشاهدة ريلز - 2$",
            parse_mode='Markdown'
        )
    elif query.data == 'contact':
        await query.edit_message_text(
            "📞 *للتواصل والطلب:*\n\n"
            "يوزر التليجرام: @mo3ad_74\n\n"
            "💰 الدفع عبر شام كاش فقط",
            parse_mode='Markdown'
        )
    elif query.data == 'about':
        await query.edit_message_text(
            "🤖 *عن متجر US Syria*\n\n"
            "متجر سوري موثوق 100%\n"
            "✅ أسعار منافسة\n"
            "✅ ضمان على الخدمة",
            parse_mode='Markdown'
        )

def main():
    threading.Thread(target=run_flask).start()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    main()
