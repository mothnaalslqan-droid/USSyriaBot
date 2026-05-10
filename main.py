import os
import asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# قراءة التوكن من متغير البيئة
TOKEN = os.environ.get('TOKEN')

# إنشاء تطبيق Flask
app = Flask(__name__)

# 1. تجهيز البوت
application = Application.builder().token(TOKEN).build()

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("اسعارنا 💵", callback_data='prices')],
        [InlineKeyboardButton("تواصل معنا 📞", callback_data='contact')],
        [InlineKeyboardButton("عن البوت 🤖", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('أهلاً فيك بمُتجرنا!', reply_markup=reply_markup)

# دالة التعامل مع الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'prices':
        await query.edit_message_text(text="هنا الأسعار...")
    elif query.data == 'contact':
        await query.edit_message_text(text="تواصل معنا عبر هذا الرابط...")
    elif query.data == 'about':
        await query.edit_message_text(text="عن البوت: هذا بوت معلوماتي.")

# إضافة الهاندلرز للبوت
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))

# 2. تهيئة البوت قبل التشغيل
asyncio.run(application.initialize())

# 3. Flask Routes
@app.route
