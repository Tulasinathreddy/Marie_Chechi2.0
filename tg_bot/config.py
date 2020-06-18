from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 920974692  # my telegram ID
    OWNER_USERNAME = "techno0018"  # my telegram username
    API_KEY = "1186546845:AAE8eJMpEw_m9PSjDxplQHzz0j3fpF1DigI"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://crypvbke_telebot:password@localhost:3306/crypvbke_telebot'  # sample db credentials
    MESSAGE_DUMP = '-1001299813526' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [920974692]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
