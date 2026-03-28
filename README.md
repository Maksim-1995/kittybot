# 🐱 Telegram Kitty Bot

Простой Telegram-бот на Python, который отправляет случайные изображения котиков (и собак как fallback).

---

## 🚀 Функциональность

* Команда `/start` — приветствие и отправка котика
* Команда `/newcat` — получить нового котика
* Резервный API (если основной недоступен)
* Логирование ошибок
* Обработка сбоев API

---

## 🏗 Структура проекта

```
kittybot/
├── main.py
├── config.py
├── services/
│   └── api.py
├── handlers/
│   ├── start.py
│   └── cat.py
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Установка

### 1. Клонирование репозитория

```
git clone <your-repo>
cd bot
```

### 2. Создание виртуального окружения

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Установка зависимостей

```
pip install -r requirements.txt
```

---

## 🔐 Настройка окружения

Создай файл `.env`:

```
TOKEN=your_telegram_token
URL=https://api.thecatapi.com/v1/images/search
```

---

## ▶️ Запуск

```
python main.py
```

---

## 🧩 requirements.txt

```
pyTelegramBotAPI
python-dotenv
requests
```
