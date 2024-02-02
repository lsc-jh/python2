import pygame
import os
import math
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space fight")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'explosion.wav'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'laser.wav'))

HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

METEOR_WIDTH, METEOR_HEIGHT = 50, 50

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

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

METEOR_IMAGE = pygame.image.load(
    os.path.join('Assets', 'meteor.png'))
METEOR_1 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_2 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_3 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def yellow_control(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -15:  # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width - 15 < BORDER.x:  # right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > -10:  # up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height - 10 < HEIGHT:  # down
        yellow.y += VEL


def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL + 15 > BORDER.x + BORDER.width:  # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width - 15 < WIDTH:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > -10:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height - 10 < HEIGHT:  # down
        red.y += VEL


def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteor_1, meteor_2, meteor_3):
    WINDOW.blit(SPACE, (0, 0))
    # WINDOW.fill(WHITE) - what happens when we don't fit the background at all
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), True, WHITE)
    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))

    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(METEOR_1, (meteor_1.x, meteor_1.y))
    WINDOW.blit(METEOR_2, (meteor_2.x, meteor_2.y))
    WINDOW.blit(METEOR_3, (meteor_3.x, meteor_3.y))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    pygame.display.update()


def handle_bullets(yellow_bullets, red_bullets, yellow, red, meteor_1, meteor_2, meteor_3):
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
    if yellow.colliderect(meteor_1):
        meteor_1.x = 480
        meteor_1.y = 240
        pygame.event.post(pygame.event.Event(YELLOW_HIT))
    if yellow.colliderect(meteor_2):
        meteor_2.x = 480
        meteor_2.y = 240
        pygame.event.post(pygame.event.Event(YELLOW_HIT))
    if yellow.colliderect(meteor_3):
        meteor_3.x = 480
        meteor_3.y = 240
        pygame.event.post(pygame.event.Event(YELLOW_HIT))

    if red.colliderect(meteor_1):
        meteor_1.x = 480
        meteor_1.y = 240
        pygame.event.post(pygame.event.Event(RED_HIT))
    if red.colliderect(meteor_2):
        meteor_2.x = 480
        meteor_2.y = 240
        pygame.event.post(pygame.event.Event(RED_HIT))
    if red.colliderect(meteor_3):
        meteor_3.x = 480
        meteor_3.y = 240
        pygame.event.post(pygame.event.Event(RED_HIT))


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WINDOW.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def meteor_controller(meteor_1, meteor_2, meteor_3):
    # moving the meteors
    meteor_1.x += METEOR_1_X_VEL
    meteor_1.y += METEOR_1_Y_VEL
    meteor_2.x += METEOR_2_X_VEL
    meteor_2.y += METEOR_2_Y_VEL
    meteor_3.x += METEOR_3_X_VEL
    meteor_3.y += METEOR_3_Y_VEL

    # meteor 1 reaches edges
    if meteor_1.x > 999:
        meteor_1.x = 1
    if meteor_1.x < 1:
        meteor_1.x = 999
    if meteor_1.y > 499:
        meteor_1.y = 1
    if meteor_1.y < 1:
        meteor_1.y = 499

    # meteor 2 reaches edges
    if meteor_2.x > 999:
        meteor_2.x = 1
    if meteor_2.x < 1:
        meteor_2.x = 999
    if meteor_2.y > 499:
        meteor_2.y = 1
    if meteor_2.y < 1:
        meteor_2.y = 499

    # meteor 3 reaches edges
    if meteor_3.x > 999:
        meteor_3.x = 1
    if meteor_3.x < 1:
        meteor_3.x = 999
    if meteor_3.y > 499:
        meteor_3.y = 1
    if meteor_3.y < 1:
        meteor_3.y = 499


def main():
    red = pygame.Rect(700, 300, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
    yellow = pygame.Rect(100, 300, SPACESHIP_HEIGHT, SPACESHIP_WIDTH)

    meteor_1 = pygame.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)
    meteor_2 = pygame.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)
    meteor_3 = pygame.Rect(480, 240, METEOR_WIDTH, METEOR_HEIGHT)

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
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        # print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()
        yellow_control(keys_pressed, yellow)
        red_control(keys_pressed, red)
        meteor_controller(meteor_1, meteor_2, meteor_3)

        handle_bullets(yellow_bullets, red_bullets, yellow, red, meteor_1, meteor_2, meteor_3)

        drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteor_1, meteor_2, meteor_3)

    main()


if __name__ == "__main__":
    main()
