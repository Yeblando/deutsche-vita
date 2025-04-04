from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Ваш токен
TOKEN = "7916092260:AAEKZ3jEiC5_bwCuUO8AHpiEOdZQ-K6IL1k"

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text("Привет! Я бот!")

# Главная функция для запуска бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Добавление обработчика команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
