# -*- coding: utf-8 -*-

import telebot
import google.generativeai as genai
import threading
import os
from flask import Flask

# =========================
# TOKENS
# =========================

BOT_TOKEN = "8356879608:AAGNoug55rbkBdEbpYNqxvwbRJEjgTUbyYo"
GOOGLE_API_KEY = "AIzaSyA_6xCgYS9XoY_ItyxfUMfyTpZLBofExVA"

# =========================
# GEMINI
# =========================

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# =========================
# TELEGRAM BOT
# =========================

bot = telebot.TeleBot(BOT_TOKEN)

SYSTEM_PROMPT = """
أنت أوريون، خبير عالمي في الأنيميشن 3D وسرد القصص بأسلوب بيكسار.
تتحدث دائماً باللهجة السورية.
"""

def generate_reply(text):

    try:

        prompt = SYSTEM_PROMPT + "\nالمستخدم: " + text + "\nأوريون:"

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        print(e)

        return "صار خطأ."

@bot.message_handler(commands=['start'])

def start(msg):

    bot.reply_to(msg, "أهلاً أنا أوريون")

@bot.message_handler(func=lambda m: True)

def handle(msg):

    reply = generate_reply(msg.text)

    bot.reply_to(msg, reply)

# =========================
# FLASK
# =========================

app = Flask(__name__)

@app.route('/')

def home():

    return "Orion is alive"

# =========================
# START BOT
# =========================

def run_bot():

    bot.infinity_polling()

threading.Thread(target=run_bot).start()
