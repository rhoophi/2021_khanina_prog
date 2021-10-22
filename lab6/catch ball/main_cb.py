import pygame as pg
import pygame.draw as draw
from random import randint

pg.init()

FPS = 30
size_x = 1200
size_y = 800
screen = pg.display.set_mode((size_x, size_y))
font = pg.font.Font(None, 40)
font_name = pg.font.match_font('arial')

RED = (255, 158, 158, 255)
BLUE = (121, 218, 235,)
YELLOW = (232, 235, 171)
GREEN = (171, 235, 171)
MAGENTA = (219, 123, 194)
CYAN = (180, 238, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls_n = 5  # number of big balls
g = 1.2  # gravity
mu = 0.9  # gravity
existence_special_target = 0

R = [0] * (balls_n + 1)
color = [0] * (balls_n + 1)
x = [0] * (balls_n + 1)
y = [0] * (balls_n + 1)
v_x = [0] * (balls_n + 1)
v_y = [0] * (balls_n + 1)


def parameters(n):
    """
    creates random parameters of coordinates (x, y), velocity (v_x, v_y), radius (R), color for balls
    and a special target
    :param n: 1 for balls; 2 for special target
    :return: list of parameters
    """
    x_0 = randint(0, size_x)
    y_0 = randint(0, size_y)
    v_x_0 = randint(-35 * n, 35 * n)
    v_y_0 = randint(-35 * n, 35 * n)
    r_0 = randint(30 / n, 50 / n)
    color_0 = COLORS[randint(0, len(COLORS) - 1)]
    return [x_0, y_0, v_x_0, v_y_0, r_0, color_0]


def ball(N):
    """
    creates N balls and a special target
    :param N: number of balls
    """
    for i in range(0, N):
        x[i], y[i], v_x[i], v_y[i], R[i], color[i] = parameters(1)
        draw.circle(screen, color[i], (x[i], y[i]), R[i])


def respawn_ball(j):
    """
    recreates the object with j index after it was clicked on
    :param j: ball's index in object list
    """
    x[j], y[j], v_x[j], v_y[j], R[j], color[j] = parameters(1)


def draw_text(surface, text_0, size, x_0, y_0):
    """
    writes text on screen
    :param surface: surface to blit on
    :param text_0: text to write
    :param size: size of text
    :param x_0: horizontal position
    :param y_0: vertical position
    """
    font_0 = pg.font.Font(font_name, size)
    text_surface = font.render(text_0, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x_0, y_0)
    surface.blit(text_surface, text_rect)


def physics(j, mu_0):
    """
    changes the parameters of j-indexed balls if they hit the wall
    :param j: index of ball or, if j = N, special target
    :param mu_0: 
    """
    x[j] += v_x[j]
    y[j] += v_y[j]
    if j == balls_n:
        if (y[balls_n] - size_y / 2) < 0:
            v_y[balls_n] -= g
        elif (y[balls_n] - size_y / 2) >= 0:
            v_y[balls_n] += g
        if (x[balls_n] - size_x / 2) < 0:
            v_x[balls_n] -= g
        elif (x[balls_n] - size_x / 2) >= 0:
            v_x[balls_n] += g
    if x[j] - R[j] <= 0:
        x[j] = R[j]
        v_x[j] = -v_x[j] * mu_0
        v_y[j] = randint(-35, 35)
    elif x[j] + R[j] >= size_x:
        x[j] = size_x - R[j]
        v_x[j] = -v_x[i] * mu_0
        v_y[j] = randint(-35, 35)
    elif y[j] - R[j] <= 0:
        y[j] = R[j]
        v_y[j] = -v_y[j] * mu_0
        v_x[j] = randint(-35, 35)
    elif y[j] + R[j] >= size_y:
        y[j] = size_y - R[i]
        v_y[j] = -v_y[j] * mu_0
        v_x[j] = randint(-35, 35)


def special_target():
    """
    creates very fast and small target with special description of movement
    """
    global existence_special_target
    existence_special_target = 1
    for _ in range(0, balls_n):
        x[balls_n], y[balls_n], v_x[balls_n], v_y[balls_n], R[balls_n], color[balls_n] = parameters(2)
        draw.circle(screen, color[balls_n], (x[balls_n], y[balls_n]), R[balls_n])


pg.mixer.init()
hit_sound = pg.mixer.Sound("hit_sound.mp3")
pg.mixer.music.load("dark_statique.mp3")

pg.display.update()
clock = pg.time.Clock()
finished = False

timer = 0
special_timer = 0
score = 0
play_time = 90

ball(balls_n)
pg.mixer.music.play(-1)

while not finished and play_time - int((timer * FPS / 1000) // 1) > 0:
    clock.tick(FPS)
    timer += 1

    text = font.render(str(score), True, WHITE)
    place = text.get_rect(center=(size_x / 2, 30))
    screen.blit(text, place)

    text = font.render(str(play_time - int((timer * FPS / 1000) // 1)), True, WHITE)
    place = text.get_rect(center=(6 * size_x / 8, 30))
    screen.blit(text, place)  # creates text with countdown

    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            for i in range(balls_n):
                if (x[i] - event.pos[0]) ** 2 + (y[i] - event.pos[1]) ** 2 <= R[i] ** 2:
                    pg.mixer.Sound.play(hit_sound)
                    score += 1
                    respawn_ball(i)
            if (x[balls_n] - event.pos[0]) ** 2 + (y[balls_n] - event.pos[1]) ** 2 <= R[balls_n] ** 2:
                pg.mixer.Sound.play(hit_sound)
                score += 10
                existence, special_timer, R[balls_n] = 0, 0, 0
                x[balls_n], y[balls_n] = -1, -1
    if timer % ((play_time // 5) * FPS) == 0:
        special_target()
    for i in range(balls_n):
        physics(i, 1)
        draw.circle(screen, color[i], (x[i], y[i]), R[i])
    if existence_special_target == 1:
        physics(balls_n, mu)
        special_timer += 1
        if timer % (FPS / 2) == 0:
            color[balls_n] = COLORS[randint(0, len(COLORS) - 1)]
        draw.circle(screen, color[balls_n], (x[balls_n], y[balls_n]), R[balls_n])
        if special_timer == (play_time // 15) * FPS:
            existence_special_target = 0
            special_timer = 0
    pg.display.update()
    screen.fill(BLACK)
pg.quit()

print('enter your name: ')
name_current = str(input())
if len(name_current) < 9:
    name_current = name_current + ' ' * (9 - len(name_current))
print('your score: ', score)

line_count = 0
place = []
name = []
result = []
with open('leaders.txt', 'r') as file:
    tab = file.read
    for line in file:
        name.append(line.split(' | ')[1])
        result.append(line.split(' | ')[2])
        result[line_count] = int(result[line_count].replace("\n", ""))
        line_count += 1

place_now = line_count
for i in range(0, line_count):
    if score > int(result[i]):
        place_now = i
        break

name.insert(place_now, name_current)
result.insert(place_now, score)

with open('leaders.txt', 'w') as file:
    for i in range(0, line_count + 1):
        row = str(i + 1) + ' | ' + str(name[i]) + ' | ' + str(result[i]) + '\n'
        file.write(row)

file.close()
