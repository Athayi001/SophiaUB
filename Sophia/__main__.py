import threading
from Sophia import *
from pyrogram import Client, filters
import os
from pyrogram import idle
from subprocess import getoutput as run
from Restart import restart_program

PWD = f"{os.getcwd()}/"
my_id = None

if __name__ == "__main__":
    Sophia.start()
    Sophia.send_photo(
        'me',
        photo="https://i.imgur.com/DuoscLX.jpeg",
        caption=(
            f"**✅ Sophia started ⚡**\n\n"
            f"**👾 Version:** {MY_VERSION}\n"
            f"**🥀 Python:** 3.12\n"
            f"**🐬 Owner:** {Sophia.me.first_name if not Sophia.me.last_name else f'{Sophia.me.first_name} {Sophia.me.last_name}'}\n"
            f"**🦋 Join:** __@Hyper_speed0 & @FutureCity005__"
        )
    )
    SophiaBot.start()
    idle()
