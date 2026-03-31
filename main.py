from telethon import TelegramClient, events
import re
import asyncio

api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'

client = TelegramClient('session', api_id, api_hash)

SOURCE_CHAT = -1002155298579
TARGET_CHAT = -1003893253069

pattern = re.compile(r'https://t\.me/duckmyduck_bot\?start=\w+')
DELETE_DELAY = 12


@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    text = event.raw_text

    if not text or "duckmyduck_bot" not in text:
        return

    if "Uncommon" in text:
        emoji = "🟩"
    elif "Rare" in text:
        emoji = "🟦"
    elif "Epic" in text:
        emoji = "🟪"
    else:
        return

    link = pattern.search(text)
    if not link:
        return

    msg = f"{emoji} {link.group(0)}"

    sent = await event.client.send_message(
        TARGET_CHAT,
        msg,
        link_preview=False
    )

    await asyncio.sleep(DELETE_DELAY)

    try:
        await sent.delete()
    except:
        pass


client.start()
client.run_until_disconnected()