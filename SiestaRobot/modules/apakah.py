import random
from SiestaRobot.events import register
from SiestaRobot import telethn

APAKAH_STRING = ["Go and ask ur mother!!! Bitch"
                 ]


@register(pattern="^/boobs ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Hmm Horny Want a PP slash ???')
        return
    await event.reply(random.choice(APAKAH_STRING))
