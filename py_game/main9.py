import random
import pygame


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Coin Game")

RED = (255, 0, 0)
BLEAK = (0, 0, 0)

player_image = pygame.image.load("basket.jpeg")
coin_image = pygame.image.load("coin2.png")

font = pygame.font.Font(None, 26)

player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player.image.get_rect()
player.rect.centerx = 300
player.rect.bottom = 550
coins = pygame.sprite.Group()


class Coin(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 590)
        self.rect.y = -25
        self.image = coin_image


    def update(self):
        self.rect.y += 1
        if self.rect.top > 600:
            self.kill()


score = 0
time_left = 40
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    if player.rect.right > 600:
        player.rect.right = 600
    if player.rect.left < 0:
        player.rect.left = 0

    if random.randint(1, 30) == 1:
        coins.add(Coin())

    coins.update()

    hit_list = pygame.sprite.spritecollide(player, coins, True)
    for hit in hit_list:
        score += 1

    time_left -= 1/60
    screen.fill(BLEAK)

    screen.blit(player.image, player.rect)
    coins.draw(screen)

    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

    text2 = font.render(f"Time left: {int(time_left)}", True, RED)
    screen.blit(text2, (10, 30))

    if time_left <= 0:
        running = False

    pygame.display.flip()
    print(f"Your Score: {score}")

pygame.quit()
