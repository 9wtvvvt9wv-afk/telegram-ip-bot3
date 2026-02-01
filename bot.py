from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

# توکن بات از متغیر محیطی گرفته میشه
TOKEN = os.getenv("8171864770:AAECNop0Q2pSRGLWz1def8M2UY5kp-6SFK4")

def get_public_ip():
    # گرفتن آی‌پی عمومی از api.ipify
    return requests.get("https://api.ipify.org", timeout=5).text

async def ip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # ارسال آی‌پی عمومی به کاربر
        ip = get_public_ip()
        await update.message.reply_text(f"🌐 Public IP:\n{ip}")
    except:
        # در صورت بروز خطا
        await update.message.reply_text("❌ خطا در دریافت IP")

# استفاده از ApplicationBuilder برای ساخت اپلیکیشن
app = ApplicationBuilder().token(TOKEN).build()

# ثبت دستور /ip
app.add_handler(CommandHandler("ip", ip_command))

# اجرای بات
print("Bot is running...")
app.run_polling()
