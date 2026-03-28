from telebot import TeleBot, types

from services.api import get_new_image


def register_handlers(bot: TeleBot):
    """
    Регистрирует обработчики команды /start.

    Args:
        bot (TeleBot): Экземпляр Telegram-бота.
    """
    @bot.message_handler(commands=["start"])
    def start(message):
        chat_id = message.chat.id
        name = message.chat.first_name

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("/newcat"))

        bot.send_message(
            chat_id,
            f"Привет, {name}! Вот котик для тебя 🐱",
            reply_markup=keyboard,
        )

        image = get_new_image()
        if image:
            bot.send_photo(chat_id, image)
