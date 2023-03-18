#(©)MR-X-MIRROR-BOTZ

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b>
╭────[ About Meh ]────⍟
│
├⍟ Meh Name : <a href=http://t.me/SheikXFileStore_bot><b>𝐒𝐡𝐞𝐢𝐤 𝐗 𝐅𝐢𝐥𝐞𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭</b></a>
├⍟ Owner : <a href=https://t.me/SheikX_TG><b>𝐒𝐡𝐞𝐢𝐤 𝐗</b></a>
├⍟ Version : MR 2.0 [ Stable ]
├⍟ Server : VPS
├⍟ Language : Python 3.10.5
├⍟ Framework : Pyrogram 2.0.97
├⍟ Developer : <a href=https://t.me/MR_X_MIRROR><b>𝐌𝐑 𝐗 𝐌𝐈𝐑𝐑𝐎𝐑</b></a>
├⍟ Powered By  : <a href=https://t.me/SheikXMoviesOffl><b>𝐒𝐡𝐞𝐢𝐤𝐗𝐌𝐨𝐯𝐢𝐞𝐬𝐎𝐟𝐟𝐥</b></a>
│
╰────[ <a href=https://t.me/SheikXMoviesOffl><b>𝐒𝐡𝐞𝐢𝐤𝐗𝐌𝐨𝐯𝐢𝐞𝐬𝐎𝐟𝐟𝐥</b></a> ]────⍟<b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
