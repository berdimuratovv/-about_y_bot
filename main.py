import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men Gemini AI botman. Menga xabar yozing.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = model.generate_content(user_text)
    await update.message.reply_text(response.text)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

app.run_polling()
