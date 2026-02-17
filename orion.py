import time
import telebot
import google.generativeai as genai

BOT_TOKEN = "8356879608:AAGNoug55rbkBdEbpYNqxvwbRJEjgTUbyYo"
GOOGLE_API_KEY = "AIzaSyA_6xCgYS9XoY_ItyxfUMfyTpZLBofExVA"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

bot = telebot.TeleBot(BOT_TOKEN)

bot.remove_webhook()

SYSTEM = "أنت أوريون خبير أنيميشن ثلاثي الأبعاد بأسلوب Pixar"

def think(user):

    try:

        response = model.generate_content(SYSTEM + user)

        return response.text

    except:

        return "خطأ مؤقت"

def send(chat,text):

    for i in range(0,len(text),4000):

        bot.send_message(chat,text[i:i+4000])

@bot.message_handler(commands=['start'])
def start(msg):

    send(msg.chat.id,"Orion Render Active")

@bot.message_handler(func=lambda m: True)
def handle(msg):

    reply = think(msg.text)

    send(msg.chat.id,reply)

print("STARTING ORION")

while True:

    try:

        bot.infinity_polling(timeout=60,long_polling_timeout=60)

    except Exception as e:

        print(e)

        time.sleep(5)
