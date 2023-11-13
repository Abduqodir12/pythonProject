from aiogram import Bot, executor, Dispatcher, types

token = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start(msg:types.Message):
    await msg.answer('Assalomu alyakum Botimizga hush kelibsiz \n'
                     '/help yaratgan odamning malumoti\n,'
                     '/info Botimizni malumotlari')


@dp.message_handler(commands=["help","contact", "lacation"])
async def help(msg: types.Message):
    await bot.send_location(chat_id=msg.chat.id,
                            latitude=41.3484574,
                            longitude=69.4301086)
    await msg.answer(f"ism sharfi {msg.from_user.full_name}\n")

    await bot.send_contact(chat_id=msg.chat.id,
                           phone_number="998798940",
                           first_name="Abduqodir",
                           last_name="Abdukarimov")

@dp.message_handler(commands="info")
async def info(msg: types.Message):
    await msg.answer(f"Token {token},\n"
                     f"name bot D7_bot\n"
                     f"link @pdp_D7bot")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)