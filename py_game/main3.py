import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((700, 800))

red = pygame.Color(255, 0, 0)
kvadrat_size = 39


def draw_rectangle(x, y):
    for i in range(4):
        rect = pygame.Rect(i*1 * kvadrat_size, y+x, kvadrat_size, kvadrat_size)
        pygame.draw.rect(screen, red, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    draw_rectangle(20, 20)
    pygame.display.update()