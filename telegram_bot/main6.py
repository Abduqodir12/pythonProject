from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
rkm = ReplyKeyboardMarkup(resize_keyboard=True)

from aiogram import Bot, executor, Dispatcher, types
token = "6836097859:AAGcfDFJHTbciYFiBsTTwIxLGKerODTYJaY"
bot = Bot(token=token)
dp = Dispatcher(bot=bot)



keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Button1')
button2 = KeyboardButton(text='Button2')
keyboard.add(button1, button2)


@dp.message_handler(commands=["start"])
async def start_commads_handler(msg:types.Message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    keyboard.add(KeyboardButton("Kantaktingizni kiriting",request_contact=True))
    keyboard.add(KeyboardButton("Python", request_location=True))
    keyboard.add(KeyboardButton("Java"))

    await msg.answer("Welcom! Choise an option",reply_markup=keyboard)


keyboard = InlineKeyboardMarkup([
    InlineKeyboardButton("Button 1",callback_data="button1"),
    InlineKeyboardButton("Button 2", callback_data='button2')
])

@dp.message_handler(commands="help")
async def help_commads_handler(msg: types.Message):
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Contacts", callback_data="contacts"))
    keyboard.add(InlineKeyboardButton("Courses",callback_data="courses"))
    keyboard.add(InlineKeyboardButton("Setting",callback_data="setting"))
    keyboard.add(InlineKeyboardButton("Message Us", callback_data="message us"))

    await msg.answer("Welcom!", reply_markup=keyboard)


@dp.callback_query_handler()
async def button_callback(query:types.CallbackQuery):
    data = query.data

    if data == 'contacts':
        await bot.send_message(query.from_user.id,"""55 508 47 47""")
    elif data == "courses":
        await bot.send_message(query.from_user.id, """Bizning kurslarimiz: Front, Python, Java""")
    elif data == "setting":
        await bot.send_message(query.from_user.id, """Bizda Python kursi bosh ekan """)
    elif data == "message us":
        await bot.send_message(query.from_user.id, """Siz Python kursiga yozildiz""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)