"""Command: .tagall optional_text_to_tag_in
You can use it in reply to a message or directly in a new message."""
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="tagall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    try:
        mentions = event.pattern_match.group(1)
    except Exception:
        mentions = "Helu, How do u do!"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 50000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        await previous_message.reply(mentions)
    else:
        await event.reply(mentions)
        await event.delete()
