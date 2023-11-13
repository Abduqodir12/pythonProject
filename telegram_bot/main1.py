import wikipedia
from aiogram import Bot, executor, Dispatcher, types

TOKEN = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

wikipedia.set_lang("uz")


# @dp.message_handler(commands="start")
# async def start(message: types.Message):
#     await message.answer("Wikipediya botiga xush kelibsiz")
#

@dp.message_handler()
async def wiki(message: types.Message):
    try:
        text = message.text
        result = wikipedia.summary(text)
        await message.answer(result)
    except:
        await message.answer("Bunaqa ma'lumot yo'q")

@dp.message_handler(commands="start")
async def retur(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(commands="foto", content_types="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1144982182.jpg")
async def photo(message: types.Message):
    await message.answer_photo(photo=photo)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

