import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# رسالة الترحيب + الأزرار
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 شدات ببجي", callback_data="uc")],
        [InlineKeyboardButton("📱 متابعين انستا", callback_data="insta")],
        [InlineKeyboardButton("💰 أسعار الشدات", callback_data="prices")],
        [InlineKeyboardButton("👨‍💻 تواصل مع الدعم", url="https://t.me/YOUR_USERNAME")] # حط يوزرك هون
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = """
🔥 **أهلاً فيك بمتجر US Syria الرسمي** 🔥

شحن شدات ببجي بأرخص الأسعار ✅
زيادة متابعين انستغرام حقيقيين ✅
الدفع آمن 100% ✅

اختر طلبك من الأزرار تحت 👇
"""
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# لما يكبس على الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "uc":
        text = """
🔥 **شحن شدات ببجي** 🔥

الأسعار:
- 60 شدة = 1$
- 325 شدة = 5$ 
- 660 شدة = 10$
- 1800 شدة = 25$

للطلب تواصل مع الدعم 👨‍💻
@YOUR_USERNAME
"""
        await query.edit_message_text(text)
        
    elif query.data == "insta":
        text = """
📱 **زيادة متابعين انستغرام** 📱

الأسعار:
- 1000 متابع = 3$
- 5000 متابع = 12$
- 10000 متابع = 20$

متابعين حقيقيين + ضمان ✅

للطلب تواصل مع الدعم 👨‍💻
@YOUR_USERNAME
"""
        await query.edit_message_text(text)
        
    elif query.data == "prices":
        text = """
💰 **قائمة الأسعار الكاملة** 💰

**شدات ببجي:**
60 = 1$ | 325 = 5$ | 660 = 10$ | 1800 = 25$

**متابعين انستا:**
1K = 3$ | 5K = 12$ | 10K = 20$

الدفع: سيرياتيل كاش - شام كاش - USDT

للطلب اضغط /start واختار تواصل مع الدعم
"""
        await query.edit_message_text(text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
