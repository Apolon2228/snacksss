from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Токен от BotFather
BOT_TOKEN = "8213722718:AAET5oXn6oK-LIOKRtWtKZl1A74400SEcqI"
CHAT_ID = None  # будем хранить chat_id пользователя

# 📌 Маршрут для сайта — сюда сайт будет отправлять данные
@app.route("/send", methods=["POST"])
def send_message():
    global CHAT_ID
    data = request.get_json()
    message = data.get("message", "Пустое сообщение")

    if CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": message})
        return jsonify({"status": "ok", "message": "Отправлено в Telegram"})
    else:
        return jsonify({"status": "error", "message": "Пользователь ещё не написал боту /start"})

# 📌 Вебхук от Telegram (чтобы поймать chat_id при /start)
@app.route("/webhook", methods=["POST"])
def webhook():
    global CHAT_ID
    update = request.get_json()
    if "message" in update:
        CHAT_ID = update["message"]["chat"]["id"]
    return "ok"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
