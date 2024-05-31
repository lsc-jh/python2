import pygame as py

py.init()
vector = py.math.Vector2

HEIGHT, WIDTH = 450, 400
ACC = 0.5
FRIC = -0.12
FPS = 60

framesPerSec = py.time.Clock()
displaySurface = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Platformer")


class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = py.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))
        self.pos = vector((10, 420))
        self.vel = vector((0, 0))
        self.acc = vector((0, 0))