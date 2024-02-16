from Sophia import *
from pyrogram import Client, filters
import os
from config import DATABASE_GROUP_ID
import logging
import pyrogram
from Restart import restart_program

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

PWD = f"{os.getcwd()}/"

# RUNNING CLIENTS 
async def run_clients():
    global FILE_AVAILABLE
    await Database.start()
    app = Database
    await app.send_message(DATABASE_GROUP_ID, "Sophia started")
    async for message in app.search_messages(DATABASE_GROUP_ID, query="#CACHE_FILE", limit=1):
        file_path = f"{PWD}Data.py"
        try:
            await Database.download_media(message.document.file_id, file_name=file_path)
        except Exception:
            print("Sophia Started")
        try:
            with open(f'{file_path}', 'r') as file:
                content = file.read()
        except Exception:
            await app.send_document(DATABASE_GROUP_ID, "BQACAgUAAx0CbtjjywACeVFlz3aBLE2v1n5yNAk_3hXisF4azwACWRAAAsrIeFYIS0o5eQ56sh4E", caption="#CACHE_FILE")
            await restart_program()
        await Sophia.start()
        await pyrogram.idle()


if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        Sophia.loop.run_until_complete(run_clients())
    else:
        raise Exception("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta, Try Again")
        exit()
