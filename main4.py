

            # file = open("asadbek.txt", "w")
            # file.write("asadbek")
            # file.close()

            # a = "asadbek Abduqodir miraziz"
            # print(a.split("\n"))

class CarShop:

    def __init__(self):
        self.products = []

    def create(self):
        file = open("shopping.txt", "w")
        text = file.read()
        products = text.split("\n")
        products.pop()
        file.close()
        self.products = products

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)

    def view(self):
        for product in self.products:
                print(product)


car_shop = CarShop()
            # shopping_online.create()

while True:
    car_buy = input("""
        1 -> View product
        2 -> Add product
        3 -> Delete product
        4 -> Quit

                """)
    if car_buy == "1":
        car_shop.view()
    elif car_buy == "2":
        product = input("Mashimangizni  nomini kiriting: ")
        car_shop.add(product=product)
    elif car_buy == "3":
        product = input("Olmaydigan mashinangizni nomini ayting: ")
        car_shop.remove(product=product)
    elif car_buy == "4":
        break
    else:
        print("Siz noto'g'ri son kiritdingiz, iltimos soni qaytadan kirit")