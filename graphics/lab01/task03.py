import sys
import numpy as np
import pprint as pprn
import pygame
from pygame.locals import *

COLOR_RED = (204, 0, 0)
COLOR_GREEN = (51, 153, 51)
COLOR_BLACK = (0, 0, 255)

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500, 250))
window.fill((153, 153, 102))
my_font = pygame.font.SysFont('Arial', 25)
pygame.display.update()

x_coord_lst = list()
print('Введите координаты двухмерного вектора: ')
x_coord_lst = [float(input(f"Координата номер {i + 1} : ")) for i in range(2)]
# print(x_coord_lst)

x = np.array(x_coord_lst)
print('Массив координат точки Х: ', x)

pygame.draw.circle(window, COLOR_BLACK, x, 6, 0)
lbl_x = my_font.render(f"x ({x[0]}, {x[1]})", False, COLOR_BLACK)
window.blit(lbl_x, (x + 5))
pygame.display.update()

t = np.array([[1, 3], [4, 1]])
print('Матрица преобразования T = ', end = '')
pprn.pprint(t)

x_new = x@t
print('Новые координаты точки X: ', end = '')
pprn.pprint(x_new)
pygame.draw.circle(window, COLOR_RED, x_new, 6, 0)
lbl_x_new = my_font.render(f"x_new ({x_new[0]}, {x_new[1]})", False, COLOR_RED)
window.blit(lbl_x_new, (x_new + 5))
pygame.display.update()

FPS = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)
    pygame.display.update()