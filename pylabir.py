import pygame as pg
import random
pg.init()
screen = pg.display.set_mode([500, 500])
screen.fill([255, 255, 255])
print(random.random() * 7)
plim = 'player_sprite.png'


class Player(pg.sprite.Sprite):
    def __init__(self, name):
        super(Player, self).__init__()
        self.__surf = pg.surface.Surface((75, 25))
        self.__name = name
        self.__image = pg.image.load(plim)

    def move(self):
        pass


class Wall:
    def __init__(self, width, height, x, y, image):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__image = image


player = Player('idkwhattoput')
pg.display.flip()
r = True
while r:
    screen.blit(player.__surf)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            r = False

    pk = pg.key.get_pressed()

pg.quit()
