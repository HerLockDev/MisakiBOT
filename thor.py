from core import thor, baslangic
from core.__loadplugins__ import load_plugins
from pyrogram import idle

baslangic()
load_plugins()


if __name__ == '__main__':
    thor.run()
