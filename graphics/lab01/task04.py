import sys
import numpy as np
import pprint as pprn
import pygame
from pygame.locals import *

COLOR_RED = (204, 0, 0)
COLOR_GREEN = (51, 153, 51)
COLOR_BLACK = (0, 0, 255)

t = np.array([[1, 3], [4, 1]])
print('Матрица преобразования T = ', end = '')
pprn.pprint(t)

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500, 500))
window.fill((153, 153, 102))
my_font = pygame.font.SysFont('Arial', 12)
pygame.display.update()

l_coord_lst = list()
print('Введите координаты первой точки: ')
l_coord_lst = [float(input(f"Координата номер {i + 1} : ")) for i in range(2)]
# print(x_coord_lst)

l_coord_lst2 = list()
print('Введите координаты второй точки: ')
l_coord_lst2 = [float(input(f"Координата номер {i + 1} : ")) for i in range(2)]

l = np.array([l_coord_lst, l_coord_lst2])
print(f"Массив координат отрезка l = ")
pprn.pprint(l)

pygame.draw.line(window, COLOR_GREEN, l[0, :], l[1, :], 6)
pygame.display.update()

lbl1 = my_font.render(f"l1({l[0, 0]}, {l[0, 1]})", True, COLOR_GREEN)
lbl2 = my_font.render(f"l2({l[1, 0]}, {l[1, 1]})", True, COLOR_GREEN)
window.blit(lbl1, l[0, :] + 5)
window.blit(lbl2, l[1, :] + 5)
pygame.display.update()

l_new = l@t
print('Новые координаты: ')
pprn.pprint(l_new)
pygame.draw.line(window, COLOR_RED, l_new[0, :], l_new[1, :], 6)
pygame.display.update()
lbl1_new = my_font.render(f"l1_new({l_new[0, 0]}, {l_new[0, 1]})", True, COLOR_RED)
lbl2_new = my_font.render(f"l2_new({l_new[1, 0]}, {l_new[1, 1]})", True, COLOR_RED)
window.blit(lbl1_new, l_new[0, :] + 5)
window.blit(lbl2_new, l_new[1, :] + 5)
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