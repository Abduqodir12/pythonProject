from aiogram import types, Bot, Dispatcher, executor


BOT_TOKEN = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def text(msg: types.Message):
    await msg.answer(f"Siz {msg.text} dedingiz")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)