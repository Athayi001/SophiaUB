import threading
from Sophia import *
from pyrogram import Client, filters
import os
from pyrogram import idle
from config import *
from subprocess import getoutput as r
from Restart import restart_program

PWD = f"{os.getcwd()}/"

if __name__ == "__main__":
    Sophia.start()
    SophiaBot.start()
    try:
        if 143 == 143:
            SophiaBot.send_photo(
                my_id,
                photo="https://i.imgur.com/DuoscLX.jpeg",
                caption=(
                    f"**✅ Sophia started ⚡**\n\n"
                    f"**👾 Version:** {MY_VERSION}\n"
                    f"**🥀 Python:** {r('python --version').lower().split('python ')[1]}\n"
                    f"**🐬 Owner:** {Sophia.me.first_name if not Sophia.me.last_name else f'{Sophia.me.first_name} {Sophia.me.last_name}'}\n"
                    f"**🦋 Join:** __@Hyper_speed0 & @FutureCity005__"
                )
            )
    except:
        pass
    idle()
