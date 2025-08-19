import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatMemberStatus
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 BOT Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 📌 Channels IDs (replace with your real IDs)
CH1 = int(os.getenv("CHANNEL_ID_1", "-1003031873990"))  
CH2 = int(os.getenv("CHANNEL_ID_2", "-1002742660499"))  

# 🔗 Links
INSTAGRAM_LINK = "https://www.instagram.com/mods_zyphr3?igsh=MWN2cWRrcXk4cWt3Zg=="
YOUTUBE_LINK = "https://youtube.com/@modszyphr3?si=Erx78UANHbOi9fvN"
CHANNEL_1_LINK = "https://t.me/premiumapkmodsfile"
CHANNEL_2_LINK = "https://t.me/+fyMHYwW3F6FiZTNl"

JOIN_TEXT = (
    "⚠️ Pehle dono channels join karo:\n\n"
    f"👉 [Channel 1]({CHANNEL_1_LINK})\n"
    f"👉 [Channel 2]({CHANNEL_2_LINK})\n\n"
    "✅ Join karne ke baad /start dubara bhejo."
)

async def is_member(app, chat_id, user_id):
    try:
        member = await app.bot.get_chat_member(chat_id, user_id)
        return member.status in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ok1 = await is_member(context.application, CH1, user_id)
    ok2 = await is_member(context.application, CH2, user_id)

    if ok1 and ok2:
        keyboard = [
            [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_LINK)],
            [InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_LINK)],
            [InlineKeyboardButton("📂 Channel 1", url=CHANNEL_1_LINK)],
            [InlineKeyboardButton("📂 Channel 2", url=CHANNEL_2_LINK)]
        ]
        await update.message.reply_text(
            "🎉 Welcome! Sab links niche hain:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await update.message.reply_text(JOIN_TEXT, parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
