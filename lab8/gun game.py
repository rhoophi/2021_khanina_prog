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
EVIL_RED = (171, 0, 0)
GREY = (125, 125, 125)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREY = (225, 225, 225)

WIDTH = 800
HEIGHT = 600

g = 5 * 30 / FPS  # gravity
timer = 0
playtime = FPS * 90
score = 0

n_targets = 1  # an initial number of targets
n_bombs = 10  # an initial number of bombs
balls = []
targets = []
bombs = []
enemies = []
enemy_colors = [NAVY, EVIL_RED]


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
    def __init__(self, x, y, color, capacity, r, g_0):
        """
        ball class constructor. self.r - radius of a ball, self.vx and self.vy are horizontal and vertical components
        of a ball's velocity, self.color - color of a ball, self.timer - timer of ball's existence, self.hit -
        variable checking if there was a target hit with this ball.
        :param x: horizontal coordinate of a ball
        :param y: vertical coordinate of a ball
        :param color: color of a ball
        :param capacity: variable, describing how frequent we can use this ball
        :param r: radius of a ball
        :param g_0: gravity
        """
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = color
        self.timer = 0
        self.capacity = capacity
        self.g = g_0

    def move(self):
        """
        moves a ball after an iteration by updating coordinates values using velocity, gravity and hitting the wall.
        """
        if self.timer <= FPS * 3:
            self.x += self.vx
            self.y += self.vy
            self.vy += self.g
        else:
            self.x, self.y, self.vx, self.vy, self.r = -2, -2, 0, 0, 0
            del self

    def draw(self):
        """
        draws a ball on screen with set color, coordinates and radius.
        """
        if self.timer < FPS * 3:
            pg.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def hit_ball(self, obj):
        """
        checks if the ball hits the object.
        :param obj: object hitting the target
        :return: True if the target hits the object, False if not
        """
        if math.hypot(self.x - obj.x, self.y - obj.y) <= self.r + obj.r:
            return True
        else:
            return False


class Target:
    def __init__(self):
        """
        target class constructor. self.x and self.y - initial horizontal and vertical coordinates of a target, self.vx
        and self.vy - initial horizontal and vertical components of target's velocity, self.r - initial radius of a
        target and self.color is initial color of a target.
        """
        self.r = random.randint(20, 50)
        self.x = random.randint(self.r, WIDTH - self.r)
        self.y = random.randint(self.r, HEIGHT - self.r)
        self.vx = random.randint(-20, 20) * 30 / FPS
        self.vy = random.randint(-20, 20) * 30 / FPS
        self.color = random.choice(GAME_COLORS)

    def new_target(self):
        """
        creates new parameters for a target.
        """
        self.__init__()

    def move(self):
        """
        moves target after an iteration. updates the self.x and self.y values using initiated velocity. checks hits
        with walls.
        """
        self.x += self.vx
        self.y += self.vy

        if self.x - self.r <= 0:
            self.x = 0 + self.r
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

    def hit_test(self, obj):
        """
        checks if the target hits the object.
        :param obj: object hitting the target
        :return: True if the target hits the object, False if not
        """
        if math.hypot(self.x - obj.x, self.y - obj.y) <= self.r + obj.r:
            return True
        else:
            return False

    def clear(self):
        """
        deletes the waste target.
        """
        self.x, self.y, self.vx, self.vy, self.r = -1, -1, 0, 0, 0
        del self


class Bomb:
    def __init__(self):
        """
        initiates a bomb.
        """
        self.r = random.randint(5, 15)
        self.x = random.randint(self.r, WIDTH - self.r)
        self.y = random.randint(self.r, HEIGHT - self.r)
        self.color = LIGHT_GREY

    def new_bomb(self):
        """
        creates new parameters for a self-destroyed bomb.
        """
        self.__init__()

    def draw(self):
        """
        draws a bomb.
        :return:
        """
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def clear(self):
        """
        deletes the waste bomb.
        """
        self.x, self.y, self.r = -1, -1, 0
        del self


class Gun:
    def __init__(self, x, y, color):
        """
        gun class constructor. self.v_gun - velocity while moving, self.pistols - magazine of a gun, self.firepower -
        initial power of a shoot, self.ready - variable checking if the gun is "ready" for shooting, self.angle - the
        angle of the barrel, self.COLOR - the initial color of a gun, self.color - color of a gun in a particular
        moment, self.r - radius of a gun's body, self.max_firepower - maximum of power of a shoot.
        :param x: horizontal coordinate of a gun
        :param y: vertical coordinate of a gun
        :param color: color of a gun
        """
        self.x = x
        self.y = y
        self.v_gun = 5 * 30 / FPS
        self.pistols = 4
        self.firepower = 20
        self.ready = 0
        self.angle = 1
        self.hp = 10
        self.COLOR = color
        self.color = self.COLOR
        self.r = 15
        self.max_firepower = 80

    def fire(self, event_0, capacity, r, g_0=g):
        """
        makes gun shoot with a ball.
        :param event_0: if button on mouse is up, shoots
        :param capacity: the capacity of initiating ball
        :param r: the radius of initiating ball
        :param g_0: gravity in the physics of initiating ball movement
        """
        new_ball = Ball(self.x, self.y, self.color, capacity, r, g_0)
        self.angle = math.atan2((self.y - event_0.pos[1]), event_0.pos[0] - self.x)
        new_ball.vx = self.firepower * math.cos(self.angle) * 30 / FPS
        new_ball.vy = - self.firepower * math.sin(self.angle) * 30 / FPS
        balls.append(new_ball)
        self.ready = 0
        self.firepower = 20

    def aiming(self, event_0):
        """
        aims the gun.
        :param event_0: get the coordinates of the cursor
        """
        if event_0:
            self.angle = math.atan2((self.y - event_0.pos[1]), event_0.pos[0] - self.x)
        if self.pistols != 0:
            self.color = self.COLOR
        else:
            self.color = GREY

    def draw(self):
        """
        draws a gun with body in both neutral and fire conditions.
        """
        pg.draw.line(screen, self.color, [self.x, self.y], [self.x + self.firepower * math.cos(self.angle),
                                                            self.y - self.firepower * math.sin(self.angle)], 8)
        pg.draw.circle(screen, self.color, [self.x, self.y], self.r)

    def power_up(self):
        """
        increases the power of shoot while the mouse button is held.
        """
        if self.ready:
            if self.firepower < self.max_firepower:
                self.firepower += 4
        if self.pistols != 0:
            self.color = self.COLOR
        else:
            self.color = GREY

    def hit_gun(self, obj):
        """
        checks if gun collides with the object.
        :param obj: object which hits the gun
        """

        if math.hypot(self.x - obj.x, self.y - obj.y) <= self.r + obj.r:
            return True
        else:
            return False

    def move_left(self):
        """
        moves the gun to the left.
        """
        if self.x >= self.r:
            self.x -= self.v_gun

    def move_right(self):
        """
        moves the gun to the right.
        """
        if self.x <= WIDTH - self.r:
            self.x += self.v_gun

    def move_up(self):
        """
        moves the gun to the top.
        """
        if self.y >= self.r:
            self.y -= self.v_gun

    def move_down(self):
        """
        moves the gun to the bottom.
        """
        if self.y <= HEIGHT - self.r:
            self.y += self.v_gun


class Enemy:
    def __init__(self, x, y, color):
        """
        enemy class constructor. self.color - color of the enemy.
        :param x: horizontal coordinate of the enemy
        :param y: vertical coordinate of the enemy
        :param obj: enemy's target object
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = random.randint(-20, 20)
        self.vy = random.randint(-20, 20)
        self.color = color

    def move(self):
        """
        moves the enemy after an iteration by updating coordinates values using velocity, gravity and hitting the wall.
        """
        self.x += self.vx
        self.y += self.vy
        if self.x - self.r <= 0:
            self.x = 0 + self.r
            self.vx = - self.vx
            self.vy = random.randint(-20, 20)
        elif self.x + self.r >= WIDTH:
            self.x = WIDTH - self.r
            self.vx = - self.vx
            self.vy = random.randint(-20, 20)
        elif self.y - self.r <= 0:
            self.y = self.r
            self.vy = - self.vy
            self.vx = random.randint(-20, 20)
        elif self.y + self.r >= HEIGHT:
            self.y = HEIGHT - self.r
            self.vy = - self.vy
            self.vx = random.randint(-20, 20)

    def draw(self):
        """
        draws a ball on screen with set color, coordinates and radius.
        """
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def clear(self):
        """
        deletes the waste bomb.
        """
        self.x, self.y, self.r = -1, -1, 0
        del self


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.init()
font = pg.font.Font(None, 40)
font_name = pg.font.match_font("arial")

finished = False
clock = pg.time.Clock()

gun_A = Gun(40, 450, NAVY)
gun_A.max_firepower = 100
gun_B = Gun(WIDTH - 40, 450, RED)
gun_B.max_firepower = 200

for _ in range(n_targets):
    targets.append(Target())

for _ in range(n_bombs):
    bombs.append(Bomb())

for _ in range(2):
    enemies.append(Enemy(WIDTH // 2, HEIGHT // 2, enemy_colors[_]))

while not finished and timer <= playtime and gun_A.hp > 0 and gun_B.hp > 0:
    screen.fill(WHITE)
    gun_A.draw()
    gun_B.draw()
    for t in targets:
        t.draw()
    for b in balls:
        b.draw()
    for bomb in bombs:
        bomb.draw()
    for enemy in enemies:
        enemy.draw()

    text = font.render(str(score), True, NAVY)
    place = text.get_rect(center=(WIDTH / 3, 30))
    screen.blit(text, place)  # score

    text = font.render(str(90 - int(timer // FPS)), True, NAVY)
    place = text.get_rect(center=(3 * WIDTH / 4, 30))
    screen.blit(text, place)  # countdown

    text = font.render("HP A:" + str(gun_A.hp), True, NAVY)
    place = text.get_rect(center=(70, 30))
    screen.blit(text, place)  # A's hp

    text = font.render("HP B:" + str(gun_B.hp), True, NAVY)
    place = text.get_rect(center=(WIDTH - 70, 30))
    screen.blit(text, place)  # B's hp

    pg.display.update()
    clock.tick(FPS)
    timer += 1

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        gun_A.move_left()
    elif keys[pg.K_d]:
        gun_A.move_right()
    elif keys[pg.K_w]:
        gun_A.move_up()
    elif keys[pg.K_s]:
        gun_A.move_down()
    if keys[pg.K_LEFT]:
        gun_B.move_left()
    elif keys[pg.K_RIGHT]:
        gun_B.move_right()
    elif keys[pg.K_UP]:
        gun_B.move_up()
    elif keys[pg.K_DOWN]:
        gun_B.move_down()

    for t in targets:
        t.move()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # if the right button of the mouse is clicked on
                if gun_A.pistols != 0:
                    gun_A.ready = 1
                else:
                    print("you don't have an infinite number of pistons!")
            if event.button == 3:  # if the right button of the mouse is clicked on
                if gun_B.pistols != 0:
                    gun_B.ready = 1
                else:
                    print("you don't have an infinite number of pistons!")
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                if gun_A.ready:
                    gun_A.fire(event, 3, 20)
                    gun_A.pistols -= 1
            if event.button == 3:
                if gun_B.ready:
                    gun_B.fire(event, -1, 10, 0)
                    gun_B.pistols -= 1
        elif event.type == pg.MOUSEMOTION:
            gun_A.aiming(event)
            gun_B.aiming(event)

    for b in balls:
        b.move()
        for t in targets:
            if b.hit_ball(t) and b.capacity != 0:
                t.new_target()
                score += 1
                b.capacity -= 1
        if b.capacity == 0:
            b.timer = FPS * 3
        for enemy in enemies:
            if b.hit_ball(enemy):
                enemy.clear()
                score += 5
        if b.hit_ball(gun_A):
            finished = True
            print("player B killed player A :(")
        elif b.hit_ball(gun_B):
            finished = True
            print("player B killed player A :(")

    for enemy in enemies:
        enemy.move()
        if gun_A.hit_gun(enemy):
            gun_A.hp -= 1
        if gun_B.hit_gun(enemy):
            gun_B.hp -= 1

    for bomb in bombs:
        if gun_A.hit_gun(bomb):
            gun_A.hp -= 1
            bomb.new_bomb()
            print("BOOM!")
        if gun_B.hit_gun(bomb):
            gun_B.hp -= 1
            bomb.new_bomb()
            print("BOOM!")
    new_N = int(score // 10 + 1)
    for _ in range(new_N - n_targets):
        targets.append(Target())
    n_targets = new_N
    gun_A.power_up()
    gun_B.power_up()

    if gun_A.pistols < 5 and timer % 60 == 0:
        gun_A.pistols += 1
        gun_B.pistols += 1

pg.quit()
if gun_A.hp > gun_B.hp:
    print("unfortunately we lost B player")
elif gun_A.hp < gun_B.hp:
    print("unfortunately we lost A player")
elif gun_A.hp == gun_B.hp and gun_A.hp == 0:
    print("unfortunately we lost both players")

print("YOUR SCORE: ", score)
