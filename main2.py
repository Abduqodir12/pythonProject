


class Bankomat:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        # self.__balance = self.__balance + amount
        self.__balance += amount
        self.transaction_history.append(
            f"{self.owner}ga {amount} summa qo'shildi. Yangi balans {self.__balance}"
        )
        print(f"{self.owner}ga {amount} summa qo'shildi. Yangi balans {self.__balance}")

    def withdraw(self, amount):
        if self.__balance < amount:
            print(f"Hisobingizda yetarli mablag' mavjud emas. Joriy balans {self.__balance}")
        else:
            self.__balance -= amount
            self.transaction_history.append(
                f"{self.owner} dan {amount} miqdorda pul yechildi. Yangi balans {self.__balance}"
            )
            print(f"{self.owner} dan {amount} miqdorda pul yechildi. Yangi balans {self.__balance}")

    def transaction(self, amount, recipient):
        if self.__balance < amount:
            print(f"Hisobingizda yetarli mablag' mavjud emas. Joriy balans {self.__balance}")
        else:
            self.__balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(
                f"{self.owner} dan {recipient.owner} ga {amount} miqdorida pul tushdi. Yangi balans {self.__balance}"
            )
            print(f"{self.owner} dan {recipient.owner} ga {amount} miqdorida pul tushdi. Yangi balans {self.__balance}")

    def get_balance(self):
        return self.__balance


account = {}

while True:
    action = input("""
        1 -> Hisob yaratish
        2 -> Pul qo'shish
        3 -> Pul yechish
        4 -> Pul o'tqazish
        5 -> Balansni ko'rish
        6 -> Tarixni ko'rish
        7 -> Chiqish
    """)

    if action == "1":
        name = input("Hisob yaratish uchun ism kiriting: ")
        if name in account:
            print(f"{name} uchun oldin account yaratilgan")
        else:
            account[name] = Bankomat(owner=name)
            print(f"{name} uchun hisob yaratildi")
    elif action == "2":
        name = input("Hisob egasini ismini kiriting: ")
        if name not in account:
            print(f"{name} uchun hisob yaratilmagan")
        else:
            amount = float(input("Pul tushadigan summani kiriting: "))
            account[name].deposit(amount=amount)
    elif action == "3":
        name = input("Hisob egasini ismini kiriting: ")
        amount = float(input("Pul yechiladigan summani kiriting: "))
        account[name].withdraw(amount=amount)
    elif action == "5":
        name = input("Hisob egasini ismini kiriting: ")
        print(account[name].get_balance())
    elif action == "7":
        break