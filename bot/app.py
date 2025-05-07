# bot/app.py
import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        send_message(chat_id, "Hello! I'm alive on OpenShift 🚀")
    else:
        send_message(chat_id, f"You said: {text}")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

