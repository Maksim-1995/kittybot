"""
Модуль для работы с внешними API (котики/собаки).
Содержит функции для получения случайных изображений.
"""

import logging
import requests

from config import URL


DOG_API = "https://api.thedogapi.com/v1/images/search"


def get_new_image():
    """
    Получает случайное изображение кота из основного API.
    
    Если основной API недоступен, использует fallback API (собаки).

    Returns:
        str | None: URL изображения или None, если получить не удалось.
    """
    urls = [URL, DOG_API]

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()

            if isinstance(data, list) and data:
                image_url = data[0].get("url")
                if image_url:
                    return image_url

        except requests.RequestException as error:
            logging.error(f"Ошибка API ({url}): {error}")

    return None
