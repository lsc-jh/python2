import pygame
import os

WIDTH = 900
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode(SIZE)

# Colors

WHITE = (255, 255, 255)

def drawWindow(red, yellow):
    WINDOW.fill(WHITE)
    
    pygame.display.update()


def main():
    
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()


if __name__ == "__main__":
    main()

