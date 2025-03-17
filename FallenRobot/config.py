class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 5653372716
    API_HASH = "aeac46b1d123e82fe6dcb43b6a26cfae"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://postgres:Aran@123@db.bekbeutrnizdlypbnifo.supabase.co:5432/postgres"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://TaktAsahina99:TaktAsahina99@cluster0.iq3cx2j.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5653372716:AAHeOJrabkMq0oOO8DKYgrY3IhR4Xc1yabg"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5790406250  # User id of your telegram account (Must be integer)

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
