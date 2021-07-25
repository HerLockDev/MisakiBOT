from core import SURUM

from pyrogram import Client, filters,__version__
from pyrogram.types import Message
import os, sys
from core import BOT_VER
from core.cmdhelp import CmdHelp

@Client.on_message(filters.command(['boti'], ['!','.','/']) & filters.me)
async def boti(client:Client, message:Message):
    tum_eklentiler = []
    for dosya in os.listdir("./core/plugins/"):
        if not dosya.endswith(".py") or dosya.startswith("_"):
            continue
        tum_eklentiler.append(dosya.replace('.py',''))
    lama = len(tum_eklentiler)
    acklm = "Python versiyonu:{}\nPyrogram versiyonu:{}\nBot versiyonu:{}\nEklenti sayınız:{}".format(SURUM,__version__,BOT_VER,lama)
    await message.edit(acklm)
CmdHelp("botinfo").add_command("boti", None, "Botunuz hakkında bilgi verir.").add()