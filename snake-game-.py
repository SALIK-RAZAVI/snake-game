import pygame
import random

pygame.init()

width, height = 650, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


snake_size = 20
snake_speed = 15


clock = pygame.time.Clock()


font_style = pygame.font.SysFont(None, 50)


def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, green, [pixel[0], pixel[1], snake_size, snake_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_pixels = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(black)
            message("You Lost! Press Q-Quit or P-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_pixels.append(snake_head)
        if len(snake_pixels) > length_of_snake:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == snake_head:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
