"""Emoji

Available Commands:
click gift as soon as fast as possible
.game

build by legend @r4v4n4 , if u edit it then u r gay..."""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "game":

        await event.edit(input_str)

        animation_chars = [
            "**Welcome To PepeBot Repo Game**",
            "**Click The Gift As Fast As Possible**",
            "**Game Starts in 3**",
            "**Game Starts in 2**",
            "**Game Starts in 1**",
            "ššššššš\nššššššš\nššššššš\nššššššš\nšššššš\nšššššš\nššššššš",
            "ššššššš\nššššššš\nššššššš\nššš[š](https://github.com/ravana69/PornHub/)ššš\nšššššš\nššššššš\nššššššš",
            "šššššš\nšššššš\nššššššš\nššššššš\nšššš[š](https://github.com/ravana69/PornHub/)šš\nššššššš\nššššššš",
            "ššššššš\nššššššš\nš[š](https://github.com/ravana69/PornHub/)ššššš\nšššššš\nššššššš\nššššššš\nššššššš",
            "ššššššš\nššššššš\nššššššš\nššššššš\nššššššš\nššššš[š](https://github.com/ravana69/PornHub/)š\nššššššš",
            "ššššš\nššššššš\nššššššš\nšššššš\nššššššš\nššššššš\n[š](https://github.com/ravana69/PornHub/)šššššš",
            "ššššššš\nšššššš[š](https://github.com/ravana69/PornHub/)\nššššššš\nššššššš\nššššššš\nššššššš\nšššššš",
            "ššššššš\nššššššš\nšššššš\nššššššš\nššššššš\nšššššš\nššššššš",
            "**Game Over**" "**Now Phack Off**",
        ]

        animation_interval = 0.5

        animation_ttl = range(14)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 14])
