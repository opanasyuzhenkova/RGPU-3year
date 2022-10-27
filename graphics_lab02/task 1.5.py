import sys
import numpy as np
import pprint as pprn
import pygame
from pygame.locals import *

COLOR_RED = (178, 41, 41)
COLOR_GREEN = (16, 132, 32)
COLOR_BLUE = (95, 152, 166)
COLOR_DARKBLUE = (0, 0, 139)
COLOR_DARKGREEN = (0, 139, 0)
COLOR_DARKRED = (139, 0, 0)

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1266, 688))
window.fill((255, 255, 255))
my_game_font = pygame.font.SysFont('Arial', 15)
pygame.display.update()

cood_shift = 200

L = np.array([
    [8, 1],
    [7, 3],
    [6, 2],
]) * 60
print(f"Массив координат отрезков L =")
pprn.pprint(L)

L_shifted = np.copy(L) + cood_shift

pygame.draw.lines(window, COLOR_DARKBLUE, True, L_shifted, 6)
pygame.display.update()

T = np.array([
    [0, 1],
    [1, 0]
])
print('Матрица T =')
pprn.pprint(T)

L_new = L @ T
print('Новые координаты точки L_new =')
pprn.pprint(L_new)

L_new_shifted = np.copy(L_new) + cood_shift

pygame.draw.lines(window, COLOR_DARKRED, True, L_new_shifted, 6)

pygame.display.update()

pygame.draw.line(window, COLOR_DARKGREEN, [0, 0], [1000, 1000], 3)
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
