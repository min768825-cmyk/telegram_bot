import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Logging setup (Bot ရဲ့ အခြေအနေကို စစ်ဆေးဖို့)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# သင့်ရဲ့ Token
TOKEN = '8589094676:AAE0-Aod4jjm991tHuRwPRBdl96hD7WMpi8'

# /start လို့ ရိုက်ရင် ပြန်မယ့်စာ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="မင်္ဂလာပါ! ကျွန်တော်က GitHub နဲ့ Koyeb မှာ Run ထားတဲ့ Bot ပါ။ အခု အလုပ်လုပ်နေပါပြီခင်ဗျာ။"
    )

# ရိုးရိုးစာရိုက်ရင် ပြန်မယ့်စာ (Echo)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f"သင်ပို့တဲ့စာက: {user_text}"
    )

if __name__ == '__main__':
    # Bot ကို စတင်ခြင်း
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handler များ ထည့်သွင်းခြင်း
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    # Bot ကို စတင် Run ခြင်း
    application.run_polling()
