
import telebot

API_TOKEN = 'YOUR_API_KEY_HERE'  # <-- Thay bằng API Bot của bạn
bot = telebot.TeleBot(API_TOKEN)

# Hàm xử lý khi người dùng gửi /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Chào mừng bạn đến với Bot giải mã MD5!\nGõ /key để nhập key sử dụng.")

# Hàm xử lý khi người dùng gửi /key
@bot.message_handler(commands=['key'])
def ask_for_key(message):
    bot.reply_to(message, "🔑 Vui lòng nhập key sử dụng bot:")

# Hàm phân tích MD5
def giai_ma_md5(md5):
    # Giả lập kết quả: bạn thay thế bằng thuật toán của bạn
    if md5.startswith("a"):
        return "Tài"
    else:
        return "Xỉu"

# Hàm xử lý tin nhắn thường
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    input_text = message.text.strip()
    if len(input_text) == 32:
        ket_qua = giai_ma_md5(input_text)
        bot.reply_to(message, f"""✅ Kết quả phân tích MD5:
🧩 Mã: {input_text}
🎯 Kết quả: {ket_qua}
""")
    else:
        bot.reply_to(message, "❌ Mã MD5 không hợp lệ. Vui lòng nhập đúng 32 ký tự.")

# Chạy bot
print("🤖 Bot đang chạy...")
bot.infinity_polling()
