# We Take This Codes From GitHub.com/Otazuki004/QuantumRobot.git
# Please Use Our QuantumRobot

from Sophia import HANDLER
from Sophia.__main__ import Sophia as bot
from config import OWNER_ID
from pyrogram import *
import asyncio
import os

video_formats = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', '3gp']
audio_formats = ['mp3', 'wav', 'ogg', 'aac', 'flac', 'wma', 'm4a']
text_formats = ['txt', 'csv', 'json', 'xml', 'html', 'md', 'pdf', 'text']
coding_languages = ['py', 'java', 'js', 'c', 'css', 'ruby', 'php', 'swift']
Image_Formats = ['jpeg', 'png', 'gif', 'tiff', 'bmp', 'webp', 'jpg']
other_formats = ['apk', 'bat', 'jar', 'iso', 'rar', '7z', 'tar.gz', 'tar.bz2', 'zip', 'tar', 'exe']

formats = [video_formats, audio_formats, text_formats, coding_languages, Image_Formats, other_formats]

@bot.on_message(filters.command("rename", prefixes=HANDLER) & filters.user(OWNER_ID)) 
def rename(_, message):
    if reply := message.reply_to_message:
        if len(message.text.split()) <2:
            return bot.send_message(message.chat.id, "Master, Please enter Text ⚠️")
        try:
            filename = message.text.replace(message.text.split(" ")[0], "")
            if not any(filename.endswith(format) for format_list in formats for format in format_list):
                message.reply_text("Master, Please enter a valid format (e.g., .mp4).")
            else:
                if reply := message.reply_to_message:
                    x = message.reply_text("`Downloading....`")
                    try:
                        path = reply.download(file_name=filename)
                    except Exception as e:
                        if str(e) == "This message doesn't contain any downloadable media":
                            x.delete()
                            message.reply_text("**Please Reply To Downloadable file 🗃️**")
                        else:
                            message.reply_text(e)
                            print(e)
                        
                    x.edit("`Uploading...`")
                    message.reply_document(path, caption=filename)
                    os.remove(path)
                    x.delete()
                else:
                    bot.send_message(message.chat.id, "**USAGE `/rename` [File Name] And Reply A media ⚡ **")
        except Exception as er:
            if str(er) == """Telegram says: [400 MESSAGE_ID_INVALID] - The message id is invalid (caused by "messages.EditMessage")""":
                return
            print(er)
            bot.send_message(message.chat.id, f"**Error: **{er}")
    else:
        bot.send_message(message.chat.id, "**Reply to a file 🗃️**")
