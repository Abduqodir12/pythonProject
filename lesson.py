class Telephone:
    def __int__(self,picture,color,charger,private):
        self.picture=picture
        self.color=color
        self.charjer=charger
        self.private=private

    def info_picture(self):
        return "108 mp "

    def info_color(self):
        return "Black"

    def info_charjer(self):
        return "5600 ml"

    def private(self):
        return "Oyin oynasa "

telefon=Telephone(f"Kamerasi:{self.info_picture},rangi :{self.color} ,batereyasi: {self.charjer}, 60fps: {self.private}")
print(telefon.info_picture())
print(telefon.info_color())
print(telefon.info_charjer())
print(telefon.private())