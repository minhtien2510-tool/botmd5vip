
import telebot
import hashlib
import json
from difflib import SequenceMatcher

API_KEY = "7934189123:AAEmKx_e0PKWbXKlcK5x2eEhzFbGG7ErJYs"
bot = telebot.TeleBot(API_KEY)

# Nạp dữ liệu học (dạng file json: {"md5": "tai/xiu"})
with open("data_md5_500k.json", "r") as f:
    learned_data = json.load(f)

# Công thức mạnh nhất từng huấn luyện
def giai_ma_md5(md5):
    b = bytes.fromhex(md5)
    total = sum(b)
    xucxac = [(b[0] + b[15]) % 6 + 1, (b[1] + b[14]) % 6 + 1, (b[2] + b[13]) % 6 + 1]
    tong = sum(xucxac)
    ketqua = "Tài" if tong >= 11 else "Xỉu"
    return ketqua, xucxac, tong

# Tìm mã gần giống nếu không có trong tập
def tim_ma_gan_nhat(md5):
    best_match = None
    best_ratio = 0
    for known_md5 in learned_data:
        ratio = SequenceMatcher(None, md5, known_md5).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = known_md5
    return best_match, best_ratio

# Xử lý tin nhắn
@bot.message_handler(func=lambda msg: True)
def xu_ly(msg):
    text = msg.text.strip().lower()
    if len(text) == 32:
        try:
            md5 = text
            if md5 in learned_data:
                result = learned_data[md5]
                bot.reply_to(msg, f"✅ MD5 đã học:
→ Kết quả: {result.upper()}")
            else:
                giai_ma, dice, total = giai_ma_md5(md5)
                gan_nhat, ratio = tim_ma_gan_nhat(md5)
                result_gan = learned_data.get(gan_nhat, "Không rõ")
                bot.reply_to(msg, f"🤖 MD5 chưa có trong tập.
"
                                  f"🧠 Dự đoán theo công thức:
→ {giai_ma} ({dice}, Tổng: {total})
"
                                  f"🔍 Gần giống với: `{gan_nhat}` ({round(ratio*100, 2)}%) → {result_gan.upper()}")
        except Exception as e:
            bot.reply_to(msg, f"Lỗi: {str(e)}")
    else:
        bot.reply_to(msg, "📌 Vui lòng nhập đúng mã MD5 (32 ký tự).")

bot.polling()
