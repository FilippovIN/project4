import pygame
import random

V = 100  # скорость пикселей в секунду
FPS = 50
CIRCLE_RADIUS = 10  # радиус шариков

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# список координат шариков
koord = []
# список цветов шариков
color = []

# второй холст
screen2 = pygame.Surface(screen.get_size())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            koord.append(list(event.pos))
            col = (random.random() * 255, random.random() * 255, random.random() * 255)
            color.append(col)
            screen2.fill((0, 0, 0))
            pygame.draw.circle(screen2, col, event.pos, CIRCLE_RADIUS)
            screen.blit(screen2, (0, 0))

    screen.fill((0, 0, 0))

    # движение шариков
    for t in range(len(koord)):
        if koord[t][1] + V / FPS < height - CIRCLE_RADIUS:
            koord[t][1] += V / FPS
        x_pos, y_pos = koord[t]
        pygame.draw.circle(screen, color[t], (x_pos, int(y_pos)), CIRCLE_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
