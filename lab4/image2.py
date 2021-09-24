import pygame
import pygame.draw as draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 500))

draw.rect(screen, (255, 255, 255), (0,0, 400, 500))
draw.rect(screen, (25, 66, 64), (0, 300 , 400, 500))
draw.rect(screen, (134, 146, 150), (0, 0, 400, 285))
draw.rect(screen, (102, 121, 128), (0, 0, 400, 270))
draw.rect(screen, (74, 95, 102), (0, 0, 400, 255))
draw.rect(screen, (56, 75, 82), (0, 0, 400, 240))
draw.rect(screen, (255, 255, 255), (30, 30, 45, 45))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()