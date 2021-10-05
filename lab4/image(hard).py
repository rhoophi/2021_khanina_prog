import pygame
import pygame.draw as draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

lightblue = (88, 172, 232)
white = (255, 255, 255)
darkblue = (29, 38, 43)
lightyellow = (240, 221, 162)
black = (0, 0, 0)
grey = (15, 15, 15)
darkgrey = (99, 105, 128)


def car(x, y, scale=1, orient=1):
    """
    Функция, рисующая машинку, с начальной точкой в центре машины.
    :param x: Координата x машины
    :param y: Координата y машины
    :param scale: размер объекта(по умолчанию 1)
    :param orient: Ориентация объекта(orient == 1 - машина повернута направо, orient == -1 - машина повернута налево)
    """
    draw.rect(screen, lightblue, (x - 60 * scale, y - 20 * scale, 120 * scale, 40 * scale))
    draw.rect(screen, lightblue, (x - 30 * scale, y - 40 * scale, 60 * scale, 20 * scale))
    draw.rect(screen, white, (
        x - 20 * scale, y - 30 * scale, 40 * scale, 10 * scale))
    draw.ellipse(screen, darkblue, (x - 50 * scale, y + 10 * scale, 40 * scale, 20 * scale))
    draw.ellipse(screen, darkblue, (x + 10 * scale, y + 10 * scale, 40 * scale, 20 * scale))
    if orient == -1:
        draw.rect(screen, lightyellow, (x - 60 * scale, y - 10 * scale, 20 * scale, 10 * scale))
    elif orient == 1:
        draw.rect(screen, lightyellow,
                  (x + 40 * scale, y - 10 * scale, 20 * scale, 10 * scale))


def glare(x, y, a, b, density=0.5):
    """
    Функция, создающая блик
    :param x: Координата x центра эллипса блика
    :param y: Координата y центра эллипса блика
    :param a: Большая полуось эллипса у блика
    :param b: Малая полуось эллипса у блика
    :param density: Прозрачность(По умолчания 0.5)
    """
    layer = pygame.Surface((600, 800))
    layer.set_colorkey(black)
    for i in range(51):
        layer.set_alpha(int((255 - i * 5) * density))
        draw.ellipse(layer, white, (a / 2 - i * a / 102, b / 2 - i * b / 102, i * a / 51, i * b / 51))
        screen.blit(layer, (x, y))


def house(color, x, y, width, length, density=255):
    """
    Функция, рисующая дом.
    :param color: Цвет  дома
    :param x: Координата х дома
    :param y: Координата y дома
    :param density: Прозрачность дома(по умолчанию density = 0)
    :param width: Ширина дома
    :param length: Длина дома
    """
    house0 = pygame.Surface((600, 800))
    house0.set_colorkey(black)
    house0.set_alpha(density)
    draw.rect(house0, color, (x, y, width, length))
    screen.blit(house0, (0, 0))


def cloud(color, x, y, a, b, density):
    """
    Функция, рисующая облако.
    :param color: Цвет облака
    :param x: Координата х облака
    :param y: Координата y облака
    :param density: Прозрачность облака
    :param a: большая полуось облака
    :param b: малая полуось облака
    """
    cloud0 = pygame.Surface((600, 800))
    cloud0.set_colorkey(black)
    cloud0.set_alpha(density)
    draw.ellipse(cloud0, color, (x, y, a, b))
    screen.blit(cloud0, (0, 0))


def road(color, x, y, width, length):
    """
    Функция, рисующая дорогу
    :param color: Цвет дороги
    :param x: Начальная координата х дороги
    :param y: Начальная координата y дороги
    :param width: Ширина дороги
    :param length: Длина дороги
    """
    draw.rect(screen, color, (x, y, width, length))


def background():
    """
    Функция, рисующая задний фон: черный прямоугольник, темные дома и облака сзади.
    """
    draw.rect(screen, (125, 125, 125), (0, 0, 600, 800))
    house(grey, 0, 0, 100, 450, 130)
    house(grey, 0, 100, 200, 350, 150)
    cloud(grey, -80, -70, 450, 150, 255)
    house(grey, 550, 70, 200, 450, 110)
    house(grey, 350, 0, 230, 450, 110)
    cloud(grey, 160, 90, 150, 60, 120)
    house(grey, 370, 0, 170, 450, 180)
    house(grey, 300, 140, 250, 450, 150)
    cloud(grey, 400, 110, 600, 200, 120)


def foreground():
    """
    Функция, рисующая ближний фон: дома и дорога
    """
    road(darkgrey, 0, 450, 600, 350)
    house(white, 287, 178, 604, 284)
    house((132, 138, 163), 289, 180, 600, 280)
    house((186, 193, 219), 550, 210, 100, 252)
    house(white, 0, 198, 391, 304)
    house((132, 138, 163), 0, 200, 389, 300)
    house((186, 193, 219), 250, 210, 80, 292)
    house((114, 119, 138), 120, 250, 100, 252)
    house((50, 57, 84), 10, 260, 120, 302)
    house((75, 85, 125), 178, 280, 80, 298)
    house((50, 57, 84), 556, 228, 150, 340)
    house((77, 91, 150), 420, 220, 120, 278)


def cars():
    """
    Функция, рисующая машины.
    """
    car(500, 700, 1, -1)
    car(350, 750, 1.3, -1)
    car(150, 650, 0.75, -1)
    car(400, 600, 0.6, 1)


background()
foreground()
cars()
glare(-200, -100, 700, 300, 0.1)
glare(250, 400, 800, 300, 0.2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
