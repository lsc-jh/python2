import random

import pygame
import time

pygame.init()

dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Snake')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

x1 = dis.get_width() / 2
y1 = dis.get_height() / 2

snake_block = 20

clock = pygame.time.Clock()
font_style = pygame.font.SysFont('Arial', 25)
score_font = pygame.font.SysFont('Arial', 35)


def print_score(score):
    value = score_font.render('Your Score: ' + str(score), True, black)
    dis.blit(value, [0, 0])


def message(msg, color):
    text = font_style.render(msg, True, color)
    dis.blit(text, [dis.get_width() / 2, dis.get_height() / 2])


def move(key, x1_change, y1_change):
    if key == pygame.K_LEFT:
        if x1_change == snake_block:
            return x1_change, y1_change

        x1_change = -snake_block
        y1_change = 0
    elif key == pygame.K_RIGHT:
        if x1_change == -snake_block:
            return x1_change, y1_change

        x1_change = snake_block
        y1_change = 0
    elif key == pygame.K_UP:
        if y1_change == snake_block:
            return x1_change, y1_change
        y1_change = -snake_block
        x1_change = 0
    elif key == pygame.K_DOWN:
        if y1_change == -snake_block:
            return x1_change, y1_change
        y1_change = snake_block
        x1_change = 0
    return x1_change, y1_change


def food_position():
    food_x = round(random.randrange(0, dis.get_width() - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis.get_height() - snake_block) / snake_block) * snake_block
    return food_x, food_y


def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def game_loop():
    game_over = False
    game_close = False
    x1 = dis.get_width() / 2
    y1 = dis.get_height() / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1

    food_x, food_y = food_position()
    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or R-Restart", red)
            print_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:  # K_c -> K_r
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                x1_change, y1_change = move(event.key, x1_change, y1_change)

        # If we hit the wall
        if x1 >= dis.get_width() or x1 < 0 or y1 >= dis.get_height() or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_list)
        print_score(length_of_snake - 1)

        pygame.display.update()  # Ez itt volt

        if x1 == food_x and y1 == food_y:
            food_x, food_y = food_position()
            length_of_snake += 1

        clock.tick(30)

    pygame.quit()
    quit()


game_loop()
