# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# --- BOT INFORMATION ---
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

PICS = (environ.get('PICS', 'https://graph.org/file/01112d7a3cb9e6fc7daba-6e30b694717486e108.jpg')).split() 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "") 
PORT = environ.get("PORT", "8080")

# --- DATABASE & CLONE INFO ---
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) 
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://bosstgbots_db_user:DiRFdWd2U9kHoP4j@cluster0.g6p3m4j.mongodb.net/?appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "techvjbotz")

# --- AUTO DELETE SETTINGS (Fast Cleanup) ---
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) 
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) 
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) 

# --- CHANNEL & LOGGING ---
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002908616515"))

# --- CAPTION CUSTOMIZATION (Small Caps) ---
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# --- PUBLIC ACCESS ---
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# --- VERIFICATION SYSTEM ---
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) 
SHORTLINK_URL = environ.get("SHORTLINK_URL", "") 
SHORTLINK_API = environ.get("SHORTLINK_API", "") 
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") 

# --- POWERFUL STREAM CONFIG (DISCLOUD FASTEST) ---
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) 
MULTI_CLIENT = True 
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '10')) 
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))

# Using DisCloud for 10x Speed than Render
# Slash (/) at the end is added to prevent DNS errors
URL = environ.get("URL", "https://discloud.app/") 

# --- PERFORMANCE BOOST SETTINGS ---
WORKERS = int(environ.get("WORKERS", "64")) # Max speed for high traffic
MAX_CONCURRENT_TRANSMISSIONS = int(environ.get("MAX_CONCURRENT_TRANSMISSIONS", "20"))

