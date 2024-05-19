# This is the main file.
import pygame as pg
pg.init()
screen = pg.display.set_mode((500, 500))
bg = pg.Surface(screen.get_size())
bg.fill((255, 255, 255))
kitten = pg.image.load('cutecat.png')
wallimage = pg.image.load('wall.png')
wall2image = pg.image.load('wall2.png')


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
wall = Wall((0, -5), 'hor')
wall2 = Wall((100, 100), 'hor')
wall3 = Wall((0, 20), 'hor')
wlist = [wall, wall2, wall3]
screen.blit(player.surf, player.rect)
screen.blit(wall.surf, wall.rect)
pg.display.flip()
r = True
while r:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            r = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if 0 < player.rect[1] < 500 and 0 < player.rect[0] < 500:
                    player.rect[1] -= 5
            if event.key == pg.K_DOWN:
                if 0 < player.rect[1] < 500 and 0 < player.rect[0] < 500:
                    player.rect[1] += 5
            if event.key == pg.K_RIGHT:
                if 0 < player.rect[1] < 500 and 0 < player.rect[0] < 500:
                    player.rect[0] += 5
            if event.key == pg.K_LEFT:
                if 0 < player.rect[1] < 500 and 0 < player.rect[0] < 500:
                    player.rect[0] -= 5
    screen.blit(bg, (0, 0))
    screen.blit(player.surf, player.rect)
    for i in range(len(wlist)):
        screen.blit(wlist[i].surf, wlist[i].rect)
    pg.display.update()
pg.quit()
