from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")
    FSUB = getenv("approvebotfree")
    CHID = int(getenv("1732001513"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
