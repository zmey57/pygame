# This is the main file.
import pygame as pg
pg.init()
screen = pg.display.set_mode([500, 500])
screen.fill([255, 255, 255])
kitten = pg.image.load('cutecat.png')
wall = pg.image.load('wall.png')
wall2 = pg.image.load('wall2.png')


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = kitten
        self.rect = self.surf.get_rect()
        screen.blit(self.surf, self.rect)


class Wall(pg.sprite.Sprite):
    def __init__(self, rect, rotate):
        super(Wall, self).__init__()
        self.rotate = rotate
        if self.rotate == 'ver':
            self.surf = wall2
        elif self.rotate == 'hor':
            self.surf = wall
        self.rect = rect
        screen.blit(self.surf, self.rect)


player = Player()
wall = Wall((250, 250), 'hor')

pg.display.flip()
r = True
while r:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            r = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.rect.move_ip(0, 5)
            if event.key == pg.K_DOWN:
                player.rect.move_ip(0, -5)
            if event.key == pg.K_RIGHT:
                player.rect.move_ip(5, 0)
            if event.key == pg.K_LEFT:
                player.rect.move_ip(-5, 0)
    pg.display.update()
pg.quit()
