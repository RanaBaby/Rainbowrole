"""Emoji

Available Commands:

.repe

   build by legend @NeoMatrix90 , if u edit it then u r gay..."""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "repe":

        await event.edit(input_str)

        animation_chars = [
            "r",
            "ra",
            "rap",
            "rape",
            "rape_",
            "rape_t",
            "rape_tr",
            "rape_tra",
            "rape_trai",
            "rape_train",
            "ape_trainπ",
            "pe_trainπππ",
            "e_trainππππ",
            "_trainπππππ",
            "trainππππππ",
            "rainπππππππ",
            "ainππππππππ",
            "inπππππππππ",
            "nππππππππππ",
            "ππππππππππ",
            "πππππππππ",
            "ππππππππ",
            "πππππππ",
            "ππππππ",
            "πππππ",
            "ππππ",
            "πππ",
            "ππ",
            "π",
            "**rApEd**",
        ]

        animation_interval = 0.7

        animation_ttl = range(45)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 45])
