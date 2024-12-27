from subprocess import getoutput as r
from pyrogram import Client
from Sophia import *
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

a = r("ls Sophia/plugins").split('\n')
help_data = {'safe': 'hey'}
help_names = ['safe']
for x in a:
    if x.endswith('.py') and not x.startswith('__pycache__'):
        try:
            module = __import__(f"Sophia.plugins.{x.replace('.py', '')}", fromlist=["MOD_NAME", "MOD_HELP"])
            if hasattr(module, 'MOD_NAME') and hasattr(module, 'MOD_HELP'):
                help_data[module.MOD_NAME] = module.MOD_HELP
                help_names.append(module.MOD_NAME)
        except:
            pass
logging.info(f"{f'Loaded Modules: {help_names}' if help_names else 'No modules loaded'}")

@SophiaBot.on_inline_query()
async def showcommands(_, query):
    buttons = []
    row = []
    for i, cmd in enumerate(help_names):
        buttons.append(InlineKeyboardButton(cmd, callback_data=f"help: {cmd}"))
        
    reply_markup = InlineKeyboardMarkup(buttons)

    InlineQueryResultArticle(
        title="Help",
        input_message_content=InputTextMessageContent("Here are the available commands:"),
        reply_markup=reply_markup
    )
