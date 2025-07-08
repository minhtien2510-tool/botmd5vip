
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import re

BOT_TOKEN = '7934189123:AAEmKx_e0PKWbXKlcK5x2eEhzFbGG7ErJYs'  # ← Dán token bot của bạn ở đây

# 🔍 Hàm giải mã MD5
def giai_ma_md5(md5):
    hex8 = md5[:8]
    total = sum(int(c, 16) for c in hex8)
    return "✅ Kết quả: Tài" if total % 2 == 0 else "✅ Kết quả: Xỉu"

# 💬 Xử lý tin nhắn văn bản (MD5)
def handle_message(update, context):
    msg = update.message.text.strip()
    if len(msg) == 32 and all(c in '0123456789abcdefABCDEF' for c in msg):
        result = giai_ma_md5(msg)
        update.message.reply_text(f"🧩 Mã: `{msg}`\n{result}", parse_mode='Markdown')
    else:
        update.message.reply_text("⚠️ Vui lòng gửi đúng 1 mã MD5 (32 ký tự hex).")

# 📘 /start
def start(update, context):
    update.message.reply_text("🌠 BOT MD5 MINHH TIEEN 🌠 đã sẵn sàng!\nGửi mã MD5 để phân tích!")

# 👤 /id
def show_id(update, context):
    user_id = update.message.from_user.id
    update.message.reply_text(f"🆔 ID Telegram của bạn là: `{user_id}`", parse_mode='Markdown')

# 💡 /help
def help_command(update, context):
    help_text = (
        "🌠 *BOT MD5 MINHH TIEEN* 🌠\n"
        "🌠 *TRỢ GIÚP BOT GIẢI MÃ MD5* 🌠\n\n"
        "💾 *Danh sách lệnh:*\n"
        "👉🏿 /start – Khởi động bot\n"
        "👉🏿 /id – Hiển thị ID Telegram của bạn\n"
        "👉🏿 /help – Xem menu trợ giúp\n\n"
        "🔍 *Gửi mã MD5 (32 ký tự) để phân tích!*\n"
        "☎️ *Hỗ trợ:* [@minhtien2510](https://t.me/minhtien2510')"
    )
    update.message.reply_text(help_text, parse_mode='Markdown')

# 🚀 MAIN
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("id", show_id))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("🤖 Bot đang chạy...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()