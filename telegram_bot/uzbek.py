
from uzbek_latin_cyrillic_converter import converter

def to_cyrillic(text: str):
    data = converter.latin_to_cyrillic(text)
    return data

