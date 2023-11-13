from aiogram import Bot,Dispatcher, executor,types
from asd import qr_creator


TOKEN = "6055924232:AAH1q6v-7w5ubcc89yCnUhzzgDrxONYh1Xg"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def send_welcom(msg: types.Message):
    await msg.answer("Salom")

@dp.message_handler()
async def qr_create(msg: types.Message):
    id = msg.from_user.id
    qr_creator(msg.text, id)
    await msg.answer_photo(photo=open(f"{id}.png", 'br'), caption=f"{msg.text} uchun qr code")




if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)