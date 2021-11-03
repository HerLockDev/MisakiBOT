from pyrogram import Client, filters
from pyrogram.types import Message

def load_plugins():
    for dosya in Client.iter_history(chat_id="self"):
        try:
            if dosya.document:
                Client.download_media(file_name="./core/plugins")
            else:
                break
        except Exception as hata:
            print(f"{hata}'dan dolayı sonradan yüklenmiş pluginler")