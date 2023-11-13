
class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display_info(self):
                print(f"Ism: {self.name}, Yosh: {self.age}")

class Cat(Animal):
        def __init__(self, name, age, ):
            super().__init__(name, age)

        def display_info(self):
            super().display_info()

class Dog(Animal):
        def __init__(self, name, age, address):
            super().__init__(name, age)
            self.address = address

        def display_info(self):
            super().display_info()
            return f"{self.address} da yashaydi"

class Horse(Animal):
        def __init__(self, name, age, tajriba):
            super().__init__(name, age)
            self.tajriba = tajriba

        def display_info(self):
            super().display_info()
            return f"{self.tajriba} yillik tajribasi bor"

cat = Cat("Pishak", 6 )
Aegean = Cat("Mol", 6 )

labrador = Dog("Bobik", 6, "Kocha")
alabay = Dog("Bori bosar", 6, "Kocha")

genetics = Horse("Sport oti", 16, 10)
pony = Horse("Bolani oti", 16, 5)
# print(asliddin.display_info())

people = [cat, Aegean, labrador, alabay, genetics, pony]

while True:
    choice = input("""
                1. Catlar
                2. Doglar
                3. Horselar
                4. Quit

            """)
    if choice == "1":
        for man in people:
            if isinstance(man, Cat):
                print(man.display_info())
    elif choice == "2":
        for man in people:
            if isinstance(man, Dog):
                print(man.display_info())
    elif choice == "3":
        for man in people:
            if isinstance(man, Horse):
                print(man.display_info())
    elif choice == "4":
        break
    else:
        print("Siz noto'g'ri qiymat kiritdingiz, iltimos boshqattan urinib ko'ring")


# class Telephone:
#     def __int__(self,picture,color,charger,private):
#         self.picture=picture
#         self.color=color
#         self.charjer=charger
#         self.private=private
#
#     def info(self):
#         print(f"Kamerasi: {self.picture}, Rangi :{self.color}, Zaryai: {self.charjer},Xususiyati :{self.private}")
#
#
# telefon=Telephone("180 mp", "Black", "5600", '60 fps')