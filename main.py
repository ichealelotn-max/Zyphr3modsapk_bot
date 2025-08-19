import os, logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatMemberStatus, ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

def to_int(x):
    try:
        return int(x) if x else None
    except Exception:
        return None

CH1 = to_int(os.getenv("CHANNEL_ID_1"))
CH2 = to_int(os.getenv("CHANNEL_ID_2"))

CH1_LINK = os.getenv("CHANNEL_1_LINK", "")
CH2_LINK = os.getenv("CHANNEL_2_LINK", "")
INSTAGRAM = os.getenv("INSTAGRAM_LINK", "")
YOUTUBE = os.getenv("YOUTUBE_LINK", "")
ADMINS = [s.strip() for s in os.getenv("ADMINS", "").split(",") if s.strip()]

async def is_member(app, chat_id, user_id):
    if not chat_id:
        return True
    try:
        m = await app.bot.get_chat_member(chat_id, user_id)
        return m.status in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )
    except Exception as e:
        logging.warning(f"get_chat_member failed for {chat_id}: {e}")
        return False

def default_keyboard():
    rows = []
    if INSTAGRAM:
        rows.append([InlineKeyboardButton("📸 Instagram", url=INSTAGRAM)])
    if YOUTUBE:
        rows.append([InlineKeyboardButton("▶️ YouTube", url=YOUTUBE)])
    if CH1_LINK:
        rows.append([InlineKeyboardButton("📂 Channel 1", url=CH1_LINK)])
    if CH2_LINK:
        rows.append([InlineKeyboardButton("📂 Channel 2", url=CH2_LINK)])
    return InlineKeyboardMarkup(rows) if rows else None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ok1 = await is_member(context.application, CH1, user_id)
    ok2 = await is_member(context.application, CH2, user_id)

    if ok1 and ok2:
        text = (
            "✅ <b>Access granted!</b>\n\n"
            + (f"▶️ <b>YouTube:</b> {YOUTUBE}\n" if YOUTUBE else "")
            + (f"📸 <b>Instagram:</b> {INSTAGRAM}\n" if INSTAGRAM else "")
            + (f"\n👨‍💻 <b>Admins:</b> {', '.join(ADMINS)}" if ADMINS else "")
        )
    else:
        text = (
            "🎉 <b>Welcome!</b>\n"
            "⚠️ Pehle dono channels join karo, phir <code>/start</code> dubara bhejo.\n"
            + (f"\n1️⃣ {CH1_LINK}" if CH1_LINK else "")
            + (f"\n2️⃣ {CH2_LINK}" if CH2_LINK else "")
        )

    await update.message.reply_text(
        text,
        reply_markup=default_keyboard(),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )

def main():
    if not TOKEN:
        raise SystemExit("BOT_TOKEN missing in env")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
