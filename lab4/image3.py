import pygame
import pygame.draw as draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))


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


def glare(color, x, y, a, b, tr=0.5):
    layer = pygame.Surface((600, 800))
    layer.set_colorkey((0, 0, 0))
    for i in range(51):
        layer.set_alpha(int((255 - i * 5) * tr))
        draw.ellipse(layer, (255, 255, 255), (a / 2 - i * a / 102, b / 2 - i * b / 102, i * a / 51, i * b / 51))
        screen.blit(layer, (x, y))


# фон
draw.rect(screen, (125, 125, 125), (0, 0, 600, 800))
# черные дома сзади
house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(130)
draw.rect(house0, (15, 15, 15), (0, 0, 100, 450))
screen.blit(house0, (0, 0))

house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(80)
draw.rect(house0, (15, 15, 15), (0, 100, 200, 350))
screen.blit(house0, (0, 0))
# и облака
house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(120)
draw.ellipse(house0, (15, 15, 15), (-80, -70, 450, 150))
screen.blit(house0, (0, 0))

glare((255, 255, 255), -200, -100, 700, 300, 0.1)

house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(110)
draw.rect(house0, (15, 15, 15), (550, 70, 200, 450))
screen.blit(house0, (0, 0))

house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(110)
draw.rect(house0, (15, 15, 15), (350, 0, 230, 450))
screen.blit(house0, (0, 0))
# еще облако
house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(120)
draw.ellipse(house0, (15, 15, 15), (160, 90, 150, 60))
screen.blit(house0, (0, 0))

house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(180)
draw.rect(house0, (15, 15, 15), (370, 0, 170, 450))
screen.blit(house0, (0, 0))

house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(150)
draw.rect(house0, (15, 15, 15), (300, 140, 250, 450))
screen.blit(house0, (0, 0))
# и еще облако
house0 = pygame.Surface((600, 800))
house0.set_colorkey((0, 0, 0))
house0.set_alpha(120)
draw.ellipse(house0, (15, 15, 15), (400, 110, 600, 200))
screen.blit(house0, (0, 0))

# дорога
draw.rect(screen, (99, 105, 128), (0, 450, 600, 350))
# ближние домики

glare((255, 255, 255), 250, 200, 1200, 300)

draw.rect(screen, (255, 255, 255), (287, 178, 604, 284))
draw.rect(screen, (132, 138, 163), (289, 180, 600, 280))
draw.rect(screen, (186, 193, 219), (550, 210, 100, 252))

draw.rect(screen, (255, 255, 255), (0, 198, 391, 304))
draw.rect(screen, (132, 138, 163), (0, 200, 389, 300))
draw.rect(screen, (186, 193, 219), (250, 210, 80, 292))
draw.rect(screen, (114, 119, 138), (120, 250, 100, 252))
# домики еще ближе
draw.rect(screen, (50, 57, 84), (10, 260, 120, 302))
draw.rect(screen, (75, 85, 125), (178, 280, 80, 298))
draw.rect(screen, (50, 57, 84), (556, 228, 150, 340))
draw.rect(screen, (77, 91, 150), (420, 220, 120, 278))

# машинки
car(500, 700)
car(350, 750, 150)
car(150, 650, 90)
car(400, 600, 80, -1)

glare((255, 255, 255), 250, 400, 800, 300, 0.2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
