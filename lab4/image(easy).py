import pygame
import pygame.draw as draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 500))


def car(x, y, size=120, orient=1):
    draw.rect(screen, (88, 172, 232), (x - size // 2, y - size // 6, size, size // 3))
    draw.rect(screen, (88, 172, 232), (x - size // 4, y - size // 3, size // 2, size // 6))
    draw.rect(screen, (255, 255, 255), (
        x - (size // 4 - size // 12), y - (size // 3 - size // 12), size // 2 - size // 6, size // 6 - size // 12))
    draw.ellipse(screen, (29, 38, 43), (x - size // 3 - size // 12, y + size // 12, size // 3, size // 6))
    draw.ellipse(screen, (29, 38, 43), (x + size // 6 - size // 12, y + size // 12, size // 3, size // 6))
    if orient == 1:
        draw.rect(screen, (240, 221, 162), (x - size // 2, y - size // 6 + size // 12, size // 6, size // 12))
    else:
        draw.rect(screen, (240, 221, 162),
                  (x + size // 2 - size // 6, y - size // 6 + size // 12, size // 6, size // 12))


# фон
draw.rect(screen, (255, 255, 255), (0, 0, 400, 500))
draw.rect(screen, (25, 66, 64), (0, 300, 400, 500))
draw.rect(screen, (171, 189, 207), (0, 0, 400, 290))

draw.rect(screen, (109, 136, 163), (20, 50, 100, 270))
draw.rect(screen, (91, 100, 138), (130, 60, 95, 265))
draw.rect(screen, (179, 183, 199), (75, 100, 100, 240))

# эллипсы у домов = эллд
elld = pygame.Surface((400, 500))
elld.set_colorkey((0, 0, 0))
elld.set_alpha(150)
draw.ellipse(elld, (182, 188, 212), (0, 0, 250, 100))
screen.blit(elld, (15, 30))

draw.rect(screen, (235, 237, 245), (295, 50, 100, 270))

elld = pygame.Surface((400, 500))
elld.set_colorkey((0, 0, 0))
elld.set_alpha(150)
draw.ellipse(elld, (182, 188, 212), (0, 0, 230, 140))
screen.blit(elld, (78, 70))

draw.rect(screen, (103, 110, 138), (255, 70, 80, 260))

elld = pygame.Surface((400, 500))
elld.set_colorkey((0, 0, 0))
elld.set_alpha(150)
draw.ellipse(elld, (182, 188, 212), (0, 0, 400, 160))
screen.blit(elld, (170, 70))

draw.circle(screen, (142, 191, 174), (350, 750), 400)

car(300, 400, 120, -1)

# эллипсы из машины = эллм
ellm = pygame.Surface((150, 70))
ellm.set_colorkey((0, 0, 0))
ellm.set_alpha(150)
draw.ellipse(ellm, (182, 188, 212), (0, 0, 110, 60))
screen.blit(ellm, (100, 320))

ellm = pygame.Surface((150, 70))
ellm.set_colorkey((0, 0, 0))
ellm.set_alpha(150)
draw.ellipse(ellm, (182, 188, 212), (0, 0, 60, 30))
screen.blit(ellm, (150, 370))

ellm = pygame.Surface((400, 500))
ellm.set_colorkey((0, 0, 0))
ellm.set_alpha(150)
draw.ellipse(ellm, (182, 188, 212), (0, 0, 200, 80))
screen.blit(ellm, (-15, 230))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
