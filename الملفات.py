import os
import asyncio
from pathlib import Path
from jmthon import jmthon
from telethon import events

@jmthon.on(events.NewMessage(outgoing=True, pattern="^.تنصيب (.*)"))
async def install(event):
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "jmthon/plugins/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_delete(
                    event,
                    f"- تم تنصيب الملف `{os.path.basename(downloaded_file_name)}`",
                    10,
                )
            else:
                os.remove(downloaded_file_name)
                await edit_delete(
                    event, "**خـطأ اسم هذا الملـف موجود بالفعل في السورس**.", 10
                )
        except Exception as e:
            await edit_delete(event, f"**خـطأ:**\n`{e}`", 20)
            os.remove(downloaded_file_name)
