
import telebot
import json

TOKEN = "7934189123:AAEmKx_e0PKWbXKlcK5x2eEhzFbGG7ErJYs"
bot = telebot.TeleBot(TOKEN)

with open("data_md5_500k.json", "r") as f:
    md5_data = json.load(f)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👋 Chào mừng bạn đến với Bot giải mã MD5 Tài/Xỉu!")

@bot.message_handler(func=lambda m: True)
def handle_md5(message):
    md5_input = message.text.strip().lower()

    if md5_input in md5_data:
        result = md5_data[md5_input]
        bot.reply_to(message, f"✅ Kết quả giải mã MD5:
→ {result}")
    else:
        bot.reply_to(message, f"⚠️ MD5 chưa học:
→ {md5_input}")

bot.polling()
