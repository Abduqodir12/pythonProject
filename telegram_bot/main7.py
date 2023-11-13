from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types, Bot, Dispatcher, executor
import logging



BOT_TOKEN = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)
result = ""  # global

def keyboard_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton("7"),
            KeyboardButton("8"),
            KeyboardButton("9"),
            KeyboardButton("*"))
    rkm.row(KeyboardButton("4"),
            KeyboardButton("5"),
            KeyboardButton("6"),
            KeyboardButton("/"))
    rkm.row(KeyboardButton("1"),
            KeyboardButton("2"),
            KeyboardButton("3"),
            KeyboardButton("+"))
    rkm.row(KeyboardButton("="),
            KeyboardButton("0"),
            KeyboardButton("."),
            KeyboardButton("-"))
    return rkm


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text="Kalkulator",
                         reply_markup=keyboard_button())


@dp.message_handler()
async def calculator(message: types.Message):
    global result
    if message.text.strip() == "=":
        try:
            await message.answer(f"Result is {eval(result)}")
            result = ""
        except:
            await message.answer("Xatolik bo'ldi")
            result = ""
    else:
        result += message.text.strip()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)