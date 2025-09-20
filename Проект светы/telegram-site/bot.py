from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# вставь сюда свой токен, полученный у BotFather
TOKEN = "8213722718:AAET5oXn6oK-LIOKRtWtKZl1A74400SEcqI"

# /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот твоего сайта 🌐")

# простая реакция на текст
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ты написал: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # регистрируем команды и обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # запускаем бота
  app.run_webhook(
    listen="0.0.0.0",
    port=5000,
    webhook_url="https://http://127.0.0.1:4000/webhook"
)


if __name__ == "__main__":
    main()
 
