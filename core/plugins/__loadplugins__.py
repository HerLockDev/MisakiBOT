# PLUGIN_CHANNEL_ID kanalından pluginleri çekmeye yarayan modül ...
# Herus

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.channels import CreateChannel
import asyncio,importlib,os,sys
from core import PLUGIN_CHANNEL_ID,thor
@Client.on_message(filters.command(['loadp'], ['!','.','/']) & filters.me)
async def loadp(client:Client, message:Message):
    if PLUGIN_CHANNEL_ID is None:
        return await client.send_message(chat_id="me",message="PLUGIN_CHANNEL_ID değerini herokudan el ile girmeniz gerekmekte ...")
    async for dosya in await thor.iter_history(chat_id=PLUGIN_CHANNEL_ID):
        eklenti_dizini = f"./core/plugins/{dosya.document.file_name}"
        if dosya.document and dosya.document.file_name.split(".")[-1] == "py":
            try:
                await client.download_media(message=dosya,file_name=eklenti_dizini)
                await asyncio.sleep(2)
                try:
                    spec = importlib.util.spec_from_file_location(eklenti_dizini, eklenti_dizini)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                except Exception as e:
                    await client.send_message(chat_id = "me",message = "Plugin dosyalarından biri hatalı lütfen hatalı olanı düzelt veya sil.Hata: {e}")
                    os.remove(eklenti_dizini)
                    return
                await client.send_message(chat_id = "me",message = "PLUGIN_CHANNEL_ID'deki tüm pluginler yüklendi ...")
                try:
                    await thor.stop()
                except:
                    pass
                os.execl(sys.executable, sys.executable, *sys.argv)
                return
            except Exception as e:
                print(str(e))