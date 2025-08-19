import os
from telegram import Update
from telegram.constants import ChatMemberStatus
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Token aur channel IDs
BOT_TOKEN = "8259299390:AAHpXdqWXbaxJoFhqSp2WSKEG_CPCLQqrr0"
CH1 = -1003031873990
CH2 = -1002742660499

# 🔗 Links
INSTAGRAM_LINK = "https://www.instagram.com/mods_zyphr3?igsh=MWN2cWRrcXk4cWt3Zg=="
YOUTUBE_LINK = "https://youtube.com/@modszyphr3?si=Erx78UANHbOi9fvN"

# 📌 Join text
JOIN_TEXT = (
    "👋 Welcome!\n"
    "Please join BOTH channels first:\n"
    f"1) https://t.me/+fyMHYwW3F6FiZTNl\n"
    f"2) https://t.me/premiumapkmodsfile\n\n"
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
        await update.message.reply_text(
            f"✅ Access granted!\n\n"
            f"📌 Instagram: {INSTAGRAM_LINK}\n"
            f"📌 YouTube: {YOUTUBE_LINK}\n\n"
            "Enjoy bro 🎉"
        )
    else:
        await update.message.reply_text(JOIN_TEXT)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
