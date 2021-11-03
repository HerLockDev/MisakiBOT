from pyrogram import Client, filters
from pyrogram.types import Message
import importlib
async def load_plugins():
    
    for dosya in await Client.iter_history(chat_id="me"):
        eklenti_dizini = f"./core/plugins/{dosya.file_name}"
        
        if dosya.document:
            try:
                await Client.download_media(file_name=f"./core/plugins/{dosya.file_name}")
                try:
                    spec = importlib.util.spec_from_file_location(eklenti_dizini, eklenti_dizini)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                except Exception as e:
                    print(f"{hata}'dan dolayı sonradan yüklenmiş pluginler yüklenemedi.")
            except Exception as hata:
                print(f"{hata}'dan dolayı sonradan yüklenmiş pluginler yüklenemedi.")
