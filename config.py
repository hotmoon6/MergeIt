import os


class Config(object):
    API_HASH = os.environ.get("9bd003806267466f904f91aa035d8991")
    BOT_TOKEN = os.environ.get("5308277473:AAHcoxK_BtfycMCCH5uu9YceCXb8pG0AxVA")
    TELEGRAM_API = os.environ.get("12581928")
    OWNER = os.environ.get("1621366244")
    OWNER_USERNAME = os.environ.get("Lucifer_v007")
    PASSWORD = os.environ.get("spidey007")
    DATABASE_URL = os.environ.get("mongodb+srv://hotmoon:hotmoon@dbformergeandmuxbot.iml6x.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001504347270")  # Add channel id as -100 + Actual ID
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle"]
