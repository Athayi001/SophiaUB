from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from Sophia import SophiaVC
from config import OWNER_ID as OWN
from pyrogram import filters
import asyncio
import os
import requests
import wget
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
import yt_dlp
from pytgcalls.types import MediaStream


flex = {}
chat_watcher_group = 3

ydl_opts = {
    "format": "low",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}


@bot.on_message(filters.command("play", prefixes=HANDLER) & filters.user(OWN))
async def play(_, message):
    if len(message.text.split()) <2:
        await message.reply("Give a song name to search it")
        return
    query = " ".join(message.command[1:])
    m = await message.reply("🔄 Searching....")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:4000]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        await m.edit(
            "⚠️ No results were found. Make sure you typed the information correctly"
        )
        print(str(e))
        return
    await m.edit("📥 Downloading...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.delete()
        await message.reply_photo(photo=thumb_name, caption=f"Started playing: {title}")
        await SophiaVC.play(message.chat.id, MediaStream(path))
        
    except Exception as e:
        await m.edit(f"**Error:**{e} ")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
