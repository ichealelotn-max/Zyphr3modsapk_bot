from telegram import Update
from telegram.constants import ChatMemberStatus
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Bot Token
TOKEN = "8259299390:AAHpXdqWXbaxJoFhqSp2WSKEG_CPCLQqrr0"

# 📌 Channels
CH1 = -1002742660499   # Channel 1 ID
CH2 = -1003031873990   # Channel 2 ID

# 📌 Links
CH1_LINK = "https://t.me/premiumapkmodsfile"
CH2_LINK = "https://t.me/+fyMHYwW3F6FiZTNl"
INSTAGRAM = "https://www.instagram.com/mods_zyphr3?igsh=MWN2cWRrcXk4cWt3Zg=="
YOUTUBE = "https://youtube.com/@modszyphr3?si=Erx78UANHbOi9fvN"

# 👨‍💻 Admins
ADMINS = ["@Zyphr3", "@Sum48x"]

JOIN_TEXT = (
    "👋 Welcome!\n"
    "Please join BOTH channels first:\n"
    f"1) {CH1_LINK}\n"
    f"2) {CH2_LINK}\n\n"
    "👉 Join karne ke baad /start dubara bhejo."
)

async def is_member(app, chat_id, user_id):
    try:
        m = await app.bot.get_chat_member(chat_id, user_id)
        return m.status in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )
    except Exception:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ok1 = await is_member(context.application, CH1, user_id)
    ok2 = await is_member(context.application, CH2, user_id)

    if ok1 and ok2:
        text = (
            "✅ Access granted!\n\n"
            f"📺 YouTube: {YOUTUBE}\n"
            f"📷 Instagram: {INSTAGRAM}\n\n"
            f"👨‍💻 Admins: {', '.join(ADMINS)}"
        )
        await update.message.reply_text(text)
    else:
        await update.message.reply_text(JOIN_TEXT)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
