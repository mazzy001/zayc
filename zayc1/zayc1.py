import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x, y = 200, 200
width, height = 200, 400
color = (200, 200, 200)

body_width = width // 2
body_height = height // 2
body_y = y + body_height // 2
ellipse(screen, color, (x - body_width // 2, body_y - body_height // 2, body_width, body_height))

head_size = height // 4
circle(screen, color, (x, y - head_size // 2), head_size // 2)

ear_height = height // 3
ear_y = y - height // 2 + ear_height // 2
for ear_x in (x - head_size // 4, x + head_size // 4):
    ellipse(screen, color, (ear_x - (width // 8) // 2, ear_y - ear_height // 2, width // 8, ear_height))

leg_height = height // 16
leg_y = y + height // 2 - leg_height // 2
for leg_x in (x - width // 4, x + width // 4):
    ellipse(screen, color, (leg_x - (width // 4) // 2, leg_y - leg_height // 2, width // 4, leg_height))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()