"""Fun pligon...for @PepeB0t
\nCode by @kirito6969 , ©[Eyepatch](https://t.me/NeoMatrix90)
type `.degi` and `.nehi` to see the fun.
"""
from uniborg.util import admin_cmd
import asyncio


@borg.on(admin_cmd(pattern="degi ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in (
            "/", "#", "@", "!"):
        await event.edit("Wo")
        await asyncio.sleep(0.7)
        await event.edit("Degi")
        await asyncio.sleep(1)
        await event.edit("Tum")
        await asyncio.sleep(0.8)
        await event.edit("Ekbar")
        await asyncio.sleep(0.9)
        await event.edit("Mang")
        await asyncio.sleep(1)
        await event.edit("Kar")
        await asyncio.sleep(0.8)
        await event.edit("Toh")
        await asyncio.sleep(0.7)
        await event.edit("Dekho")
        await asyncio.sleep(1)
        await event.edit("`Wo Degi Tum Ekbar Mang Kar toh Dekho`")


@borg.on(admin_cmd(pattern="nehi"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Wo PaKkA DeGi Tu ManG KaR ToH DekH`")
    await asyncio.sleep(699)
