# import pygame
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y) -> None:
#         super().__init__()
#         self.image = pygame.image.load("futboll.png")
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= 10
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += 10
#         if keys[pygame.K_UP]:
#             self.rect.y += 10
#         if keys[pygame.K_DOWN]:
#             self.rect.y -= 10
#
#
# player = Player(100, 150)
# player2 = Player(200, 300)
# player3 = Player(300, 100)
# player4 = Player(100, 150)
# player5 = Player(400, 500)


# group = pygame.sprite.Group()
# group.add(player5, player4, player3, player2, player)
#
# colliton = pygame.sprite.collide_rect(player5,player4)
# print(colliton)



import pygame

import random




WIDTH = 800

HEIGHT = 650

FPS = 30





WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)





class Player(pygame.sprite.Sprite):
    def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.Surface((50, 50))
         self.image.fill(GREEN)
         self.rect = self.image.get_rect()
         self.rect.center = (WIDTH / 2, HEIGHT / 2)


def update(self):
    self.rect.x += 5
    if self.rect.left > WIDTH:
       self.rect.right = 0






pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player()

all_sprites.add(player)





running = True

while running:
       clock.tick()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

all_sprites.update()


screen.fill(BLACK)

all_sprites.draw(screen)


pygame.display.flip()



