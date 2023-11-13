from aiogram import types, Bot, executor, Dispatcher
import logging
from aiogram.dispatcher.filters import Text

from keyboard import main_menu, filial_menu

BOT_TOKEN = "6476854116:AAGFyVSfi3v4UUymWkOWx4LPTGlwQeDylf8"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())


@dp.message_handler(Text(equals="🏢 Kompaniya haqida"))
async def about_company(message: types.Message):
    await message.answer_photo(photo="https://jolbors.com/media/works/991/615214f7210e6.jpg",
                               caption="""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


@dp.message_handler(Text(equals="📍 Fililallar"))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=filial_menu(),
                               caption="""EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.

Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!""")


@dp.message_handler(Text(equals="⬅️ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())


@dp.message_handler(Text(equals="Menyu"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://static.tildacdn.com/tild6333-3963-4534-b062-636331353739/14.png",
                               caption="<a href='https://evos.uz/'>Evos saytiga o'tish</a>",
                               parse_mode="HTML")
    await message.answer(text="<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a>|<a href='https://t.me/evosdeliverybot'>Telegram</a>|<a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>",
                         parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)