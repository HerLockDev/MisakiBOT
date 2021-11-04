from core import thor, baslangic
from core.__loadplugins__ import load_plugins
from pyrogram import idle
async def run_bot():
    baslangic()
    await load_plugins()
    await thor.start()
    await idle()
    await thor.stop()

if name == '__main__':
    thor.run(run_bot())
