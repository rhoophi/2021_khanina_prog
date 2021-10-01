import pygame
import pygame.draw as draw

pygame.init()
#Slomal kod lol
FPS = 30
screen = pygame.display.set_mode((400, 500))
draw.rect(screen, (255, 255, 255), (0, 0, 400, 500))

draw.circle(screen, (247, 237, 186), (200, 250), 100)
draw.circle(screen, (0, 0, 0), (200, 250), 100, 1)
draw.rect(screen, (0, 0, 0), (150, 300, 100, 10))
draw.circle(screen, (250, 127, 127), (150, 250), 30)
draw.circle(screen, (250, 127, 127), (250, 250), 20)
draw.circle(screen, (0, 0, 0), (150, 250), 20)
draw.circle(screen, (0, 0, 0), (250, 250), 10)
draw.polygon(screen, (0, 0, 0), ([(100, 190), (175, 210), (190, 240)]))
draw.polygon(screen, (0, 0, 0), ([(210, 210), (230, 190), (300, 190)]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
