
import telebot
import json

TOKEN = "7934189123:AAEmKx_e0PKWbXKlcK5x2eEhzFbGG7ErJYs"
bot = telebot.TeleBot(TOKEN)

# Load dữ liệu MD5 từ file JSON
with open("data_md5_500k.json", "r") as f:
    md5_data = json.load(f)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng bạn đến với bot giải mã MD5 Tài/Xỉu!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    msg = message.text.strip().lower()
    if msg in md5_data:
        result = md5_data[msg]
        ket_qua = "Tài" if result >= 11 else "Xỉu"
        bot.reply_to(message, f"✅ Kết quả giải mã MD5: {ket_qua} ({result})")
    else:
        bot.reply_to(message, "❌ Mã MD5 chưa được học. Vui lòng thử lại mã khác.")

bot.infinity_polling()
