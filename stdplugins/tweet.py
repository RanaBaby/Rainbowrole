# By @kirito6969 for PepeBot
# Don't edit credits Madafaka
"""Commands:\n
`.dtrump`
`.imodi`
`.kanna`
`.mind`
`.tweet`
`.carry`
`.ph`"""

import os
from asyncio import sleep

import requests
from html_telegraph_poster.upload_images import upload_image
from PIL import Image

from uniborg import MODULE, deEmojify, phss
from uniborg.util import admin_cmd, edit_or_reply

MODULE.append("tweet")


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
    return user_obj


async def purge():
    try:
        os.system("rm -rf *.png")
        os.system("rm -rf *.webp")
    except OSError:
        pass


@borg.on(admin_cmd(pattern="dtrump ?(.*)"))
async def trumptweet(event):
    args = event.pattern_match.group(1)
    if not args and not event.reply_to_msg_id:
        await event.edit("`Give some text to Doland Trump`")
        await sleep(3)
        await event.delete()
        return
    if not args:
        rep = await event.get_reply_message()
        args = rep.text
    await event.edit("`Trump Tweeting...`")
    args = deEmojify(args)
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={args}"
    ).json()
    meow = r.get("message")
    if not meow:
        return await event.edit("`Trump not found. He ran away :)`")
    await event.client.send_file(
        event.chat_id, file=meow, reply_to=event.reply_to_msg_id
    )
    await sleep(2)
    await event.delete()


@borg.on(admin_cmd(pattern="mind ?(.*)"))
async def changemymind(e):
    args = e.pattern_match.group(1)
    if not args and not e.reply_to_msg_id:
        await e.edit("`Give some text to change_your_min`")
        await sleep(3)
        await e.delete()
        return
    if not args:
        rep = await e.get_reply_message()
        args = rep.text
    await e.edit("`Creating Banner...`")
    args = deEmojify(args)
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={args}"
    ).json()
    wew = r.get("message")
    if not wew:
        return await e.edit("`Can't able to change Mind :(`")
    await e.client.send_file(e.chat_id, file=wew, reply_to=e.reply_to_msg_id)
    await sleep(2)
    await e.delete()


@borg.on(admin_cmd(pattern="kanna ?(.*)"))
async def kannagen(e):
    args = e.pattern_match.group(1)
    if not args and not e.reply_to_msg_id:
        await e.edit("`Give some text to Kanna`")
        await sleep(5)
        await e.delete()
        return
    if not args:
        rep = await e.get_reply_message()
        args = rep.text
    args = deEmojify(args)
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={args}"
    ).json()
    kk = r.get("message")
    if not kk:
        return await e.edit("`Nothing found from the API`")
    await e.edit("`Kanna is writing your text`")
    await e.client.send_file(e.chat_id, file=kk, reply_to=e.reply_to_msg_id)
    await sleep(2)
    await e.delete()


@borg.on(admin_cmd(pattern="imodi ?(.*)"))
async def trumptweet(event):
    args = event.pattern_match.group(1)
    if not args and not event.reply_to_msg_id:
        await event.edit("`Give some text to Modi Bish!`")
        await sleep(5)
        await event.delete()
        return
    if not args:
        replied = await event.get_reply_message()
        args = replied.text
    args = deEmojify(args)
    k = f"https://nekobot.xyz/api/imagegen?type=tweet&text={args}&username=narendramodi"
    r = requests.get(k).json()
    meow = r.get("message")
    if not meow:
        return await event.edit("`Modi not found. He ran away :)`")
    await event.edit("`Modi is Tweeting`")
    await event.client.send_file(
        event.chat_id, file=meow, reply_to=event.reply_to_msg_id
    )
    await sleep(2)
    await event.delete()


@borg.on(admin_cmd(pattern="tweet ?(.*)"))
async def nekobot(cat):
    kk = cat.pattern_match.group(1)
    replied = await cat.get_reply_message()
    query = kk
    if replied:
        text = replied.message
        username = query
    elif "|" in query:
        text, username = query.split("|")
    if replied and not query:
        await cat.edit("`Give username when replying to a message :(`")
        return
    if not replied and not query:
        await cat.edit("`Give me some text :(. Use .tweet message | username`")
        return
    try:
        await cat.edit(f"`Requesting {username} to tweet...`")
        text = deEmojify(text)
        catfile = await tweets(text, username)
        await borg.send_file(cat.chat_id, file=catfile, reply_to=cat.reply_to_msg_id)
        await cat.delete()
    except Exception as e:
        await cat.edit(str(e))


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    pepe = r.get("message")
    if not pepe:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(pepe).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


@borg.on(admin_cmd(pattern="carry ?(.*)"))
async def trumptweet(event):
    args = event.pattern_match.group(1)
    if not args and not event.reply_to_msg_id:
        await event.edit("`Give some text to Carry Bish` ????")
        await sleep(5)
        await event.delete()
        return
    if not args:
        replied = await event.get_reply_message()
        args = replied.text
    args = deEmojify(args)
    k = f"https://nekobot.xyz/api/imagegen?type=tweet&text={args}&username=CarryMinati"
    r = requests.get(k).json()
    meow = r.get("message")
    if not meow:
        return await event.edit("`Carryminati not found. He iz Busy :)`")
    await event.edit("`Carry Minati is Tweeting for You` ????")
    await event.client.send_file(
        event.chat_id, file=meow, reply_to=event.reply_to_msg_id
    )
    await sleep(2)
    await event.delete()


@borg.on(admin_cmd(pattern=r"ph(?: |$)(.*)", allow_sudo=True))
async def phcomment(event):
    try:
        a = await edit_or_reply(event, "`Proccessing..`")
        text = event.pattern_match.group(1)
        reply = await event.get_reply_message()
        if reply:
            user = await get_user_from_event(event)
            if user.last_name:
                name = user.first_name + " " + user.last_name
            else:
                name = user.first_name
            text = text if text else str(reply.message)
        elif text:
            user = await bot.get_me()
            if user.last_name:
                name = user.first_name + " " + user.last_name
            else:
                name = user.first_name
            text = text
        else:
            return await a.edit("`Gib text Bish!`")
        try:
            photo = await event.client.download_profile_photo(
                user.id,
                str(user.id) + ".png",
                download_big=False,
            )
            uplded = upload_image(photo)
        except BaseException:
            uplded = "https://telegra.ph/file/7d110cd944d54f72bcc84.jpg"
    except BaseException as e:
        await purge()
        return await a.edit(f"Error: `{e}`")
    img = await phss(uplded, text, name)
    try:
        await event.client.send_file(
            event.chat_id,
            img,
            reply_to=event.reply_to_msg_id,
        )
    except BaseException:
        await purge()
        return await a.edit("`Reply message has no text!`")
    await a.delete()
    await purge()
