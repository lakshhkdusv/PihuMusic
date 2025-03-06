import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NETFLIXMUSIC import LOGGER, app, userbot
from NETFLIXMUSIC.core.call import BABY
from NETFLIXMUSIC.misc import sudo
from NETFLIXMUSIC.plugins import ALL_MODULES
from NETFLIXMUSIC.utils.database import get_banned_users, get_gbanned
from NETFLIXMUSIC.plugins.tools.clone import restart_bots
from config import BANNED_USERS

async def init():
    if not config.STRING1:
        LOGGER(__name__).error("String Session not filled, please provide a valid session.")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NETFLIXMUSIC.plugins" + all_module)
    LOGGER("NETFLIXMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await BABY.start()
    
    try:
        active_call = await BABY.get_active_call()
        if not active_call:
            LOGGER("NETFLIXMUSIC").error("𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗩𝗢𝗜𝗖𝗘 𝗖𝗛𝗔𝗧 𝗕𝗘𝗙𝗢𝗥𝗘 𝗣𝗟𝗔𝗬𝗜𝗡𝗚 𝗠𝗨𝗦𝗜𝗖!")
            exit()
        await BABY.stream_call("https://envs.sh/t6W.mp4")
    except NoActiveGroupCall:
        LOGGER("NETFLIXMUSIC").error("𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁 𝗡𝗼𝘁 𝗙𝗼𝘂𝗻𝗱 𝗶𝗻 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁, 𝗔𝘁𝘁𝗲𝗺𝗽𝘁𝗶𝗻𝗴 𝘁𝗼 𝗝𝗼𝗶𝗻...")
        try:
            await userbot.join_chat(config.LOG_GROUP_ID)  # Replace with actual group ID
            await asyncio.sleep(5)  # Wait for 5 sec before retrying
            await BABY.stream_call("https://envs.sh/t6W.mp4")  # Retry streaming
        except Exception as e:
            LOGGER("NETFLIXMUSIC").error(f"Failed to Join Voice Chat: {e}")
            exit()
    except Exception as e:
        LOGGER("NETFLIXMUSIC").error(f"Voice Chat Error: {e}")
    
    await BABY.decorators()
    await restart_bots()
    LOGGER("NETFLIXMUSIC").info("CONTACT ︎ME")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NETFLIXMUSIC").info("𝗦𝗧𝗢𝗣 𝗣𝗿𝗼𝗕𝗼𝘁 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
