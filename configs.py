from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "20239261"))
    API_HASH = getenv("API_HASH", "af61dab399ed3220a3a81570b56bd29d")
    BOT_TOKEN = getenv("BOT_TOKEN", "6694252129:AAGobWHGc6XbaZwfXgAf-5NJ_u3L9SRSPvo")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "XozMovies")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1002139227512"))
    ADMIN = list(map(int, getenv("ADMIN", "1242556540 1058787811").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://evamusicbot:mrwaris04@cluster0.5ad8zuj.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002132087730"))
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    DP_PIC = os.environ.get("DP_PIC", "https://graph.org/file/67a5c787deb0d67fd3f69.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Auto_Accept_Xo_Bot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://te.legra.ph/file/ba16b6f4c78879c5d5527.jpg https://te.legra.ph/file/ba16b6f4c78879c5d5527.jpg").split()

    LOGO = """🇩 🇵 _🇧 🇴 🇹 🇿"""

dp1 = Config()
