from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 1234567 
API_HASH = 'your_api_hash'

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
