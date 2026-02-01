from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

# توکن جدید رو مستقیماً وارد می‌کنیم
TOKEN = "8171864770:AAECNop0Q2pSRGLWz1def8M2UY5kp-6SFK4"  # توکن جدید شما

def get_public_ip():
    return requests.get("https://api.ipify.org", timeout=5).text

async def ip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        ip = get_public_ip()
        await update.message.reply_text(f"🌐 Public IP:\n{ip}")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا در دریافت IP: {str(e)}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("ip", ip_command))

print("Bot is running...")
app.run_polling()
