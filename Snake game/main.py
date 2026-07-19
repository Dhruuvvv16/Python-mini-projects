import random
import sys

import pygame

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

BLACK = (15, 15, 15)
GREEN = (0, 200, 0)
LIGHT_GREEN = (100, 255, 100)
RED = (220, 50, 50)
WHITE = (240, 240, 240)

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
OPPOSITE = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}


def move_snake(snake, direction):
    """Move the snake forward by one cell (same length)."""
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    return [new_head] + snake[:-1]


def grow_snake(snake, direction):
    """Move the snake forward and keep the tail (snake gets longer)."""
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    return [new_head] + snake


def check_wall_collision(head, width, height):
    x, y = head
    return x < 0 or x >= width or y < 0 or y >= height


def check_self_collision(snake):
    return snake[0] in snake[1:]


def spawn_food(snake, width, height):
    while True:
        pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        if pos not in snake:
            return pos


def draw_cell(surface, position, color):
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, BLACK, rect, 1)

