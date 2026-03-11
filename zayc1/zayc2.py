import random
import pygame
from pygame.draw import ellipse, circle

pygame.init()

FPS = 30
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 750
BACKGROUND_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_ellipse_centered(surface, color, x, y, width, height):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_circle_centered(surface, color, x, y, radius):
    circle(surface, color, (x, y), radius)


def draw_hare(surface, x, y, width, height, body_color, head_color, ear_color, leg_color):


    body_width = width // 2
    body_height = height // 2
    body_x = x
    body_y = y + body_height // 2

    head_diameter = height // 4
    head_x = x
    head_y = y - head_diameter // 2

    ear_width = width // 8
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    ear_positions = [
        x - head_diameter // 4,
        x + head_diameter // 4
    ]

    leg_width = width // 4
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    leg_positions = [
        x - width // 4,
        x + width // 4
    ]

    draw_ellipse_centered(surface, body_color, body_x, body_y, body_width, body_height)
    draw_circle_centered(surface, head_color, head_x, head_y, head_diameter // 2)

    for ear_x in ear_positions:
        draw_ellipse_centered(surface, ear_color, ear_x, ear_y, ear_width, ear_height)

    for leg_x in leg_positions:
        draw_ellipse_centered(surface, leg_color, leg_x, leg_y, leg_width, leg_height)


def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def generate_hare():
    width = random.randint(60, 180)
    height = width * 2
    x = random.randint(width // 2, SCREEN_WIDTH - width // 2)
    y = random.randint(height // 2, SCREEN_HEIGHT - height // 2)
    return {
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "body_color": random_color(),
        "head_color": random_color(),
        "ear_color": random_color(),
        "leg_color": random_color()
    }


def generate_hares(count):
    hares = []
    for i in range(count):
        hares.append(generate_hare())
    return hares


hares = []

var = int(input("Хотите сами ввести число зайцев (1) или сгенерировать их число случайно (2): "))

if var == 1:
    n = int(input("Введите число зайцев: "))
    hares = generate_hares(n)

if var == 2:
    n = random.randint(1, 1000)
    print("Случайно сгенерировано число зайцев:", n)
    hares = generate_hares(n)


screen.fill(BACKGROUND_COLOR)

for hare in hares:
    draw_hare(
        screen,
        hare["x"],
        hare["y"],
        hare["width"],
        hare["height"],
        hare["body_color"],
        hare["head_color"],
        hare["ear_color"],
        hare["leg_color"]
    )

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()