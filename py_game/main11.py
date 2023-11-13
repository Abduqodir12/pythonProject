import random
import time

import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 128, 0)

window_x = 700
window_y = 600

pygame.init()

screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game")
snake_speed = 15

fps = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
score = 0

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True


def show_score(choice, size, font, color):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f"Score: {score}", True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


def game_over():
    game_font = pygame.font.SysFont("times new roman", 38)
    game_over_surface = game_font.render(f"""Your score: {score}. GAME OVER !!!""",
                                         True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (350, 300)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

direction = "RIGHT"
change_to = direction

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] +=10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10,
        ]
    fruit_spawn = True
    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, WHITE, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    show_score(1, 20, "times new roman", WHITE)
    pygame.display.update()
    fps.tick(snake_speed)
