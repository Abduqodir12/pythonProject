import pygame
import random

pygame.init()

oyna_width = 600
oyna_height = 750

oyna = pygame.display.set_mode((oyna_width, oyna_height))
pygame.display.set_caption("KUB game")
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
black = (0, 0, 0)
cube_size = 49
cube_speed = 15
score = 0

oyin_cube = pygame.Rect(oyna_width / 2 - cube_size / 2, oyna_height - cube_size, cube_size, cube_size)

yiqilish_cubes = []
for i in range(11):
    x = random.randint(1, oyna_width - cube_size)
    y = random.randint(-oyna_height, 1)
    yiqilish_cubes.append(pygame.Rect(x, y, cube_size, cube_size))

running = True
cloc = pygame.time.Clock()

while running:
    oyna.fill(red)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        oyin_cube.x -= cube_speed
    if keys[pygame.K_RIGHT]:
        oyin_cube.x += cube_speed

    for cube in yiqilish_cubes:
        cube.y += cube_speed
        if cube.colliderect(oyin_cube):
            cube.y = -cube_size
            score += 5

    for cube in yiqilish_cubes:
        pygame.draw.rect(oyna, blue, cube)

    pygame.draw.rect(oyna, black, oyin_cube)

    font = pygame.font.Font(None, 46)
    score_text = font.render(f"Score: {score}", True, black)
    oyna.blit(score_text, (10, 10))

    pygame.display.flip()
    cloc.tick(70)

pygame.quit()