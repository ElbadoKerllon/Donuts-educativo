import pygame
import math

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

# Cálculo de 'rows' e 'columns' corrigido
rows = HEIGHT // y_separator
columns = WIDTH // x_separator

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

chars = ".,-:;=!*&^%^$#@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)


def text_display(letter, x, y):
    text = font.render(str(letter), True, white)
    screen.blit(text, (x, y))


run = True
while run:
    screen.fill(black)
    z = [0] * (rows * columns)
    b = [' '] * (rows * columns)

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = x + columns * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y > 0 and columns > x > 0 and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    x_start, y_start = 0, 0  # Reset das coordenadas de início

    for i in range(len(b)):
        A += 0.00002
        B += 0.00001
        if i == 0 or i % columns == 0:
            y_start += y_separator
            x_start = 0
        text_display(b[i], x_start, y_start)
        x_start += x_separator

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False