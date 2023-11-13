#import aiogram.types.sticker
from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text
from googletrans import Translator

translator = Translator()


TOKEN = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)



#
@dp.message_handler(commands=["start","photo"])
async def start(message: types.Message):
    await message.answer(f"Xush kelibsiz {message.from_user.first_name},{message.from_user.username}")
    await message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1144982182.jpg")


@dp.message_handler(commands=["photo","start"])
async def photo(message: types.Message):
    await message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1144982182.jpg")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1144982182.jpg")

@dp.message_handler(content_types=["video","document"])
async def gif(message: types.Message):
    await message.reply("Video keldi")
    await message.reply("dakument keldi")

# @dp.message_handler(user_id=906728942)
# async def self(message: types.Message):
#     await message.answer(f"Salom Abduqodir")


@dp.message_handler(Text(contains="Salom") | Text(contains="salam"))
async def self(message: types.Message):
    await message.reply(f"Va alaykum asalom")

@dp.message_handler(Text(endswith="qalay"))
async def self(message: types.Message):
    await message.reply(f"Yaxshi")

# @dp.message_handler(aiogram.types.sticker.Sticker)
# async def self(message: types.Message):
#     await message.reply(f"Salom!")
#
# @dp.message_handler()
# async def translate(text):
#     await translator.translate(text, src="uz", dest="ru")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)