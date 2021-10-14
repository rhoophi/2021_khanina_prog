import pygame
import pygame.draw as draw
from random import randint

pygame.init()

FPS = 30
size_x = 1200
size_y = 800
screen = pygame.display.set_mode((size_x, size_y))
font = pygame.font.Font(None, 40)  # scoreboard's font
font_name = pygame.font.match_font('arial')

RED = (255, 158, 158)
BLUE = (121, 218, 235)
YELLOW = (232, 235, 171)
GREEN = (171, 235, 171)
MAGENTA = (219, 123, 194)
CYAN = (180, 238, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

N = 5  # number of balls generating on the screen


def ball(N):
    """
    draws N balls with x, y coordinates, radius r, v_x and v_y components of velocity and randomly coloured
    :param N: the number of balls
    :return:
    """
    global x, y, v_x, v_y, r, existence, color
    x = []
    y = []
    v_x = []
    v_y = []
    r = []
    color = []
    existence = [1] * N
    for i in range(0, N):
        x.append(randint(0, size_x))
        y.append(randint(0, size_y))
        v_x.append(randint(-30, 30))
        v_y.append(randint(-30, 30))
        r.append(randint(30, 50))
        color.append(COLORS[randint(0, len(COLORS) - 1)])
        draw.circle(screen, color[i], (x[i], y[i]), r[i])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

counter = 0  # number of caught balls
ball(N)

while not finished:
    clock.tick(FPS)
    scoreboard = font.render(str(counter), True, WHITE)
    place = scoreboard.get_rect(center=(size_x / 2, 30))
    screen.blit(scoreboard, place)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(N):
                if (x[i] - event.pos[0]) ** 2 + (y[i] - event.pos[1]) ** 2 <= r[i] ** 2:
                    counter += 1
                    existence[i] = 0

    for i in range(N):
        if existence[i] == 1:
            x[i] += v_x[i]
            y[i] += v_y[i]
            draw.circle(screen, color[i], (x[i], y[i]), r[i])
        else:  # respawn
            existence[i] = 1
            x[i], y[i] = randint(0, size_x), randint(0, size_y)
            r[i] = randint(30, 50)
            v_x[i] = randint(-30, 30)
            v_y[i] = randint(-30, 30)
            color[i] = COLORS[randint(0, len(COLORS) - 1)]
        # physics
        if x[i] <= 0:
            x[i] = 0
            v_x[i] = -v_x[i]
            v_y[i] = randint(-30, 30)
        elif x[i] >= size_x:
            x[i] = size_x
            v_x[i] = -v_x[i]
            v_y[i] = randint(-30, 30)
        elif y[i] <= 0:
            y[i] = 0
            v_y[i] = -v_y[i]
            v_x[i] = randint(-30, 30)
        elif y[i] >= size_y:
            y[i] = size_y
            v_y[i] = -v_y[i]
            v_x[i] = randint(-30, 30)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
