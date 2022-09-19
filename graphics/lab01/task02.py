import sys
import numpy as np
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Arial', 25)
window = pygame.display.set_mode((500, 500))
window.fill((153, 153, 102))
pygame.display.update()

pygame.draw.circle(window, (51, 102, 0), [200, 200], 15, 0)

pygame.draw.line(window, (0, 0, 0), [200, 0], [200, 200], 10) # цвет, 1т, 2т, ширина линии
pygame.draw.line(window, (0, 0, 0), [200, 300], [200, 500], 10) # цвет, 1т, 2т, ширина линии

text = my_font.render('hi, i am just a text', False, (255, 255, 255))
window.blit(text, (200, 240))
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