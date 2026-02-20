from flask import Flask
from threading import Thread
import asyncio
import bot  # твой основной файл с ботом

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот EasyGacha работает!"

def run_bot():
    asyncio.run(bot.main())  # запускаем функцию main() из bot.py

@app.route('/health')
def health():
    # Для внешних пингов
    return "OK"

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    t = Thread(target=run_bot)
    t.start()
    # Запускаем веб-сервер Flask
    app.run(host="0.0.0.0", port=8080)