import os, logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatMemberStatus, ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

# ---- Bot Token ----
TOKEN = "8259299390:AAFPXiPinOA3BWuSQavjBcUrFnfNSqk2dGA"

# ---- Channel IDs ----
CH1 = -1002742660499   # Channel 1 ID
CH2 = -1003031873990   # Channel 2 ID

# ---- Links ----
CH1_LINK = "https://t.me/premiumapkmodsfile"
CH2_LINK = "https://t.me/+fyMHYwW3F6FiZTNl"
INSTAGRAM = "https://www.instagram.com/mods_zyphr3?igsh=MWN2cWRrcXk4cWt3Zg=="
YOUTUBE = "https://youtube.com/@modszyphr3"
ADMINS = ["@Zyphr3", "@Sum48x"]  # Admin usernames

# ---- Check Member ----
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

# ---- Start Command ----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ok1 = await is_member(context.application, CH1, user_id)
    ok2 = await is_member(context.application, CH2, user_id)

    if ok1 and ok2:
        keyboard = [
            [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM)],
            [InlineKeyboardButton("▶️ YouTube", url=YOUTUBE)],
            [InlineKeyboardButton("📂 Channel 1", url=CH1_LINK)],
            [InlineKeyboardButton("📂 Channel 2", url=CH2_LINK)],
            [InlineKeyboardButton("👨‍💻 Admin 1", url="https://t.me/Zyphr3")],
            [InlineKeyboardButton("👨‍💻 Admin 2", url="https://t.me/Sum48x")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "✅ Access Granted! Niche buttons use karo 👇"
    else:
        keyboard = [
            [InlineKeyboardButton("📂 Join Channel 1", url=CH1_LINK)],
            [InlineKeyboardButton("📂 Join Channel 2", url=CH2_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "⚠️ Pehle dono channels join karo, fir /start bhejo."

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML
    )

# ---- Main ----
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
