"""
Точка входа в приложение Telegram-бота.

Инициализирует бота и регистрирует обработчики.
"""

import logging
from telebot import TeleBot

from config import TOKEN
from handlers import start, cat

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

bot = TeleBot(TOKEN)

# регистрация хендлеров
start.register_handlers(bot)
cat.register_handlers(bot)


def main():
    """
    Точка входа в приложение.

    Запускает Telegram-бота в режиме polling.
    При падении автоматически перезапускает его.
    """
    while True:
        try:
            bot.polling(none_stop=True)
        except KeyboardInterrupt:
            print("Бот остановлен вручную")
            break  # ⛔ ВАЖНО — выходим из цикла

        except Exception as e:
            logging.error(f"Бот упал: {e}")

if __name__ == "__main__":
    main()
