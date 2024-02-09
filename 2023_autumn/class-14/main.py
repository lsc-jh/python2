import pygame
import os
import random
import math

from pygame.rect import Rect

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
METEOR_IMAGE = pygame.image.load(os.path.join('Assets', 'meteor.png'))

def get_meteor_image():
    return pygame.transform.rotate(pygame.transform.scale(METEOR_IMAGE, (50, 50)), 90)

METEOR_1 = get_meteor_image()
METEOR_2 = get_meteor_image()
METEOR_3 = get_meteor_image()

METEOR_VEL = 2
METEOR_1_DIR = random.randint(0, 359)
METEOR_2_DIR = random.randint(0, 359)
METEOR_3_DIR = random.randint(0, 359)
METEOR_1_X_VEL = math.cos(METEOR_1_DIR) * METEOR_VEL
METEOR_1_Y_VEL = math.sin(METEOR_1_DIR) * METEOR_VEL
METEOR_2_X_VEL = math.cos(METEOR_2_DIR) * METEOR_VEL
METEOR_2_Y_VEL = math.sin(METEOR_2_DIR) * METEOR_VEL
METEOR_3_X_VEL = math.cos(METEOR_3_DIR) * METEOR_VEL
METEOR_3_Y_VEL = math.sin(METEOR_3_DIR) * METEOR_VEL

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
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -15:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.height -15 < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > -10:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT:
        yellow.y += VEL


def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL + 15 > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.height - 35 < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > -10:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT:
        red.y += VEL


def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteors): # uj a `meteors`
    WINDOW.blit(SPACE, (0, 0))
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(f"Health: " + str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render(f"Health: " + str(yellow_health), True, WHITE)
    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))
    
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    # innen
    images = [METEOR_1, METEOR_2, METEOR_3]
    for index in range(0, len(meteors)):
        WINDOW.blit(images[index], (meteors[index].x, meteors[index].y))
    # eddig
    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    pygame.display.update()

def check_meteor_coll(meteors, ship: Rect, event):
    for meteor in meteors:
        if ship.colliderect(meteor):
            meteor.x = 480
            meteor.y = 240
            pygame.event.post(pygame.event.Event(event))


def handle_bullets(yellow_bullets, red_bullets, yellow: Rect, red: Rect, meteor_1: Rect, meteor_2:Rect, meteor_3: Rect):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        elif meteor_1.colliderect(bullet) or meteor_2.colliderect(bullet) or meteor_3.colliderect(bullet):
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
        elif meteor_1.colliderect(bullet) or meteor_2.colliderect(bullet) or meteor_3.colliderect(bullet):
            red_bullets.remove(bullet)

    check_meteor_coll([meteor_1, meteor_2, meteor_3], yellow, YELLOW_HIT)
    check_meteor_coll([meteor_1, meteor_2, meteor_3], red, RED_HIT)

def position_meteor(meteor, x, y):
    meteor.x += x
    meteor.y += y
    
    if meteor.x > 999:
        meteor.x = 1
    if meteor.x < 1:
        meteor.x = 999
    if meteor.y > 499:
        meteor.y = 1
    if meteor.y < 1:
        meteor.y = 499

def move_meteors(meteor_1, meteor_2, meteor_3):
    position_meteor(meteor_1, METEOR_1_X_VEL, METEOR_1_Y_VEL)
    position_meteor(meteor_2, METEOR_2_X_VEL, METEOR_2_Y_VEL)
    position_meteor(meteor_3, METEOR_3_X_VEL, METEOR_3_Y_VEL)

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    meteor_1 = pygame.Rect(480, 240, 50, 50)
    meteor_2 = pygame.Rect(480, 240, 50, 50)
    meteor_3 = pygame.Rect(480, 240, 50, 50)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

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
        move_meteors(meteor_1, meteor_2, meteor_3)
        drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, [meteor_1, meteor_2, meteor_3])
    pygame.quit()


if __name__ == "__main__":
    main()
