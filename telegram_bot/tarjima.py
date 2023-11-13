# pip install googletrans==3.1.0a0 shu versiyasini install qilamiz

from googletrans import Translator

translator = Translator()


def translate(text):
    translation = translator.translate(text, src="uz", dest="en")
    return translation.text


text = input("So'z kiriting: ")
print(translate(text=text))

