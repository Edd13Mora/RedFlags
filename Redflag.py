import sys
import requests
import telegram
from datetime import date, timedelta
import asyncio
import tracemalloc
tracemalloc.start()

today = date.today()
one_day_ago = str(today - timedelta(days=1))

WEBSITE_URL = "https://red.flag.domains/posts/" + one_day_ago
print(WEBSITE_URL)

# Replace <YOUR_BOT_TOKEN> with your Telegram bot token
bot = telegram.Bot(token='##############################')
# Replace <CHAT_ID> with the ID of the chat you want to send the message to
chat_id = '########'

async def check_for_word(word):
    response = requests.get(WEBSITE_URL)
    if response.status_code == 200:
        if word in response.text:
            message = f"Warning a potential domain similare to urs '{word}' was recently registred, make sure to not be victime of phishing attacks, check the source here>"
            await bot.send_message(chat_id=chat_id, text=message)
            print("Message sent to Telegram.")
        else:
            print(f"Nothing")
    else:
        print(f"Could not connect to the website {WEBSITE_URL}.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <word>")
    else:
        word = sys.argv[1]
        asyncio.run(check_for_word(word))
