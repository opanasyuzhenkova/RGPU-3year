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
window = pygame.display.set_mode((1266, 668))
window.fill((255, 255, 255))
my_game_font = pygame.font.SysFont('Arial', 15)
pygame.display.update()

L = np.array([
    [0, 100],
    [200, 300]
])
print(f"Массив координат отрезка L =")
pprn.pprint(L)

point_M = np.array(
    [(L[0, 0] + L[1, 0]) / 2, (L[0, 1] + L[1, 1]) / 2]
)
print(f"Координаты середины начального отрезка point_M =")

pygame.draw.line(window, COLOR_BLUE, L[0, :], L[1, :], 6)
pygame.display.update()
label_point_1 = my_game_font.render(f"L_1({L[0, 0]}, {L[0, 1]})", True, COLOR_DARKBLUE)
label_point_2 = my_game_font.render(f"L_2({L[1, 0]}, {L[1, 1]})", True, COLOR_DARKBLUE)
window.blit(label_point_1, (L[0, :] + 5))
window.blit(label_point_2, (L[1, :] + 5))
pygame.display.update()

pygame.draw.circle(window, COLOR_BLUE, point_M, 6, 0)
pygame.display.update()

T = np.array([
    [1, 2],
    [3, 1]
])
print('Матрица T =')
pprn.pprint(T)

L_new = L @ T
print('Новые координаты точки L_new =')
pprn.pprint(L_new)

pygame.draw.line(window, COLOR_RED, L_new[0, :], L_new[1, :], 6)
pygame.display.update()
label_point_1_new = my_game_font.render(f"L_1_new({L_new[0, 0]}, {L_new[0, 1]})", True, COLOR_DARKRED)
label_point_2_new = my_game_font.render(f"L_2_new({L_new[1, 0]}, {L_new[1, 1]})", True, COLOR_DARKRED)
window.blit(label_point_1_new, (L_new[0, :] + 5))
window.blit(label_point_2_new, (L_new[1, :] + 5))
pygame.display.update()

point_M_new = point_M @ T
print(f"Координаты середины нового отрезка point_M_new =")
pprn.pprint(point_M_new)

pygame.draw.circle(window, COLOR_DARKRED, point_M_new, 6, 0)
pygame.display.update()

pygame.draw.line(window, COLOR_DARKGREEN, point_M, point_M_new, 3)

FPS = 30

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)
    pygame.display.update()
