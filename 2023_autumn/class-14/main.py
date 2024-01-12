import pygame
import os

WIDTH = 900
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(SIZE)

SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60
VEL = 5

YELLOW_S_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_S_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

RED_S_START = pygame.transform.rotate(
    pygame.transform.scale(RED_S_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270
)

YELLOW_S_START = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_S_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90
) 

# Colors
WHITE = (255, 255, 255)

def drawWindow(red, yellow):
    WINDOW.fill(WHITE)
    WINDOW.blit(YELLOW_S_START, (yellow.x, yellow.y))   
    WINDOW.blit(RED_S_START, (red.x, red.y))   
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        drawWindow(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()

