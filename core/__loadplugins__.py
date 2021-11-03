from pyrogram import Client, filters
from pyrogram.types import Message

async def load_plugins():
    for dosya in Client.iter_history("me"):
        try:
            if dosya.document:
                await Client.download_media(file_name="./core/plugins")
            else:
                break
        except Exception as hata:
            print(f"{hata}'dan dolayı sonradan yüklenmiş pluginler")