#coded by @theErenay
#@ThorUserBot

from os import isatty
from core import TEMP_AYAR, idm
from core.cmdhelp import CmdHelp

from pyrogram import Client, filters
from pyrogram.types import Message
AFK_MSG = False
@Client.on_message(filters.command(['afk'], ['!','.','/']) & filters.me)
async def afk(client:Client, message:Message):
    global AFK_MSG
    #------------------------------------------------------------- Başlang >
    girilen_yazi = message.text
    AFK_MSG = girilen_yazi[5:]

    msg = "**Artık AFK'yım!**"
    if TEMP_AYAR["AFK"]:
        msg = "**Şu an AFK Değilim!**"
        TEMP_AYAR["AFK"] = False
        AFK_MSG = False
        await message.edit(msg)
    else:
        TEMP_AYAR["AFK"] = True
        if AFK_MSG:
            await message.edit(msg + f"\n`Sebep:` {AFK_MSG}")
        else:
            await message.edit(msg + f"\n`Sebep: {TEMP_AYAR['AFK_MSG']}`")

@Client.on_message(filters.incoming & ~filters.bot & ~filters.private) 
async def on_tag(_,m):                                                                              async def on_tag(_, m):
    msg = "Şu an AFK'yım!"
    mentioned = m.mentioned
    rep_m = m.reply_to_message
    if mentioned or rep_m and rep_m.from_user and rep_m.from_user.id == idm:
        if TEMP_AYAR["AFK"]:

            await m.reply(msg + f"\n`Sebep:` {TEMP_AYAR['AFK_MSG']}")

@Client.on_message(filters.incoming & ~filters.bot & filters.private)
async def on_pm(client:Client, message:Message):
    msg = "**Şu an AFK'yım!**"
    if TEMP_AYAR["AFK"]:
        if not AFK_MSG:
            await message.reply(msg + "\n`Sebep:` " + TEMP_AYAR["AFK_MSG"], reply_to_message_id = message.message_id)
        else:
            await message.reply(msg + "\n`Sebep:` " + AFK_MSG, reply_to_message_id = message.message_id)

@Client.on_message(filters.outgoing)
async def on_me(client:Client, message:Message):
    if TEMP_AYAR["AFK"]:
        global AFK_MSG
        msg = "**Şu an AFK Değilim!**"
        TEMP_AYAR["AFK"] = False
        AFK_MSG = False
        await client.send_message(message.chat.id,  msg)

CmdHelp("afk").add_command("afk", "<İsteğe bağlı sebep>", "AFK olduğunuzu belirtir.", "afk uyuyor").add_command("unafk", None, "AFK modunu kapatır.").add()
