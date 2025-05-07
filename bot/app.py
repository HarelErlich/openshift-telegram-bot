# bot/app.py
import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("⚠️ BOT_TOKEN environment variable is not set!", flush=True)

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📩 Received data:", data, flush=True)

    try:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        print(f"💬 From chat_id {chat_id}: '{text}'", flush=True)

        if text == "/start":
            send_message(chat_id, "Hello! I'm alive on OpenShift 🚀")
        else:
            send_message(chat_id, f"You said: {text}")

    except Exception as e:
        print("❌ Error handling incoming message:", e, flush=True)

    return {"ok": True}

def send_message(chat_id, text):
    if not BOT_TOKEN:
        print("❌ Cannot send message: BOT_TOKEN is not set", flush=True)
        return

    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    print(f"➡️ Sending to Telegram: {payload}", flush=True)

    try:
        response = requests.post(url, json=payload)
        print(f"✅ Telegram response {response.status_code}: {response.text}", flush=True)
    except Exception as e:
        print("❌ Error sending message to Telegram:", e, flush=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

