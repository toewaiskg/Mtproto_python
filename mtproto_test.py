import asyncio
from telethon import TelegramClient, events

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
# api_id = 12345
# api_hash = '0123456789abcdef0123456789abcdef'

api_id  = 49631
api_hash = 'fb050b8f6771e15bfda5df2409931569'

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    # added by mayyi
    # print((await client.get_me()).stringify())
    # await client.send_message('username', 'Hello! Talking to you from Telethon')
    # await client.send_file('username', '/home/may/Pictures/8.png')
    # await client.download_profile_photo('me')
    # messages = await client.get_messages('username')
    # await messages[0].download_media()
    # @client.on(events.NewMessage(pattern='(?i)hi|hello'))
    # async def handler(event):
    #     await event.respond('Hey!')

asyncio.run(main())

