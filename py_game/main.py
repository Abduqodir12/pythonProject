import pygame

x = 600
y = 600
pygame.init()
pygame.display.set_caption('D7 Junior \\•')
gren = pygame.display.set_mode((x, y))
running = True
green = pygame.Color(0, 128, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gren.fill(green)
    pygame.display.update()

pygame.quit()