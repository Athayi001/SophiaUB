from Sophia import Sophia as bot
from Sophia import HANDLER
from config import OWNER_ID as OWN
from pyrogram import enums
from pyrogram import filters
from pyrogram.types import *
import asyncio

async def is_admin(chat_id: int, user_id: int):
    chat_members = await bot.get_chat_members(chat_id)
    for member in chat_members:
        if member.user.id == user_id:
            return member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.CREATOR]
    return False

@bot.on_message(filters.command("unbanall", prefixes=HANDLER) & filters.user(OWN))
async def unbanall(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if user_id != OWN and (await is_admin(chat_id, user_id)) == False:
        return
    elif message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("Sorry, This Command Only works in Groups!")
    else:
        try:
            BANNED = []
            unban = 0
            async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
                BANNED.append(m.user.id)
                try:
                    await bot.unban_chat_member(chat_id, m.user.id)
                    unban += 1
                except: pass
                await asyncio.sleep(0.8)
            await message.reply("Found Banned Members: {}\nUnbanned Successfully: {}".format(len(BANNED), unban))
        except Exception as e:
            if "CHAT_ADMIN_REQUIRED" in str(e):
                return await message.reply_text("**Sorry**, `I don't have Admin rights to do this!. ❌`")
            await message.reply_text(f"**Error:** {e}")
            print(e)

@bot.on_message(filters.command("banall", prefixes=HANDLER) & filters.user(OWN))
async def banall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id != OWN and (await is_admin(chat_id, user_id)) == False:
        return
    elif message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This Command Only works in Groups!")
    else:
        try:
            Members = []
            Admins = []
            async for x in bot.get_chat_members(chat_id):
                if not x.privileges:
                    Members.append(x.user.id)
                else:
                    Admins.append(x.user.id)
            for user_id in Members:
                if message.text.split()[0].lower().startswith("s"):
                    m = await bot.ban_chat_member(chat_id, user_id)
                    await m.delete()
                else:
                    await bot.ban_chat_member(chat_id, user_id)
            await message.reply_text("Successfully Banned: {}\nRemaining Admins: {}".format(len(Members), len(Admins)))
        except Exception as e:
            if "400 CHAT_ADMIN_REQUIRED" in str(e):
                return await message.reply_text("You don't have enough admin rights to do this 🚫")
            await message.reply_text(f"**Error:** {e}")
            print(e)

@bot.on_message(filters.command("kickall", prefixes=HANDLER) & filters.user(OWN))
async def kickall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id != OWN and (await is_admin(chat_id, user_id)) == False:
        return
    elif message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("This Command Only works in Groups!")
    else:
        try:
            Members = []
            Admins = []
            async for x in bot.get_chat_members(chat_id):
                if not x.privileges:
                    Members.append(x.user.id)
                else:
                    Admins.append(x.user.id)
            for user_id in Members:
                if message.text.split()[0].lower().startswith("s"):
                    m = await bot.ban_chat_member(chat_id, user_id)
                    await bot.unban_chat_member(chat_id, user_id)
                    await m.delete()
                else:
                    await bot.ban_chat_member(chat_id, user_id)
                    await bot.unban_chat_member(chat_id, user_id)
            await message.reply_text("Successfully Kicked: {}\nRemaining Admins: {}".format(len(Members), len(Admins)))
        except Exception as e:
            if "CHAT_ADMIN_REQUIRED" in str(e):
                return await message.reply_text("You don't have enough admin rights to do this 🚫")
            await message.reply_text(f"**Error:** {e}")
            print(e)

MOD_NAME = 'Bans'
MOD_HELP = """**⚕️ Banall**
.banall - To ban all members from a group.
.unbanall - To unban all members from a group.
.kickall - To kick all members from a group.

**🥀 Normal-Ban**
.ban <Reply/id> - To ban them.
.kick <Reply/id> - To kick them.
.unban <Reply/id> - To unban them.
**💡 LMAO:** Don't try to test this and destroy your group!
"""
