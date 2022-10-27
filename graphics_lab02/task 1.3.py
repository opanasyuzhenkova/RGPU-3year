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

cood_shift = 200

L = np.array([
    [-1 / 2, 3 / 2],
    [3, -2],
    [-1, -1],
    [3, 5 / 3],
]) * 100
print(f"Массив координат отрезков L =")
pprn.pprint(L)

L_shifted = np.copy(L) + cood_shift

for i in range(0, 4, 2):
    color = COLOR_DARKBLUE if i == 0 else COLOR_BLUE
    line_width = 6 if i == 0 else 3
    pygame.draw.line(window, color, L_shifted[0 + i, :], L_shifted[1 + i, :], line_width)
    window.blit(
        my_game_font.render(f"L_1({L_shifted[0 + i, 0]:.3f}, {L_shifted[0 + i, 1]:.3f})", True, COLOR_DARKBLUE),
        (L_shifted[0 + i, :] + 5)
    )
    window.blit(
        my_game_font.render(f"L_2({L_shifted[1 + i, 0]:.3f}, {L_shifted[1 + i, 1]:.3f})", True, COLOR_DARKBLUE),
        (L_shifted[1 + i, :] + 5)
    )

pygame.display.update()

T = np.array([
    [1, 2],
    [1, -3]
])
print('Матрица T =')
pprn.pprint(T)

L_new = L @ T
print('Новые координаты точки L_new =')
pprn.pprint(L_new)

L_new_shifted = np.copy(L_new) + cood_shift

for i in range(0, 4, 2):
    color = COLOR_DARKRED if i == 0 else COLOR_RED
    line_width = 6 if i == 0 else 3
    pygame.draw.line(window, color, L_new_shifted[0 + i, :], L_new_shifted[1 + i, :], line_width)
    window.blit(
        my_game_font.render(f"L_1_new({L_new_shifted[0 + i, 0]:.3f}, {L_new_shifted[0 + i, 1]:.3f})", True,
                            COLOR_DARKRED), (L_new_shifted[0 + i, :] + 5),
    )
    window.blit(
        my_game_font.render(f"L_2_new({L_new_shifted[1 + i, 0]:.3f}, {L_new_shifted[1 + i, 1]:.3f})", True,
                            COLOR_DARKRED), (L_new_shifted[1 + i, :] + 5)
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
