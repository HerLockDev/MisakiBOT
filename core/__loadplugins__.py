from pyrogram import Client, filters
from pyrogram.types import Message
from core import thor
import importlib
import traceback
async def load_plugins():
    
    for dosya in await thor.iter_history(chat_id="me"):
        eklenti_dizini = f"./core/plugins/{dosya.file_name}"
        
        if dosya.document:
            try:
                await Client.download_media(file_name=f"./core/plugins/{dosya.file_name}")
                try:
                    spec = importlib.util.spec_from_file_location(eklenti_dizini, eklenti_dizini)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                except Exception as e:
                    traceback.print_exc()
            except Exception as hata:
                traceback.print_exc()
