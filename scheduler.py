import telegram
from datetime import datetime
import pytz

# Token and chat_id
TOKEN = "PASTE_YOUR_TOKEN_HERE"
CHAT_ID = 1222947235

# Bot Setup
bot = telegram.Bot(token=TOKEN)

# Tip Message
tip = """🏆 Pre-Match FT Win Tip  
🔹 Team A vs Team B  
✅ Pick: Team A FT Win  
📊 RTP: 76%  
📈 Form: WWWDW  
📊 xG: 2.1 vs 0.9  
#Hi5PremiumTips"""

# Send message with time check
now = datetime.now(pytz.timezone('Asia/Bangkok'))
if now.hour == 16 and now.minute == 0:
    bot.send_message(chat_id=CHAT_ID, text=tip)
else:
    print("⏳ Not tip time yet.")
