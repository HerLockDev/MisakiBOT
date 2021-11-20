
from core.cmdhelp import CmdHelp
from pyrogram import Client, filters
from pyrogram.types import Message
from random import choice
    
ALIVE_MESSAGES = ["Hocam Çalışıyorum...! MisakiUserBot"]
@Client.on_message(filters.command(['alive'], ['!','.','/']) & filters.me)
async def komut(client:Client, message:Message):

    await message.edit(choice(ALIVE_MESSAGES))
CmdHelp("alive").add_command("alive", None, "Bot yaşıyor mu ona bakar.").add()
