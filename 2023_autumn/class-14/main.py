import pygame
import os

pygame.mixer.init()
pygame.font.init()

WIDTH = 900
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space fight")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'explosion.wav'))
FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'laser.wav'))

HEALTH_FONT = pygame.font.SysFont('arial', 40)

FPS = 60
VEL = 5
BULLET_VEL = 7 # uj
MAX_BULLETS = 3 # uj
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT)
)

def yellow_control(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:
        yellow.y += VEL


def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VEL
    if keys_pressed[pygame.K_UP]:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        red.y += VEL


def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WINDOW.blit(SPACE, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(f"Health: " + str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render(f"Health: " + str(yellow_health), True, WHITE)
    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))
    
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # yellow.x += 1
        keys_pressed = pygame.key.get_pressed()
        red_control(keys_pressed, red)
        yellow_control(keys_pressed, yellow)
        drawWindow(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
