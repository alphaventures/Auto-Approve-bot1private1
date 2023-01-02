from os import path, getenv

class Config:
    API_ID = int(getenv("17572104"))
    API_HASH = getenv("db57dc05bff345180fa5bd0a5d74c3e0")
    BOT_TOKEN = getenv("5855874254:AAH_rUpg9PeeX-KTXZ4OD7ZTTrhyKJfeU0I")
    FSUB = getenv("approvebotfree")
    CHID = int(getenv("1732001513"))
    SUDO = list(map(int, getenv("5216753212").split()))
    MONGO_URI = getenv("mongodb+srv://ankynoda:ankynoda@cluster.sc0egiu.mongodb.net/?retryWrites=true&w=majority", "")
    
cfg = Config()
