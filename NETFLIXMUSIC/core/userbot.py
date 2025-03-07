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
        LOGGER(__name__).info("Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("NAINCY_UPDATES")
                await self.one.join_chat("RADHA_MUSIC_REBOT")
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
        """Ensures the assistant joins the group before playing music."""
        if not self.one.is_connected:
            await self.one.start()

        try:
            chat = await self.one.get_chat(chat_id)
            if chat.type in ["supergroup", "group"]:
                await self.one.join_chat(chat_id)
                LOGGER(__name__).info(f"Assistant joined {chat_id}.")
            else:
                LOGGER(__name__).warning(f"Chat {chat_id} is not a valid group.")
        except Exception as e:
            LOGGER(__name__).error(f"Failed to join assistant in chat {chat_id}: {e}")

            # Alternative: Try joining via an invite link
            try:
                invite_link = await self.one.export_chat_invite_link(chat_id)
                await self.one.join_chat(invite_link)
                LOGGER(__name__).info(f"Assistant joined {chat_id} via invite link.")
            except Exception as e:
                LOGGER(__name__).error(f"Failed to join assistant via invite link: {e}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
        except:
            pass
