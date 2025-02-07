import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7086282398:AAHTHX-bYIuknn7JurXbKn4Vr0qcBBgTev4"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('open'))
async def open(message: Message) -> None:
    markup1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/blueheart/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/electro1/index.html')
                )             
            ]
        ]
    )
    markup2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/loveyou/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/loveyouspin/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/pulse/index.html')
                )
            ]
        ]
    )
    markup3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/hearts/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/heartslaser/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/love/index.html')
                )
            ]
        ]
    )
    markup4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/electro2/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/firework/index.html')
                ),
                InlineKeyboardButton(
                    text = 'open', 
                    web_app=WebAppInfo(url='https://davitshtorm.github.io/V_day/res/heartbeat/index.html')
                ) 
            ]
        ]
    )
    await message.answer(text='1', reply_markup=markup1)
    await message.answer(text='2', reply_markup=markup2)
    await message.answer(text='3', reply_markup=markup3)
    await message.answer(text='4', reply_markup=markup4)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())