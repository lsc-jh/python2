import pygame

pygame.init()

dis = pygame.display.set_mode((400, 300))
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

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('Arial', 50)

def message(msg, color):
    text = font_style.render(msg, True, color)
    dis.blit(text, [dis.get_width() / 2, dis.get_height() / 2])

game_over = False

def move(key):
    global x1_change, y1_change
    if key == pygame.K_LEFT:
        x1_change = -snake_block
        y1_change = 0
    elif key == pygame.K_RIGHT:
        x1_change = snake_block
        y1_change = 0
    elif key == pygame.K_UP:
        y1_change = -snake_block
        x1_change = 0
    elif key == pygame.K_DOWN:
        y1_change = snake_block
        x1_change = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            move(event.key)
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()  # Ez itt volt
    clock.tick(30)

pygame.quit()
quit()
