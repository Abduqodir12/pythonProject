from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 Kompaniya haqida"), KeyboardButton(text="📍 Fililallar"))
    rkm.row(KeyboardButton(text="💼 Bo'sh ish o'rinlari"))
    rkm.row(KeyboardButton(text="Menyu"), KeyboardButton(text="🗣 Yangiliklar"))
    rkm.row(KeyboardButton(text="📞 Kontaktlar/Manzil"), KeyboardButton(text="🇺🇿/🇷🇺 Til"))
    return rkm


def filial_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Yaqin filiallarni ko'rsatish"))
    rkm.row(KeyboardButton(text="🏢 Bosh ofis"), KeyboardButton(text="Toshkent sh."))
    rkm.row(KeyboardButton(text="⬅️ Ortga"))
    return rkm

def nain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Locatsiya jonatish"))
    rkm.row(KeyboardButton(text="🔙 Ortga"))
    return rkm


def kain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Samarqand Darvoza"), KeyboardButton(text="📍 Alayskiy bozor"))
    rkm.row(KeyboardButton(text="📍 Malika"), KeyboardButton(text="📍 Yahyo Gulamov, 94"))
    rkm.row(KeyboardButton(text="↩️ Ortga"))
    return rkm

def gain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijoon"))
    rkm.row(KeyboardButton(text="Kokond"), KeyboardButton(text="Namangan"))
    rkm.row(KeyboardButton(text="Toshkent viloyati"), KeyboardButton(text="Samarqand"))
    rkm.row(KeyboardButton(text="Fargona"), KeyboardButton(text="Xorezm viloyati"))
    rkm.row(KeyboardButton(text="Navoi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="◀️ Ortga"))
    return rkm

def fain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal hodim"), KeyboardButton(text="Operator"))
    rkm.row(KeyboardButton(text="Etkazib beruvchi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="⏪ Ortga"))
    return rkm

def qain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal hodim"), KeyboardButton(text="Operator"))
    rkm.row(KeyboardButton(text="Etkazib beruvchi"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="⏮ Ortga"))
    return rkm

def pain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Chilonzor rayon"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="🔚 Ortga"))
    return rkm

def lain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="Ortga"))
    button = KeyboardButton(text="Register")
    rkm.add(button)
    return rkm

def cancel():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="cancel")
    rkm.add(button)
    return rkm


def wain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Chilonzor rayon"))
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="🔚 Ortga"))
    return rkm

def cain_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌Qaytish❌"), KeyboardButton(text="Ortga"))
    button = KeyboardButton(text="Register")
    rkm.add(button)
    return rkm

# ----------------------------------------------------------------------------------------------------

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def register():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Register")
    rkm.add(button)
    return rkm


def cancel():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="cancel")
    rkm.add(button)
    return rkm