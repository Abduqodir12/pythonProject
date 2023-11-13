from aiogram import Bot, executor, Dispatcher, types

TOKEN = "6836097859:AAGcfDFJHTbciYFiBsTTwIxLGKerODTYJaY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text="Salom")

@dp.message_handler(commands="photo")
async def photo(msg: types.Message):
    await bot.send_photo(msg.chat.id,photo='https://avatars.mds.yandex.net/i?id=679291e72a2ff29a46e2c5f1c92fc3258a35044b-8351914-images-thumbs&n=13',
                         caption='Pdp dars jarayoni')

@dp.message_handler(commands="lacation")
async def lacation(msg: types.Message):
    await bot.send_location(chat_id=msg.chat.id,
                            latitude=41.3264751,
                            longitude=69.2259098)


@dp.message_handler(commands="contact")
async def contact(msg: types.Message):
    await bot.send_contact(chat_id=msg.chat.id,
                           phone_number='55 508 47 47',
                           first_name="PDP academiya",
                           last_name="PDP hodimlari")


@dp.message_handler(commands="video")
async def video(msg: types.Message):
    with open("https://video-preview.s3.yandex.net/RxAYMwIAAAA.mp4") as video_file:
        await bot.send_video(chat_id=msg.chat.id,
                         video=video_file,caption='Pdp ni videosi')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)