from telethon.sync import TelegramClient, events
from myParser import parse
from models import Advices
from config import api_id, api_hash, chats

client = TelegramClient('InvestAdviceSession', api_id, api_hash)

@client.on(events.NewMessage(chats=chats))
async def normal_handler(event):
    
    mess=event.message.to_dict()['message']
    mess_date=event.message.to_dict()['date']
    
    print(mess, mess_date)

    parsed = parse(mess)

    if not parsed:
        return
    
    parsed['datetime'] = mess_date
    parsed['source'] = 'channel: ' + event.message.chat.title
    # print(parsed)
    Advices.save_new(**parsed)


client.start()
client.run_until_disconnected()

