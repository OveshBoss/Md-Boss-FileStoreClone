# Don't Remove Credit @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import sys
import glob
import importlib
import asyncio
import logging
import logging.config
import pytz
from pathlib import Path
from datetime import date, datetime 
from aiohttp import web
from pyrogram import Client, idle, __version__
from pyrogram.raw.all import layer

from config import LOG_CHANNEL, ON_HEROKU, CLONE_MODE, PORT
from Script import script 
from TechVJ.server import web_server
from plugins.clone import restart_bots
from TechVJ.bot import StreamBot
from TechVJ.utils.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients

# Logging Configuration
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

# --- PERFORMANCE BOOST CONFIG ---
# Humne workers aur concurrent transmissions ko engine level par set kiya hai
# Taaki file bhejte hi link instant generate ho

ppath = "plugins/*.py"
files = glob.glob(ppath)

# Engine optimization for speed
StreamBot.workers = 100 # Response speed badhane ke liye
StreamBot.start()
loop = asyncio.get_event_loop()

async def start():
    print('\n')
    print('Initializing Tech VJ Bot - Super Fast Mode Enabled')
    
    bot_info = await StreamBot.get_me()
    StreamBot.username = bot_info.username
    
    # Background initialization for faster startup
    await initialize_clients()
    
    # Plugin loading optimization
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            import_path = f"plugins.{plugin_name}"
            spec = importlib.util.spec_from_file_location(import_path, Path(f"plugins/{plugin_name}.py"))
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules[import_path] = load
            print(f"Tech VJ Boosted => {plugin_name}")

    if ON_HEROKU:
        asyncio.create_task(ping_server())

    # Timezone & Formatting
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    today = date.today()
    time = now.strftime("%H:%M:%S %p")

    # Web Server Startup
    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, "0.0.0.0", PORT).start()

    # Small Caps Restart Notification
    # script.RESTART_TXT should already be in small caps from our previous step
    await StreamBot.send_message(
        chat_id=LOG_CHANNEL, 
        text=script.RESTART_TXT.format(today, time)
    )

    if CLONE_MODE:
        asyncio.create_task(restart_bots()) # Tasking mode for non-blocking speed

    print("Bot Started Powered By @VJ_Bots - Optimized for OveshBoss")
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')
