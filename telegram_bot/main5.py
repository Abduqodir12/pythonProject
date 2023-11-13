from aiogram import Bot, executor, Dispatcher, types
from text import kurs

API_key = "bb2e134333b0372b457c0b73"
token = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Salom, men dollar kursi bilan tanishtiradigan botman\n"
                         "/dollar")


@dp.message_handler(commands="dollar")
async def dollar(message: types.Message):
    await message.answer(f"Bugungi dollar kursi {kurs}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)