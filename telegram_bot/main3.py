from aiogram import Bot, Dispatcher, types, executor
from tarjima import translate
from uzbek import to_cyrillic

TOKEN ="6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    print(message)
    await message.answer(f"Assalomu alaykum {message.from_user.first_name}")

# @dp.message_handler()
# async def tarjima(message: types.Message):
#     data = translate(message.text)
#     await message.answer(data)

@dp.message_handler()
async def kiril(msg: types.Message):
    data = to_cyrillic(msg.text)
    await msg.answer(data)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)