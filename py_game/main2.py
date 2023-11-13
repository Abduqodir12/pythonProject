import pygame

pygame.init()
screen = pygame.display.set_mode((700, 900))
pygame.display.set_caption("D7 guruhi")
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 128, 0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    screen.fill(red)
    pygame.draw.rect(screen, green, (300, 350, 200, 300))
    pygame.display.update()

pygame.quit()

# -----------------------------------------------------------------------------------

# pygame.init()
# screen = pygame.display.set_mode((700, 800))
# pygame.display.set_caption("D7 guruhi")
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 128, 0)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0,0,0))
#     screen.fill(red)
#     pygame.draw.polygon(screen, green,
#                         ((100, 100), (100, 200), (200, 200), (100, 150), (50, 80), ))
#     pygame.display.update()
#
# pygame.quit()


# -----------------------------------------------------------------------------------------------------

# yaponiya uy ishi

# pygame.init()
# screen = pygame.display.set_mode((900, 700))
# pygame.display.set_caption("D7 guruhi")
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 128, 0)
# white = pygame.Color(255, 255, 255)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((255, 255, 255))
#     screen.fill(white)
#     pygame.draw.circle(screen, red,(450, 300), 50)
#     pygame.display.update()
#
# pygame.quit()


# ----------------------------------------------------------------------------------------------------------

# ikkinchi uy ishi

# pygame.init()
# screen = pygame.display.set_mode((700, 900))
# pygame.display.set_caption("D7 guruhi")
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 128, 0)
# white = pygame.Color(255, 255, 255)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((255, 255, 255))
#     screen.fill(white)
#     pygame.draw.circle(screen, red,(150, 50), 15)
#     pygame.display.update()
#
# pygame.quit()


# ---------------------------------------------------------------------------------------------------------------

#uchinchi uy ishi

# pygame.init()
# screen = pygame.display.set_mode((700, 900))
# pygame.display.set_caption("D7 guruhi")
# red = pygame.Color(255, 0, 0)
# black = pygame.Color(0, 0, 0)
# blue = pygame.Color(240, 248, 255)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     screen.fill(black)
#     pygame.draw.rect(screen, red, (300, 800, 90, 20))
#     pygame.display.update()
#     pygame.draw.rect(screen, blue, (600, 700, 20, 50))
#     pygame.display.update()
#
#
# pygame.quit()