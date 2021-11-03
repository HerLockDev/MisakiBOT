from pyrogram import Client, __version__, filters
import os, sys, platform
from dotenv import load_dotenv
from math import ceil
import time
from pyrogram.types import Message as message

print("ThorUserBot Başlatılıyor...")

def hata(yazi:str) -> None:
   print("[✗] {}".format(yazi))
def bilgi(yazi:str) -> None:
   print("[*] {}".format(yazi))
def basarili(yazi:str) -> None:
   print("[✓] {}".format(yazi))
def onemli(yazi:str) -> None:
   print("[!] {}".format(yazi))


if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    hata("""En az python 3.6 sürümüne sahip olmanız gerekir.
              Birden fazla özellik buna bağlıdır. Bot kapatılıyor.""")
    quit(1)

if  os.path.exists("ayar.env"):
    load_dotenv("ayar.env")

# Yapılandırmanın önceden kullanılan değişkeni kullanarak düzenlenip düzenlenmediğini kontrol edin.
# Temel olarak, yapılandırma dosyası için kontrol.
AYAR_KONTROL = os.environ.get("___________LUTFEN_______BU_____SATIRI_____SILIN__________", None)

if AYAR_KONTROL:
    hata("\n\tLütfen ayar.env dosyanızı düzenlediğinize emin olun /veya\n\tilk hashtag'de belirtilen satırı kaldırın..\n")
    quit(1)

API_ID          = str(os.environ.get("API_ID", str))
API_HASH        = str(os.environ.get("API_HASH", str))
STRING_SESSION  = str(os.environ.get("STRING_SESSION", str))
SESSION_ADI     = os.environ.get("SESSION_ADI", "ThorUserbot")
INDIRME_ALANI   = os.environ.get("INDIRME_ALANI", "downloads/")
HEROKU_APPNAME  = os.environ.get("HEROKU_APPNAME", str)
HEROKU_APIKEY   = os.environ.get("HEROKU_APIKEY", str)
HEROKU          = os.environ.get("HEROKU", str)

if not os.path.isdir(INDIRME_ALANI): os.makedirs(INDIRME_ALANI)

if STRING_SESSION.startswith('-') or len(STRING_SESSION) < 351:
    hata("\n\tMuhtemelen String Session Hatalı..!\n")
    quit(1)


try:
    thor        = Client(
STRING_SESSION,
api_id          = API_ID,
api_hash        = API_HASH,
plugins         = dict(root="core/plugins")
)
except ValueError:
    print("Lütfen ayar.env dosyanızı DÜZGÜNCE oluşturun!")


TEMP_AYAR = {
"AFK" : "0",
"AFK_MSG": "Ana Afk Mesajı",
"PLUGIN_MSG" : {
    "info" : {"DEVS" : "[Erenay](https://t.me/theErenay) ve [Herus](https://t.me/Herus31)"}
}}

idm = None
PATTERNS = "."
CMD_HELP = {}
CMD_HELP_BOT = {}

tum_eklentiler = []
for dosya in os.listdir("./core/plugins/"):
    if not dosya.endswith(".py") or dosya.startswith("_"):
        continue
    tum_eklentiler.append(dosya.replace('.py',''))

def baslangic() -> None:
    thor.start()
    time.sleep(1.5)
    sohbet_id = -1001246173978
    sup_id = -1001462884581
    user_bot_id = -1001443146628
    plug_id = -1001329844111
    dev_id = -1001281914458
    try:
        thor.join_chat(sohbet_id)
    except:
        pass
    try:
        thor.join_chat(sup_id)
    except:
        pass
    try:    
        thor.join_chat(user_bot_id)
    except:
        pass
    try:    
        thor.join_chat(plug_id)
    except:
        pass
    try:
        thor.join_chat(dev_id)
    except:
        pass
    for dosya in thor.iter_history("me",filters.document):
        try:
            thor.download_media(dosya)
        except Exception as hata:
            print("{hata}'dan dolayı kayıtlı mesajlardaki pluginler yüklenemedi ...")

    surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
    print(f"@{SESSION_ADI} 🍁 Python: {surum} Pyrogram: {__version__}")
    basarili(f"{SESSION_ADI} {len(tum_eklentiler)} eklentiyle çalışıyor...\n")
    thor.stop()

BOT_VER = "Beta v0.2"
SURUM = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
