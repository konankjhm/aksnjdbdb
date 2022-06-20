import sys
from os import execl
from telethon import events
from konan konan konan

@ioi5n.on(events.NewMessage(outgoing=True, pattern="^.اعادة تشغيل$"))
async def _(event):
    await event.edit("جار أعادة التشغيل انتظر دقيقه")
    await jmthon.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)
