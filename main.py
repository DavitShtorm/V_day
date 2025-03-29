import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.types import BotCommand

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "8157945109:AAHR-PwqW6BkcEKk3C4nTgI26R0MHvU0PwE"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="get", description="Get 🎁"),
    ]
    await bot.set_my_commands(commands)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    user = message.from_user
    username = user.username
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    language_code = user.language_code

    await bot.send_message('5120372573', f"User {first_name} pressed /start\n"
                                    f"ID: {user_id}\n"
                                    f"Name: {first_name} {last_name}\n"
                                    f"Username: @{username}\n"
                                    f"Language: {language_code}")
    print( "\n----------"+
           f"\nUser {first_name} pressed /start\n"+
          f"ID: {user_id}\n"+
          f"Name: {first_name} {last_name}\n"+
          f"Username: @{username}\n"+
          f"Language: {language_code}"+
           "\n----------\n")


@dp.message(Command('get'))
async def open(message: Message) -> None:
#    markup = InlineKeyboardMarkup(inline_keyboard=[
#    [
#        InlineKeyboardButton(text='firework❤️', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/firework/index.html')),
#        InlineKeyboardButton(text='heart laser💓', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/heartslaser/index.html')),
#        InlineKeyboardButton(text='electro1💗', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/electro1/index.html'))
#    ],
#    [
#        InlineKeyboardButton(text='pulse🫀', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/pulse/index.html')),
#        InlineKeyboardButton(text='love you spin💘', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/loveyouspin/index.html')),
#        InlineKeyboardButton(text='heart beat💕', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/heartbeat/index.html'))
#    ],
#    [
#        InlineKeyboardButton(text='hearts🩷', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/hearts/index.html')),
#        InlineKeyboardButton(text='love❣️', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/love/index.html'))
#    ],
#    [
#        InlineKeyboardButton(text='electro2💞', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/electro2/index.html')),
#        InlineKeyboardButton(text='love you💖', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/loveyou/index.html'))
#    ]
#])
    markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/firework/index.html')),
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/heartslaser/index.html')),
    ],
    [
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/pulse/index.html')),
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/heartbeat/index.html'))
    ],
    [
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/loveyouspin/index.html')),
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/electro1/index.html'))
    ],
    [
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/hearts/index.html')),
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/love/index.html'))
    ],
    [
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/electro2/index.html')),
        InlineKeyboardButton(text='🌹', web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/loveyou/index.html'))
    ]
])

    message_send = await message.answer(text='🌹', reply_markup=markup)

    user = message.from_user
    username = user.username
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    language_code = user.language_code
    await bot.send_message('5120372573', f"User {first_name} pressed /get\n"
                                    f"ID: {user_id}\n"
                                    f"Name: {first_name} {last_name}\n"
                                    f"Username: @{username}\n"
                                    f"Language: {language_code}")

    print( "\n----------"+
           "\nUser {first_name} pressed /get\n"+
          f"ID: {user_id}\n"+
          f"Name: {first_name} {last_name}\n"+
          f"Username: @{username}\n"+
          f"Language: {language_code}"+
           "\n----------\n")

    await asyncio.sleep(600)

    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await asyncio.sleep(1)
    except:
        pass


    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message_send.message_id)
    except:
        pass

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    global bot
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await set_commands(bot)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())