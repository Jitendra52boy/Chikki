import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21930924"))
API_HASH = getenv("API_HASH", "f876fdafb8c33ace535dd8fe4c708680")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7957306881:AAHx71CJepuagiO1t8qQV4M0E1tp90i2CmY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Chiiki9198:Chiiki9198@cluster0.3huk06c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 330))

# Chat id of a group forf876fdafb8c33ace535dd8fe4c708680 logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002377131698))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7120605993))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Abhimusicss/Abhi-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "stable")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/musicloger03")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/musicloger03")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFOo6wAN6oKF2-LzDegnJ9Lp2rzpIJyvpj6c0pN1k-jvvdUovcXTivbT-hzfj6vuXooOj9_TMKHf3kIfi1m6aH-FZkMb5eM69hdvK3YbxOQXa8vpmP4yDO07HJfKvzI-dVcTXH98hrzI2VI9jEHTy2ScYP8iUSswuN6F89_3irTW79RdkIcu_zFy0ySwaXn-rUA062zjcvOoQPqro_D1Dj1rizypejdVmi8Dmug556Du1W9iPmITtY4yM5ZcjGA4imj8MYTH7BqCT8Y_pMIaad85-oNhy_YhQzXBn-GkRRHnA5r8V9SopRsqABHtrAZJNucNUD3pqh86j9bXtYaUzdhiDlVDgAAAAGwP3SGAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/9eefyn.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/9eefyn.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
STATS_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/nef735.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/9eefyn.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
