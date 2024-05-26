# This is the main file.
import random
import pygame as pg
r = ['hor', 'ver']
pg.init()
screen = pg.display.set_mode((500, 500))
bg = pg.Surface(screen.get_size())
bg.fill((255, 255, 255))
kitten = pg.image.load('cutecat.png')
wallimage = pg.image.load('wall.png')
wall2image = pg.image.load('wall2.png')
wnse = 's'

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = kitten
        self.rect = [10, 10]



class Wall(pg.sprite.Sprite):
    def __init__(self, rect, rotate):
        super(Wall, self).__init__()
        self.rotate = rotate
        if self.rotate == 'ver':
            self.surf = wall2image
        elif self.rotate == 'hor':
            self.surf = wallimage
        self.rect = rect


player = Player()
wall1 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall2 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall3 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall4 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall5 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall6 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall7 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall8 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall9 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall10 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall11 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall12 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall13 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall14 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall15 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall16 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall17 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall18 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall19 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall20 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall21 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall22 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall23 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall24 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wall25 = Wall((random.randint(10, 450), random.randint(10, 450)), random.choice(r))
wlist = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15,
         wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25]
pg.display.flip()
r = True
while r:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            r = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP: wnse = 'up'
            if event.key == pg.K_DOWN: wnse = 'down'
            if event.key == pg.K_RIGHT: wnse = 'right'
            if event.key == pg.K_LEFT: wnse = 'left'
        elif event.type == pg.KEYUP: wnse = 's'
    if wnse == 'up':
        if 0 < player.rect[1] - 5 < 475:
            player.rect[1] -= 0.1
    elif wnse == 'down':
        if 0 < player.rect[1] + 5 < 475:
            player.rect[1] += 0.1
    elif wnse == 'right':
        if 0 < player.rect[0] + 5 < 475:
            player.rect[0] += 0.1
    elif wnse == 'left':
        if 0 < player.rect[0] - 5 < 475:
            player.rect[0] -= 0.1
    everyone = pg.sprite.Group
    walls = pg.sprite.Group
    screen.blit(bg, (0, 0))
    screen.blit(player.surf, player.rect)
    for i in range(len(wlist)):
        screen.blit(wlist[i].surf, wlist[i].rect)
    pg.display.update()
pg.quit()

