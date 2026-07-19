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


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    food = spawn_food(snake, GRID_WIDTH, GRID_HEIGHT)
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not game_over:
                new_direction = {
                    pygame.K_UP: UP, pygame.K_DOWN: DOWN,
                    pygame.K_LEFT: LEFT, pygame.K_RIGHT: RIGHT,
                }.get(event.key)
                if new_direction and new_direction != OPPOSITE[direction]:
                    direction = new_direction
            if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_r:
                snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                direction = RIGHT
                food = spawn_food(snake, GRID_WIDTH, GRID_HEIGHT)
                score = 0
                game_over = False

        if not game_over:
            next_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            if next_head == food:
                snake = grow_snake(snake, direction)
                food = spawn_food(snake, GRID_WIDTH, GRID_HEIGHT)
                score += 1
            else:
                snake = move_snake(snake, direction)

            if check_wall_collision(snake[0], GRID_WIDTH, GRID_HEIGHT) or check_self_collision(snake):
                game_over = True

        screen.fill(BLACK)
        for segment in snake:
            draw_cell(screen, segment, GREEN)
        draw_cell(screen, snake[0], LIGHT_GREEN)
        draw_cell(screen, food, RED)

        score_surface = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (10, 10))

        if game_over:
            msg = font.render("Game Over! Press R to restart", True, WHITE)
            rect = msg.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(msg, rect)

        pygame.display.flip()
        clock.tick(FPS)
