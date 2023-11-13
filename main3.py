# with open("d7.txt", "w") as file:
#     file.write("Ibrohim, xamidullo, asadbek")

# with open("car.txt", "a") as file:
#     file.write("Tayota Supra mk5 \n , Bugatti Chiron \n, Volga 3110 \n")
#     file.write("\n Gm  , Matasikl")


#import os

#if os.path.exists("car.txt"):
#    print("bu fayl mavjud")
#else:
#    with open("car.txt","w") as file:
#        file.write("Yangi malumot")

#--------------------------------------


with open("birinchi.txt", "w") as f:
    f.write("oqish kerak")


with open("ikkichi.txt", "r") as file:
    file.write("Yozishi kerak")
    contens = f.read()
    print(contens)

with open("Uchinchi.txt", "a") as file:
    file.write("Yozib oqish kerak")