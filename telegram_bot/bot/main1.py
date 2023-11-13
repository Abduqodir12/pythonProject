from aiogram import executor, types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import re
from keyboard import register, cancel
from state_code import UserState

BOT_TOKEN = "6476854116:AAGFyVSfi3v4UUymWkOWx4LPTGlwQeDylf8"
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hello guys",
                         reply_markup=register())


@dp.message_handler(Text(equals="Register"))
async def start(message: types.Message):
    await message.answer("Ismingizni kiriting",
                         reply_markup=cancel())
    await UserState.name.set()


@dp.message_handler(Text(equals="cancel"), state="*")
async def start(message: types.Message, state: FSMContext):
    await message.answer("Bekor qilindi",
                         reply_markup=register())
    await state.finish()


@dp.message_handler(state=UserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isalpha():
            data["name"] = message.text
            await message.answer("Yoshingizni kiriting")
            await UserState.next()
        else:
            await message.answer("Faqat harf kiritish mumkin")


@dp.message_handler(state=UserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data["age"] = int(message.text)
            if data["age"] > 18:
                await message.answer("Raqamingizni kiriting")
                await UserState.next()
            else:
                await message.answer("Yoshing togri kelmaydi ukam")
        except:
            await message.answer("Faqat butun raqam kiriting")


@dp.message_handler(state=UserState.phone_number)
async def add_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone_number = re.match(PHONE_REGEX, message.text)
        if phone_number:
            data["phone_number"] = message.text
            await message.answer("Rasmingizni kiriting")
            await UserState.next()
        else:
            await message.answer("Bu raqam xato")


@dp.message_handler(state=UserState.photo, content_types="photo")
async def add_photo(message: types.Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    async with state.proxy() as data:
        data['photo'] = file_id
        await state.finish()
        await bot.send_photo(chat_id=message.chat.id,
                             photo=data['photo'],
                             caption=f"Foydalanuvchini ismi {data['name']},"
                                     f"Yoshi: {data['age']},"
                                     f"Telefon raqami: {data['phone_number']}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)