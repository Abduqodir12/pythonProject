from aiogram import types, Bot, executor, Dispatcher
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboard import main_menu, filial_menu, nain_menu, kain_menu, gain_menu, fain_menu, qain_menu, pain_menu, lain_menu, wain_menu, cain_menu
from keyboard import register, cancel
from state_code import UserState



BOT_TOKEN = "6608141145:AAHRM59PeN6XNdMt-wD51G62TxLr5EJAbKA"
bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
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

@dp.message_handler(Text(equals="🗣 Yangiliklar"))
async def tell(message: types.Message):
    await message.answer("""Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")


@dp.message_handler(Text("📞 Kontaktlar/Manzil"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
📌Ориентир: MAKRO THE TOWER""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=69.275948,
                            longitude=41.287978)



@dp.message_handler(Text(equals="☕️ Yaqin filiallarni ko'rsatish"))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=nain_menu())


@dp.message_handler(Text(equals="🔙 Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=filial_menu())

@dp.message_handler(Text("🏢 Bosh ofis"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""📍Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.
📌Ориентир: MAKRO THE TOWER""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3022159,
                            longitude=69.2486216)


@dp.message_handler(Text(equals="Toshkent sh."))
async def start(message: types.Message):
    await message.answer_photo(photo="https://storage.kun.uz/source/7/mZbBFi6Wa8kI4W_BCpz1CbMWWZzMTy6m.jpg",
                               reply_markup=kain_menu())

@dp.message_handler(Text("📍 Samarqand Darvoza"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Samarqand Darvoza"
Adres: kocha. Qoratjsh, 5А""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3160488,
                            longitude=69.2297722)

@dp.message_handler(Text(equals="↩️ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=filial_menu())

@dp.message_handler(Text("📍 Alayskiy bozor"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Alayskiy bozor"
Adres: joy. Amir Temur, 42""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3204956,
                            longitude=69.2802406)

@dp.message_handler(Text("📍 Malika"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Malika"
Adres:  kocha. Bagiravon, 29""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3236641,
                            longitude=69.1652273)

@dp.message_handler(Text("📍 Yahyo Gulamov, 94"))
async def send_contact(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg")
    await bot.send_contact(chat_id=message.chat.id,
                           first_name="""Filial: "Yahyo Gulamov, 94"
Adres:  kocha Yahyo Gulamov, 94""",
                           phone_number="📲 Контакты: +998 71 203 12 12")
    await bot.send_location(chat_id=message.chat.id,
                            latitude=41.3052033,
                            longitude=69.2817854)

@dp.message_handler(Text(equals="💼 Bo'sh ish o'rinlari"))
async def start(message: types.Message):
    await message.answer("Reioningizni tanlang",
                               reply_markup=gain_menu())


@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="◀️ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="Toshkent"))
async def start(message: types.Message):
    await message.answer("Sizni qiziqtirayotgan ishni tanlang",
                               reply_markup=fain_menu())


@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="️⏪ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=gain_menu())

@dp.message_handler(Text(equals="Andijoon"))
async def start(message: types.Message):
    await message.answer("Sizni qiziqtirayotgan ishni tanlang",
                               reply_markup=qain_menu())


@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="⏮ Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=gain_menu())

@dp.message_handler(Text(equals="Etkazib beruvchi"))
async def start(message: types.Message):
    await message.answer_photo("https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               """📌 Возраст от 20 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Свободный график(желательно)

👨‍💼/👩‍💼 Опрятный внешний вид 

🚘Наличие своего транспорта

📍ЗП в зависимости от локации и региона""",
                               reply_markup=pain_menu())


@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="🔚 Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                                reply_markup=qain_menu())


@dp.message_handler(Text(equals="Chilonzor rayon"))
async def start(message: types.Message):
    await message.answer("Registerni bosing",
                               reply_markup=lain_menu())

@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                                reply_markup=pain_menu())

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hello",
                         reply_markup=register())

@dp.message_handler(Text(equals="Register"))
async def start(message: types.Message):
    await message.answer("Toliq familiya va ismingizni kriting",
                         reply_markup=cancel())
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
        await message.answer("Yoshingizni kriting agsr yoshingiz 20 pas yoki 35 baland bjlsa biz sizni kabul qilmaymiz")
        await UserState.next()


@dp.message_handler(state=UserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
        await message.answer("Telefon nomerizni kriting")
        await UserState.next()

@dp.message_handler(state=UserState.age)
async def add_bierth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
        await message.answer("Tug'lgan yilingizni kriting")
        await UserState.next()


@dp.message_handler(state=UserState.phone_number)
async def add_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
        await state.finish()
        await message.answer("Mahsulot saqlandi")
        await message.answer(f"Mahsulotni ismi {data['name']},"
                             f"Narhi: {data['age']},"
                             f"Chiqazilgan sanasi: {data['phone_number']}")

@dp.message_handler(Text(equals="Operator"))
async def start(message: types.Message):
    await message.answer_photo("https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               """📌 Возраст от 20 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Свободный график(желательно)

👨‍💼/👩‍💼 Опрятный внешний вид 

🚘Наличие своего транспорта

📍ЗП в зависимости от локации и региона""",
                               reply_markup=wain_menu())


@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="🔚 Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                                reply_markup=qain_menu())

@dp.message_handler(Text(equals="Chilonzor rayon"))
async def start(message: types.Message):
    await message.answer("Registerni bosing",
                               reply_markup=lain_menu())

@dp.message_handler(Text(equals="❌Qaytish❌"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                               reply_markup=main_menu())

@dp.message_handler(Text(equals="Ortga"))
async def back(message: types.Message):
    await message.answer_photo(photo="https://resto.uz/data/resto/44/4343/evos-2986.jpeg",
                                reply_markup=pain_menu())


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hello",
                         reply_markup=register())

@dp.message_handler(Text(equals="Register"))
async def start(message: types.Message):
    await message.answer("Toliq familiya va ismingizni kriting",
                         reply_markup=cancel())
    await UserState.name.set()


@dp.message_handler(state=UserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
        await message.answer("Yoshingizni kriting agsr yoshingiz 20 pas yoki 35 baland bjlsa biz sizni kabul qilmaymiz")
        await UserState.next()


@dp.message_handler(state=UserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
        await message.answer("Telefon nomerizni kriting")
        await UserState.next()

@dp.message_handler(state=UserState.age)
async def add_bierth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
        await message.answer("Tug'lgan yilingizni kriting")
        await UserState.next()


@dp.message_handler(state=UserState.phone_number)
async def add_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text
        await state.finish()
        await message.answer("Mahsulot saqlandi")
        await message.answer(f"Mahsulotni ismi {data['name']},"
                             f"Narhi: {data['age']},"
                             f"Chiqazilgan sanasi: {data['phone_number']}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)