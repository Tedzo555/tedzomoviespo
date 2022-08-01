import os
from datetime import datetime 
from pyrogram import filters, Client
from pyrogram.types import User, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.raw import functions
from pyrogram.errors import PeerIdInvalid

BUTTON_1 = InlineKeyboardMarkup( [[
       InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗡𝗼𝘄 ", url="https://t.me/tzobotz")
       ]]
       )
       
INFO_TEXT = """<u>💫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧</u>
 🙋🏻‍♂️ 𝐅𝐢𝐫𝐬𝐭 𝐍𝐚𝐦𝐞 : <b>{}</b>
 🧖‍♂️ 𝐒𝐞𝐜𝐨𝐧𝐝 𝐍𝐚𝐦𝐞 : <b>{}</b>
 🧑🏻‍🎓 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : <b>@{}</b>
 🆔 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐈𝐃 : <code>{}</code>
 🌌 𝐏𝐫𝐨𝐟𝐢𝐥𝐞 𝐋𝐢𝐧𝐤 : <b>{}</b>
 🌍 𝐃𝐂 : <b>{}</b>
 🎤 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : <b>{}</b>
 🤠 𝐒𝐭𝐚𝐭𝐮𝐬 : <b>{}</b>
"""
@Client.on_message(filters.private & filters.command("info"))
async def id_handler(bot, update):
    temp = await update.reply(text="`please wait...`", quote=True)
    pfp = await bot.get_profile_photos(update.from_user.id)

    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "𝐍𝐨𝐧𝐞😔"

    if not pfp:
        await temp.edit(  
            text=INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),
            disable_web_page_preview=True,
            reply_markup=BUTTON_1
        )
    else:
        dls = await bot.download_media(pfp[0]["file_id"], file_name=f"{update.from_user.id}.png")
        await temp.delete()
        await update.reply_photo(
            photo=dls,
            caption=INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),             
            quote=True,
            reply_markup=BUTTON_1
        )
        os.remove(dls)
