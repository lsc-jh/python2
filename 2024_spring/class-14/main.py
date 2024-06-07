import pygame as py
import random

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

        self.jumping = False

    def jump(self, _platforms):
        hits = py.sprite.spritecollide(self, _platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def move(self):
        self.acc = vector(0, ACC)
        pressed_keys = py.key.get_pressed()
        if pressed_keys[py.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[py.K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + ACC * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

    def update(self, _platforms):
        hits = py.sprite.spritecollide(self, _platforms, False)
        if hits and self.vel.y > 0:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jumping = False
        self.rect.midbottom = self.pos


class Platform(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = py.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        _w = random.randint(0, WIDTH - 10)
        _h = random.randint(0, HEIGHT - 30)
        self.rect = self.surf.get_rect(center=(_w, _h))


def check(platform, _platforms):
    if py.sprite.spritecollideany(platform, _platforms):
        return False
    else:
        for p in _platforms:
            if p == platform:
                continue
            space_top = abs(platform.rect.top - p.rect.bottom)
            space_bottom = abs(platform.rect.bottom - p.rect.top)
            if space_top < 50 and space_bottom < 50:
                return False
        return True


def platform_generator(_platforms, _all_sprites):
    while len(_platforms) < 7:
        width = random.randrange(50, 100)
        p = Platform()
        is_ok = False
        while not is_ok:
            p = Platform()
            w = random.randrange(0, WIDTH - width)
            h = random.randrange(-50, 0)
            p.rect.center = (w, h)
            is_ok = check(p, _platforms)
        _platforms.add(p)
        _all_sprites.add(p)


ground = Platform()
ground.surf = py.Surface((WIDTH, 20))
ground.surf.fill((255, 0, 0))
ground.rect = ground.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
player1 = Player()

all_sprites = py.sprite.Group()
all_sprites.add(player1)
all_sprites.add(ground)

platforms = py.sprite.Group()
platforms.add(ground)

for i in range(random.randint(5, 6)):
    _is_ok = False
    platform = Platform()
    while not _is_ok:
        platform = Platform()
        _is_ok = check(platform, platforms)
    platforms.add(platform)
    all_sprites.add(platform)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                player1.jump(platforms)
        if event.type == py.KEYUP:
            if event.key == py.K_SPACE:
                player1.cancel_jump()
    displaySurface.fill((0, 0, 0))

    if player1.rect.top <= HEIGHT / 3:
        player1.pos.y += abs(player1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(player1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()
    for entity in all_sprites:
        displaySurface.blit(entity.surf, entity.rect)
    player1.move()
    player1.update(platforms)
    platform_generator(platforms, all_sprites)
    py.display.update()
    framesPerSec.tick(FPS)
