from flask import Flask
from threading import Thread
import asyncio
import os
import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот EasyGacha работает!"

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Запускаем Flask в отдельном потоке
    t = Thread(target=run_flask)
    t.start()
    # Запускаем бота в главном потоке
    asyncio.run(bot.main())