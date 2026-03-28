"""Обработчики команд, связанных с отправкой изображений животных."""

from telebot import TeleBot

from services.api import get_new_image


def register_handlers(bot: TeleBot):
    """
    Регистрирует обработчики команды /newcat.

    Args:
        bot (TeleBot): Экземпляр Telegram-бота.
    """
    @bot.message_handler(commands=["newcat"])
    def new_cat(message):
        chat_id = message.chat.id
        image = get_new_image()

        if image:
            bot.send_photo(chat_id, image)
        else:
            bot.send_message(chat_id, "Не удалось получить изображение 😢")
