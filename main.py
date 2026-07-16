import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# إعداد نظام تسجيل الأخطاء لرصد حالة البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 1. أمر الترحيب والبداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"أهلاً بك يا {user.mention_html()} في بوت الحماية والتسلية المتقدم! 🤖⚡"
    )

# 2. أمر عرض الايدي
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    
    text = (
        f"👤 **معلوماتك الشخصية:**\n\n"
        f"🔸 الاسم: {user.first_name}\n"
        f"🔸 الايدي الخاص بك: `{user.id}`\n"
        f"🔹 ايدي المجموعة: `{chat.id}`"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

# تشغيل البوت
def main():
    # هنا يجب وضع التوكن الخاص بالبوت المستخرج من BotFather
    # سنقوم ببرمجتها لاحقاً لتقرأ من متغيرات البيئة تلقائياً للحماية
    TOKEN = "YOUR_BOT_TOKEN" 
    
    application = Application.builder().token(TOKEN).build()

    # تسجيل الأوامر في البوت
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Regex("^ايدي$"), get_id))

    # بدء تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
