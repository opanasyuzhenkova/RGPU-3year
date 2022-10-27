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
    [50, 100],
    [250, 200],
    [50, 200],
    [250, 300],
])
print(f"Массив координат отрезка L =")
pprn.pprint(L)

m1 = (L[1, 1] - L[0, 1]) / (L[1, 0] - L[0, 0])
print(f"Начальный наклон по первому отрезку m1 = {m1:.3f}")

for i in range(0, 4, 2):
    pygame.draw.line(window, COLOR_DARKBLUE, L[0 + i, :], L[1 + i, :], 6)
    window.blit(
        my_game_font.render(f"L_1({L[0 + i, 0]}, {L[0 + i, 1]})", True, COLOR_DARKBLUE), L[0 + i, :] + 5
    )
    window.blit(
        my_game_font.render(f"L_2({L[1 + i, 0]}, {L[1 + i, 1]})", True, COLOR_DARKBLUE), L[1 + i, :] + 5
    )

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

m2 = (L_new[1, 1] - L_new[0, 1]) / (L_new[1, 0] - L_new[0, 0])
print(f"Наклон по новому отрезку m2 = {m2:.3f}")

a = T[0, 0]
b = T[0, 1]
c = T[1, 0]
d = T[1, 1]
m2_check = (b + d * m1) / (a + c * m1)
print(f"Проверка m2 по формуле: {m2_check:.3f}")

for i in range(0, 4, 2):
    pygame.draw.line(window, COLOR_DARKRED, L_new[0 + i, :], L_new[1 + i, :], 6)
    window.blit(
        my_game_font.render(f"L_1_new({L_new[0 + i, 0]}, {L_new[0 + i, 1]})", True, COLOR_DARKRED), L_new[0 + i, :] + 5
    )
    window.blit(
        my_game_font.render(f"L_2_new({L_new[1 + i, 0]}, {L_new[1 + i, 1]})", True, COLOR_DARKRED), L_new[1 + i, :] + 5
    )

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