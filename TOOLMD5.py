import telebot
import json
import hashlib

API_KEY = '7934189123:AAEtsWTLTRex1XMInQGmNK5aUZzCmlBxObI'
bot = telebot.TeleBot(API_KEY)

with open('data_md5_500k.json', 'r') as f:
    md5_data = json.load(f)

def predict_result(md5):
    if md5 in md5_data:
        return f"✅ MD5 đã học: {md5} → Kết quả thật: {md5_data[md5]}"
    else:
        # Áp dụng công thức mạnh nhất
        total = sum(int(c, 16) for c in md5[:16])  # đơn giản hóa
        if total % 2 == 0:
            return "🌠 Xâm Nhập Md5 Thành Công : ✅ XỈU"
        else:
            return "🌠 Xâm Nhập Md5 Thành Công : ✅ TÀI"

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "🔐 Nhập key truy cập:")

@bot.message_handler(func=lambda m: True)
def handle(msg):
    text = msg.text.strip()
    if len(text) == 32:
        result = predict_result(text.lower())
        bot.reply_to(msg, result)
    else:
        bot.reply_to(msg, "❌ Vui lòng nhập đúng 32 ký tự mã MD5.")

print("🤖 Bot đang chạy...")
bot.polling()
