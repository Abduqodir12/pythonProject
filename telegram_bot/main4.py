from aiogram import Bot, executor, Dispatcher, types

TOKEN = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text="salom qalaysiz <b>qalin</b> <i>ingichka</i>\n"
                              "bu <a href='https://university.pdp.uz/uz'>pdp</a>",
                         parse_mode="HTML")


@dp.message_handler(commands="location")
async def send_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3238123,
                            longitude=69.2419438)


@dp.message_handler(commands="contact")
async def send_contact(message: types.Message):
    await bot.send_contact(chat_id=message.chat.id,
                           phone_number="998334530919",
                           first_name="Shohruh",
                           last_name="Abdurahmon")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)