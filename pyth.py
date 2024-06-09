import pygame as py
import random
import time
py.init()
screen = py.display.set_mode((500, 500))
bg = py.Surface(screen.get_size())
bg.fill((0, 255, 255))
py.display.flip()
kittenimage = py.image.load('cutecat.png')
rockimage = py.image.load('rock.png')

class Cat:
    def __init__(self):
        super(Cat, self).__init__()
        self.surf = kittenimage
        self.rect = [250, 420]

class Rock:
    def __init__(self):
        super(Rock, self).__init__()
        self.surf = rockimage
        self.rect = [random.randint(0, 470), 0]


cat = Cat()
rocks = py.sprite.Group()
for i in range(5):
    r = Rock()
    rocks.add(r)


r = True
while r:
    screen.blit(bg, (0, 0))
    screen.blit(cat.surf, cat.rect)
    rocks.draw()
    rock.rect[1] += 0.01
    rock2.rect[1] += 0.01
    rock3.rect[1] += 0.01
    rock4.rect[1] += 0.01
    rock5.rect[1] += 0.01
    py.display.update()

    for e in py.event.get():
        if e.type == py.QUIT:
            r = False
py.quit()
'камень падай пж )'
