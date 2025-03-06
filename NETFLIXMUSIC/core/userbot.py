from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="BABYAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Beats_Support")
                await self.one.join_chat("Netflix_Music_Support")
            except Exception as e:
                LOGGER(__name__).warning(f"Assistant failed to join support chats: {e}")
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).warning(
                    "Assistant couldn't send message to log group. Check permissions!"
                )
            me = await self.one.get_me()
            self.one.id = me.id
            self.one.name = me.mention
            self.one.username = me.username
            assistantids.append(me.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

    async def join_assistant(self, chat_id):
        """Ensures the assistant is in the group before playing music."""
        if not self.one.is_connected:
            await self.one.start()
        try:
            await self.one.join_chat(chat_id)
        except Exception as e:
            LOGGER(__name__).error(f"Failed to join assistant in chat {chat_id}: {e}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
