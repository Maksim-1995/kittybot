import os
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")


if not TOKEN:
    raise ValueError("TOKEN не установлен")

if not URL:
    raise ValueError("URL не установлен")
