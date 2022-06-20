iاڪتملتasyncio
from telethon import events
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest
from jmthon import jmthon

@jmthon.on(events.NewMessage(outgoing=True, pattern="^.ضيف$"))
async def get_users(event):
    legen_ = event.text[10:]
    jmthon_chat = legen_.lower
    restricted = ["@super_ioi5n", "@konan_support"]
    konan = await event.edit(f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    if jmthon_chat in restricted:
        return await ioi5n.edit(
            event, "**- لا يمكنك اخذ الاعضاء من مجموعه السورس العب بعيد ابني  :)**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await JMTHON.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    else:
        await JMTHON.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    if event.is_private:
        return await konan.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await JMTHON.edit(
        "**▾∮ حالة الأضافة:**\n\n**▾∮ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await JMTHON.edit(
                    f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await jmthon(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await JMTHON.edit(
                f"**▾∮تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await JMTHON.edit(
        f"**▾∮ سورس كونان اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`"
    )
