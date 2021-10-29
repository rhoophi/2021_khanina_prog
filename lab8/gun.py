import math
import random
import pygame as pg

FPS = 30

RED = (255, 158, 158, 255)
BLUE = (121, 218, 235,)
YELLOW = (232, 235, 171)
GREEN = (171, 235, 171)
MAGENTA = (219, 123, 194)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA]
NAVY = (0, 0, 128)
BLACK = (0, 0, 0)
GREY = (125, 125, 125)
WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 600

g = 6  # gravity
k = 0.85  # energy loss
N = 1  # number of targets
timer = 0
score = 0

balls = []
targets = []

play_time = 90
lifetime = FPS * 3  # ball existence time in number of frames
time_spawn = 30
x_gun = 40
y_gun = 450
gun_width = 4
fire_power_max = 100


def draw_text(surface, text_0, size, x, y):
    """
    writes text on screen.
    :param surface: the surface where text is written
    :param text_0: text is written
    :param size: size of the text
    :param x: horizontal coordinate of a text
    :param y: vertical coordinate of a text
    """
    font_0 = pg.font.Font(font_name, size)
    text_surface = font.render(text_0, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


class Ball:
    def __init__(self, x=x_gun, y=y_gun):
        """
        ball class constructor. self.r - radius of a ball, self.vx and self.vy are horizontal and vertical components
        of a ball's velocity, self.color - color of a ball, self.timer - timer of ball's existence, self.hit -
        variable checking if there was a target hit with this ball.
        :param x: horizontal initial coordinate of a ball
        :param y: vertical initial coordinate of a ball
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.timer = 0
        self.hit = 0

    def move(self):
        """
        moves a ball after an iteration by updating coordinates values using velocity, gravity and hitting the wall.
        """
        if self.timer <= lifetime:
            self.x += self.vx
            self.y += self.vy
            self.vy += g
            if self.x + self.r >= WIDTH:
                self.x = WIDTH - self.r
                self.vx = - self.vx * k
            elif self.y - self.r <= 0:
                self.y = self.r
                self.vy = - self.vy * k + g
            elif self.y + self.r >= HEIGHT:
                self.y = HEIGHT - self.r
                self.vy = - self.vy * k + g
            self.timer += 1
        else:
            self.x, self.y, self.vx, self.vy, self.r = -1, -1, 0, 0, 1
            del self

    def draw(self):
        """
        draws a ball on screen with set color, coordinates and radius.
        """
        if self.timer <= lifetime:
            pg.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """
        checks if ball hits a target object obj.
        :param obj: hitting object.
        :return: True if ball hits a target, False if not.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= self.r + obj.r:
            return True
        else:
            return False


class Gun:
    def __init__(self):
        """
        gun class constructor. self.f_power - initial power of the shoot, self.f_on - variable checking if shooting
        started.
        """
        self.fire_power = 10
        self.fire_on = 0
        self.angle = 1
        self.color = GREY

    def fire_start(self, event_0):
        """
        starts preparing for a shoot.
        :param event_0: if the button on mouse is held, starts preparing for a shoot
        """
        self.fire_on = 1

    def fire_end(self, event_0):
        """
        makes gun shoot with a ball.
        :param event_0: if button on mouse is up, shoots;
        """
        global balls
        new_ball = Ball()
        new_ball.r += 5
        self.angle = math.atan2((y_gun - event_0.pos[1]), event_0.pos[0] - x_gun)
        new_ball.vx = self.fire_power * math.cos(self.angle)
        new_ball.vy = - self.fire_power * math.sin(self.angle)
        balls.append(new_ball)
        self.fire_on = 0
        self.fire_power = 10

    def targeting(self, event_0):
        """
        targets the gun.
        :param event_0: get the coordinates of the cursor
        """
        if event_0:
            self.angle = math.atan2((y_gun - event_0.pos[1]), event_0.pos[0] - x_gun)
        if self.fire_on:
            self.color = NAVY
        else:
            self.color = GREY

    def draw(self):
        """
        draws a gun in both neutral and fire conditions.
        """
        pg.draw.line(screen, self.color, [x_gun, y_gun],
                     [x_gun + self.fire_power * math.cos(self.angle), y_gun - self.fire_power * math.sin(self.angle)],
                     gun_width)

    def power_up(self):
        """
        increases the power of shoot while the mouse button is held.
        """
        if self.fire_on:
            if self.fire_power < fire_power_max:
                self.fire_power += 5
            self.color = NAVY
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """
        target class constructor. self.x and self.y - initial horizontal and vertical coordinates of a target, self.vx
        and self.vy - initial horizontal and vertical components of target's velocity, self.r - initial radius of a
        target and self.color is initial color of a target.
        """
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.vx = random.randint(-20, 20)
        self.vy = random.randint(-20, 20)
        self.r = random.randint(20, 50)
        self.color = random.choice(GAME_COLORS)

    def new_target(self):
        """
        creates a new target. self.x and self.y - initial horizontal and vertical coordinates of a new target, self.vx
        and self.vy - initial horizontal and vertical components of new target's velocity, self.r - initial radius of a
        new target and self.color is initial color of a new target.
        """
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.vx = random.randint(-20, 20)
        self.vy = random.randint(-20, 20)
        self.r = random.randint(20, 50)
        self.color = random.choice(GAME_COLORS)

    def move(self):
        """
        moves target after an iteration. updates the self.x and self.y values using initiated velocity. checks hits
        with walls.
        """
        self.x += self.vx
        self.y += self.vy

        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = - self.vx
        elif self.x + self.r >= WIDTH:
            self.x = WIDTH - self.r
            self.vx = - self.vx
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = - self.vy
        elif self.y + self.r >= HEIGHT:
            self.y = HEIGHT - self.r
            self.vy = - self.vy

    def draw(self):
        """
        draws a target with initiated parameters.
        """
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)


pg.init()
font = pg.font.Font(None, 40)
font_name = pg.font.match_font("arial")

screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()
gun = Gun()
for _ in range(N):
    targets.append(Target())

finished = False

while not finished and timer <= FPS * play_time:
    screen.fill(WHITE)
    gun.draw()

    for target in targets:
        target.draw()
    for ball in balls:
        ball.draw()

    text = font.render(str(score), True, NAVY)
    place = text.get_rect(center=(WIDTH / 3, 30))
    screen.blit(text, place)  # scoreboard

    text = font.render(str(90 - int((timer * FPS / 900) // 1)), True, NAVY)
    place = text.get_rect(center=(3 * WIDTH / 4, 30))
    screen.blit(text, place)  # countdown

    pg.display.update()

    clock.tick(FPS)
    timer += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            gun.fire_start(event)
        elif event.type == pg.MOUSEBUTTONUP:
            gun.fire_end(event)
        elif event.type == pg.MOUSEMOTION:
            gun.targeting(event)

    for ball in balls:
        ball.move()
        for target in targets:
            if ball.hittest(target):
                target.new_target()
                score += 1
                if score % 20 == 0:
                    N = N + 1
                    targets.append(Target())

    for target in targets:
        target.move()

    gun.power_up()

pg.quit()
print("your score: ", score, "!")
