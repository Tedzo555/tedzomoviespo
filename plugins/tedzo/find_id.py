import os
from datetime import datetime
from pyrogram import Client as IDBot
from pyrogram import filters
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
NEXT_TEXT = """<b><u><i>ID Features</i></u></b>
<b>✓ Sticker ID
✓ Video ID
✓ Audio ID
✓ Video Note ID
✓ Voice Note ID
✓ Photo ID
✓ Animation ID
✓ Document ID</b>
"""
BACK_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('« Back', callback_data='start')
        ]
    ]
)

@IDBot.on_message(filters.private & filters.command("id"))
async def id_handler(bot, update):
    message=update
    if message.reply_to_message:
        if message.reply_to_message.sticker:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐈𝐃 :-**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
        if message.reply_to_message.photo:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐏𝐡𝐨𝐭𝐨 𝐈𝐃 :-**  \n `{message.reply_to_message.photo.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.photo.file_unique_id}`", quote=True)
        if message.reply_to_message.video:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐕𝐢𝐝𝐞𝐨 𝐈𝐃 :-**  \n `{message.reply_to_message.video.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.video.file_unique_id}`", quote=True)
        if message.reply_to_message.animation:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐀𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧 𝐈𝐃 :-**  \n `{message.reply_to_message.animation.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.animation.file_unique_id}`", quote=True)
        if message.reply_to_message.audio:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐀𝐮𝐝𝐢𝐨 𝐈𝐃 :-**  \n `{message.reply_to_message.audio.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.audio.file_unique_id}`", quote=True)
        if message.reply_to_message.video_note:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐕𝐢𝐝𝐞𝐨 𝐍𝐨𝐭𝐞 𝐈𝐃 :-**  \n `{message.reply_to_message.video_note.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.video_note.file_unique_id}`", quote=True)
        if message.reply_to_message.voice:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐕𝐨𝐢𝐜𝐞 𝐈𝐃 :-**  \n `{message.reply_to_message.voice.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.voice.file_unique_id}`", quote=True)
        if message.reply_to_message.document:
           await message.reply(f"**𝐘𝐨𝐮𝐫 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭 𝐈𝐃 :-**  \n `{message.reply_to_message.document.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.document.file_unique_id}`", quote=True)
    else:
        await update.reply_text(        
            text=f"🆔 𝚈𝚘𝚞𝚛 𝙸𝙳 :- `{update.from_user.id}`",
            disable_web_page_preview=True,
            reply_markup=BUTTON_1
        )
@IDBot.on_message(filters.group & filters.command("id"))
async def id_handler(bot, update):
    await update.reply_text(        
        text=f"**🆔 𝚈𝚘𝚞𝚛 𝙸𝙳 :-** `{update.from_user.id}`\n\n**💬 𝚃𝚑𝚒𝚜 𝙲𝚑𝚊𝚝 𝙸𝙳 :-** `{update.chat.id}`",
        disable_web_page_preview=True,
        reply_markup=BUTTON_1
    )
@IDBot.on_message(filters.private & filters.command("info"))
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
@IDBot.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    tmp = await msg.reply(text="`please wait...`", quote=True)
    if msg.forward_from:
        text = "<u>𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>🤖 𝐁𝐨𝐭 𝐈𝐧𝐟𝐨</u>"
        else:
            text += "<u>👤𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨</u>"
        text += f'\n\n👨‍💼 𝐍𝐚𝐦𝐞 : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n🔗 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 𝐈𝐃 : `{msg.forward_from["id"]}`'
        pfp = await motech.get_profile_photos(msg.forward_from["id"])
        if not pfp:
            await tmp.edit(text, reply_markup=BUTTON_1)
        else:
            await tmp.delete()
            dls = await motech.download_media(pfp[0]["file_id"], file_name=f"{msg.chat.id}.png")
            await msg.reply_photo(
                photo=dls,
                caption=text,
                reply_markup=BUTTON_1,
                quote=True
            )
            os.remove(dls)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await tmp.edit(
                f"❌️𝐄𝐫𝐫𝐨𝐫 <b><i>{hidden}</i></b> ❌️𝐄𝐫𝐫𝐨𝐫",
            )
        else:
            text = f"<u>𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 👀</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ 𝐆𝐫𝐨𝐮𝐩</u>"
            text += f'\n\n📃 𝐍𝐚𝐦𝐞 {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n➡️ 𝐅𝐫𝐨𝐦 : @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 𝐈𝐃 : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 𝐈𝐃 `{msg.forward_from_chat["id"]}`\n\n'
            await tmp.edit(text, reply_markup=BUTTON_1)
