from telethon.sync import TelegramClient
from myParser import parse
from models import Advices
from config import api_id, api_hash, chats
from datetime import datetime


client = TelegramClient('InvestAdviceSession', api_id, api_hash)
client.start()

for chat in chats:
    messages = client.get_messages(chat, limit=15)
    for message in messages:
        parsed = parse(message.text)
        
        if not parsed:
            continue
        
        parsed['datetime'] = message.date
        parsed['source'] = 'channel: ' + message.chat.title
        # print(parsed)
        Advices.save_new(**parsed)

Advices.save_new(
    currency="GOLD",
    operation_type="BUY",
    entry=1720,
    datetime=datetime.now(),
    stop_losses=[1710],
    take_profits=[1730],
    source="prediction"
)