
import telebot
from datetime import datetime

bot = telebot.TeleBot("7934189123:AAF8DPl_JDoTj5Xa3RrUxoaofHHO3pGaNkY")  # ← Thay bằng token thật
session_data = {}

# Dữ liệu key truy cập
key_data = {
    "key_vip999": {
        "expires": "2025-07-15 10:51:40"
    }
}

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = str(message.chat.id)
    if user_id not in session_data:
        session_data[user_id] = {"authenticated": False}
        bot.reply_to(message, "🔐 Nhập key truy cập:")
    else:
        bot.reply_to(message, "🔐 Bạn đã xác thực, hãy gửi mã MD5.")

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    user_id = str(message.chat.id)
    text_input = message.text.strip()

    if not session_data.get(user_id, {}).get("authenticated", False):
        if text_input in key_data:
            expires = datetime.strptime(key_data[text_input]["expires"], "%Y-%m-%d %H:%M:%S")
            if datetime.now() < expires:
                session_data[user_id]["authenticated"] = True
                bot.reply_to(message, "✅ Key hợp lệ! Hãy gửi mã MD5:")
            else:
                bot.reply_to(message, "❌ Key đã hết hạn!")
        else:
            bot.reply_to(message, "❌ Key không hợp lệ!")
        return

    if len(text_input) == 32 and all(c in "0123456789abcdef" for c in text_input.lower()):
        bot.reply_to(message, "✅ Đã nhận mã MD5: {}\n🔍 Đang phân tích...".format(text_input))
        # TODO: Giải mã tại đây
        bot.reply_to(message, "🎯 Kết quả: TÀI hoặc XỈU (dựa trên công thức)")
    else:
        bot.reply_to(message, "❌ Vui lòng nhập đúng 32 ký tự mã MD5.")

bot.polling()
