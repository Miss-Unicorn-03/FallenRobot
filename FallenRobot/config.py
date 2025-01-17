class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27766384
    API_HASH = "7d610db1d9127ad2bd32a954d9929b36"

    CASH_API_KEY = "4QEPLUTA5QS5ULWJ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = (1814077328)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = ""  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/577f6addfd98b67129d70.jpg"

    SUPPORT_CHAT = "miss_unicorn_world"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5695336080:AAFugd_beEtQeuZb6p5gQY9yN8NyPJu4b3E"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 2093770411 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
