from pyrogram import Client, filters
from pyrogram.types import Message
from core import thor
import importlib, traceback, asyncio

@Client.on_message(filters.command(['loadplugs'], ['!','.','/']) & filters.me)
async def load_plugins(client:Client,message:Message):
    
    async for dosya in thor.iter_history(chat_id="me"):
        eklenti_dizini = f"./core/plugins/{dosya.file_name}"
        
        if dosya.document:
            try:
                await client.download_media(file_name=eklenti_dizini,message=dosya)
                await asyncio.sleep(2)
                try:
                    spec = importlib.util.spec_from_file_location(eklenti_dizini, eklenti_dizini)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                except:
                    traceback.print_exc()
            except:
                traceback.print_exc()
