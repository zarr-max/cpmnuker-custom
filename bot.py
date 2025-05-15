from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from cpmnuker import CPMNuker

sessions = {}

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /login <username> <password>")
        return

    username = context.args[0]
    password = context.args[1]

    nuker = CPMNuker()
    result = nuker.login(username, password)

    if "token" in result:
        sessions[update.effective_user.id] = nuker
        await update.message.reply_text("Login berhasil!")
    else:
        await update.message.reply_text(f"Gagal login: {result}")

async def change_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nuker = sessions.get(update.effective_user.id)
    if not nuker:
        await update.message.reply_text("Login dulu pakai /login")
        return

    if len(context.args) < 1:
        await update.message.reply_text("Usage: /changeid <new_id>")
        return

    new_id = context.args[0]
    result = nuker.change_id(new_id)
    await update.message.reply_text(str(result))

async def set_money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nuker = sessions.get(update.effective_user.id)
    if not nuker:
        await update.message.reply_text("Login dulu pakai /login")
        return

    if len(context.args) < 1:
        await update.message.reply_text("Usage: /money <jumlah>")
        return

    amount = int(context.args[0])
    result = nuker.set_money(amount)
    await update.message.reply_text(str(result))

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nuker = sessions.get(update.effective_user.id)
    if not nuker:
        await update.message.reply_text("Login dulu pakai /login")
        return

    result = nuker.ban_account()
    await update.message.reply_text(str(result))

def main():
    # Ganti token ini dengan token bot kamu
    BOT_TOKEN = "PASTE_TOKEN_BOT_KAMU_DI_SINI"

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("login", login))
    app.add_handler(CommandHandler("changeid", change_id))
    app.add_handler(CommandHandler("money", set_money))
    app.add_handler(CommandHandler("ban", ban))

    app.run_polling()

if __name__ == "__main__":
    main()
