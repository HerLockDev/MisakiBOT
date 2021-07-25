

from core import TEMP_AYAR
from core.cmdhelp import CmdHelp

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(['info'], ['!','.','/']) & filters.me)
async def hakkbilgi(client:Client, message:Message):
    
    MESAJ = f"""
ㅤㅤㅤ⚒ Thor UserBot ⚒ㅤㅤ

🛠 Sahipler: [Erenay](https://t.me/theErenay) ve [Herus](https://t.me/Herus31)
⚔️ Geliştiriciler: {TEMP_AYAR['PLUGIN_MSG']['info']['DEVS']}
 
 ┏━━━━━━━━━━━━━━━━━━━━━
 ┣ @Thor_UB
 ┣ @ThorUbSupport
 ┣ @ThorUBChat
 ┣ @ThorUBPlugin
 ┗━━━━━━━━━━━━━━━━━━━━━
 """
    await message.edit(MESAJ)

CmdHelp("info").add_command("info", None, "Botun sahipleri, geliştiriciler ve USERBOT kanalları hakkında bilgi verir.").add()
