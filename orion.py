import time
import threading
from flask import Flask
import telebot
import google.generativeai as genai

# ====================================
# WEB SERVER (required for Render)
# ====================================

app = Flask(__name__)

@app.route('/')
def home():
    return "Orion is running"

def run_web():
    import os
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)


# ====================================
# TELEGRAM + GEMINI
# ====================================

BOT_TOKEN = "8356879608:AAGNoug55rbkBdEbpYNqxvwbRJEjgTUbyYo"
GOOGLE_API_KEY = "AIzaSyA_6xCgYS9XoY_ItyxfUMfyTpZLBofExVA"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

bot = telebot.TeleBot(BOT_TOKEN)

bot.remove_webhook()

SYSTEM = "أنت أوريون، خبير أنيميشن ثلاثي الأبعاد بأسلوب Pixar."

def think(user):

    try:

        response = model.generate_content(SYSTEM + user)

        return response.text

    except:

        return "صار في خطأ مؤقت"

def send(chat,text):

    for i in range(0,len(text),4000):

        bot.send_message(chat,text[i:i+4000])

@bot.message_handler(commands=['start'])
def start(msg):

    send(msg.chat.id,"Orion Render 24/7 Active")

@bot.message_handler(func=lambda m: True)
def handle(msg):

    reply = think(msg.text)

    send(msg.chat.id,reply)

# ====================================
# START EVERYTHING
# ====================================

print("ORION STARTED")

threading.Thread(target=run_web).start()

while True:

    try:

        bot.infinity_polling()

    except:

        time.sleep(5)

