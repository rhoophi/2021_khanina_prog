import pygame
import sys
import pygame.draw as draw
import random


class Billy(pygame.sprite.Sprite):
    def __init__(self, start_pos, v, start_direct):
        super().__init__()
        self.pos = pygame.math.Vector2(start_pos)
        self.v = v
        self.direct = pygame.math.Vector2(start_direct)
        self.image = pygame.image.load("billy.png")
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))
        self.rect.center = [start_pos[0], start_pos[1]]

    def reflect(self, NV):
        self.direct = self.direct.reflect(pygame.math.Vector2(NV))

    def update(self):
        self.pos += self.direct * v
        self.rect.center = round(self.pos.x), round(self.pos.y)

        if self.rect.left < 0:
            self.reflect((1, 0))
        if self.rect.right > size_x:
            self.reflect((-1, 0))
        if self.rect.top < 0:
            self.reflect((0, 1))
        if self.rect.bottom > size_y:
            self.reflect((0, -1))


class Whip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("leatherwhip.png")
        self.rect = self.image.get_rect()
        self.hit_sound = pygame.mixer.Sound("slap.mp3")

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def hit(self):
        self.hit_sound.play()
        pygame.sprite.spritecollide(leatherwhip, billies, True)



pygame.init()
clock = pygame.time.Clock()

size_x = 1200
size_y = 800
n_billy = 20
counter = 0

screen = pygame.display.set_mode((size_x, size_y))
background = pygame.image.load("locker_bg.jpg")

pygame.mouse.set_visible(False)

billies = pygame.sprite.Group()

for billy in range(n_billy):
    v, direct = random.randint(-25, 25), (random.random(), random.random())
    new_billy = Billy((random.randint(15, size_x - 15), random.randint(15, size_y - 15)), v, direct)
    billies.add(new_billy)

leatherwhip = Whip()
leatherwhip_group = pygame.sprite.Group()
leatherwhip_group.add(leatherwhip)

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            leatherwhip.hit()
            billy_hit_list = pygame.sprite.spritecollide(leatherwhip, billies, True)
            for billy in billy_hit_list:
                counter += 1
    pygame.display.flip()
    screen.blit(background, (0, 0))
    billies.draw(screen)
    billies.update()
    leatherwhip_group.draw(screen)
    leatherwhip_group.update()
    clock.tick(60)

pygame.quit()
