# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y

import asyncio
from collections import deque

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.kos", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πΆππΆππΆππΆπ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
