from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("ꜱᴇɴꜱᴇɪ 🥀", "https://t.me/Kexx_XD"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/STORM_CHATZ"),
    ],
    [
        Button.url(
            "ɢʀᴏᴜᴘ 🧸", "https://t.me/FriendCastel"
        ),
    ],
    [
        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "https://github.com/VARC9210/STORM"),
        Button.url("ᴄʜᴀɴɴᴇʟ ☁️", "https://t.me/STORM_TECHH"),
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ 🥀{event.sender.first_name}❤️**\n\n**ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n"
        TEXT += f"➖➖➖➖➖➖➖➖➖➖➖\n"
        TEXT += f"» **ꜱᴇɴꜱᴇɪ 🫂: [⏤͟͞〲ᴋᴇx](https://t.me/kexx_xd)**\n"
        TEXT += f"» **ꜱᴛᴏʀᴍ ⚙️:** `3.0` \n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ 🐍:** `3.11` \n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ 🔰:** `{event.client.__version__}`\n➖➖➖➖➖➖➖➖➖➖➖"
        await event.client.send_file(
                    event.chat_id,  
                    "https://graph.org/file/7f4da811955cc9c3c763f.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
