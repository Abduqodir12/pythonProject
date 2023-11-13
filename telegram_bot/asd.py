import qrcode

def qr_creator(link: str, telegram_id: str):
    img = qrcode.make(link)
    type(img)
    img.save(f"{telegram_id}.png")
