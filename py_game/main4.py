#import pygame

# pygame.init()
# screen = pygame.display.set_mode((600, 600))
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("Sichqoncha bosildi", event.pos)
#         elif event.type == pygame.MOUSEBUTTONUP:
#             print("Sichqonani qoyib yubordiz", event.pos)

# -------------------------------------------------------------------

# pygame.init()
# screen = pygame.display.set_mode((600, 600))
# MY_EVENT = pygame.USEREVENT + 1
# my_event = pygame.event.Event(MY_EVENT, massage="Hello d7")
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == MY_EVENT:
#             print(event.massage)


# -----------------------------------------------------------------------------


ismi = 10
if ismi < 9:
    print("Uzun ism")
elif ismi < 6-8:
    print("Ortancha ism")
elif ismi < 6:
    print("Qisqa ism")
else:
    print("9< Uzun ism","6-8< Ortacha ism", "6< Qisqa ism")


ishchilar = 5
if ishchilar < 5:
    print("Sorin 10 mln")
elif ishchilar < 2-3:
    print("Sovrin 5 mln")
elif ishchilar < 1:
    print("Turib ishla")
else:
    print("5< Sovrin 10 mln", "2-3< Sovrin 5 mln", "1< Turib ishla")

kvadrat = 5
if kvadrat < 5:
    print("5=5 teng")
elif kvadrat < 3:
    print("3=4 notog`ri")
elif kvadrat < 1:
    print("1=2 notog`ri")
else:
    print("5=5 teng kvadrat", "3=4 keshig`", "1=2 keshig`")


son1 = int(input("a"))
son2 = int(input("v"))

if son1< son2:
    print(son2)
else:
    print(son1)


# ism = input("ism")
# if len(ism)<6:
#     print("qisqa ism")
# elif len(ism)>=6 and len(ism)<8
#     print("O`, ism")
# else:
#     print("Uzun ism")
#
# a = 50
# b = 50
# A = int(input("Son kiriting"))
# else
# print("Kvadrat")