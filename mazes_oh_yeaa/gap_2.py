import math
from collections import deque
from pj_scripts import draws
import random
from pj_scripts.node import *


def remove_wall(a, b, grid, offset):
    if a.row == b.row:
        x = a.row
        y = math.ceil((a.col + b.col) / 2) + offset - 3
        for i in range(offset - 1):
            grid[y][x + i].reset()
    elif a.col == b.col:
        x = math.ceil((a.row + b.row) / 2) + offset - 3
        y = a.col
        for i in range(offset - 1):
            grid[y + i][x].reset()
    return grid


def make_maze(win, offset):
    if offset == 3:
        gap = 10
        width = 700
        total_rows_on_grid = 70
    elif offset == 4:
        gap = 10
        width = 690
        total_rows_on_grid = 69
    grid = [[Node(i, j, gap, total_rows_on_grid, WHITE) for j in range(total_rows_on_grid)] for i in range(total_rows_on_grid)]
    stack = deque()

    for i in range(0, total_rows_on_grid, offset):
        for j in range(total_rows_on_grid):
            grid[i][j].make_barrier()
            grid[j][i].make_barrier()

    for i in range(1, total_rows_on_grid - (offset - 1), offset):
        for j in range(1, total_rows_on_grid - (offset - 1), offset):
            grid[i][j].color = PURPLE

    current = grid[1][1]
    stack.append(current)

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        adjacent = current.check_neighbours_gap(grid, offset)

        if adjacent:
            chosen_one = random.choice(adjacent)
            chosen_one.reset()
            grid = remove_wall(current, chosen_one, grid, offset)
            current.reset()
            current = chosen_one
            if chosen_one not in stack:
                stack.append(chosen_one)
        else:
            current.reset()
            current = stack[-1]
            stack.pop()
        current.make_current()
        draws.draw(win, grid, width, gap)
    current.reset()

    run = True
    start = None
    end = None

    while run:
        draws.draw(win, grid, width, gap)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if pygame.mouse.get_pressed()[0]:
                i, j = pygame.mouse.get_pos()
                i //= gap
                j //= gap
                if i < total_rows_on_grid - 1 and j < total_rows_on_grid - 1:
                    node = grid[i][j]
                    if not start and node != end and not node.is_barrier():
                        start = node
                        start.make_start()
                    elif not end and node != start and not node.is_barrier():
                        end = node
                        end.make_end()

            if pygame.mouse.get_pressed()[2]:
                i, j = pygame.mouse.get_pos()
                i //= gap
                j //= gap
                if 0 < i < total_rows_on_grid - 1 and 0 < j < total_rows_on_grid - 1:
                    node = grid[i][j]
                    if node == start:
                        start = None
                        node.reset()
                    elif node == end:
                        end = None
                        node.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    return grid, start, end, width, gap