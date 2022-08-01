import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch




@Client.on_message(filters.command(["ytsearch"]))
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/ytsearch needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=10).to_dict()
        i = 0
        text = ""
        while i < 10:
            text += f"✏️**Title** - {results[i]['title']}\n"
            text += f"⌚**Duration** - {results[i]['duration']}\n"
            text += f"👁️‍🗨️**Views** - {results[i]['views']}\n"
            text += f"💻**Channel** - {results[i]['channel']}\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
