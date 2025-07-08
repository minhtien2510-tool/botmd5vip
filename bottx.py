
import telebot
import hashlib
import json
import os

BOT_TOKEN = os.getenv("7934189123:AAEmKx_e0PKWbXKlcK5x2eEhzFbGG7ErJYs")
ADMIN_ID = os.getenv("ADMIN_ID", "")
ALLOWED_KEYS = {"demo123": "active"}

user_keys = {}

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Chào mừng bạn đến với Bot giải mã MD5"!)
"Vui lòng nhập key bằng lệnh /key để tiếp tục."

@bot.message_handler(commands=['key'])
def key_handler(message):
    key = message.text.replace('/key', '').strip()
    if key in ALLOWED_KEYS:
        user_keys[message.chat.id] = key
        bot.reply_to(message, "🔓 Key hợp lệ. Bạn có thể gửi mã MD5 để giải mã.")
    else:
        bot.reply_to(message, "❌ Key không hợp lệ. Vui lòng thử lại.")

@bot.message_handler(func=lambda m: True)
def md5_handler(message):
    if message.chat.id not in user_keys:
        bot.reply_to(message, "❗ Vui lòng nhập key trước bằng lệnh /key.")
        return

    md5 = message.text.strip().lower()
    if len(md5) != 32 or not all(c in "0123456789abcdef" for c in md5):
        bot.reply_to(message, "⚠️ Mã MD5 không hợp lệ.")
        return

    result = giai_ma_md5(md5)
    bot.reply_to(message, f"✅ Kết quả phân tích MD5:

{result}")

def giai_ma_md5(md5):
    # Giải mã bằng công thức đơn giản cho ví dụ
    bytes_sum = sum(int(md5[i:i+2], 16) for i in range(0, 32, 2))
    result = "Tài" if bytes_sum % 2 == 0 else "Xỉu"
    return f"Mã: {md5}
Tổng byte: {bytes_sum}
→ Kết quả: {result}"

bot.polling()
