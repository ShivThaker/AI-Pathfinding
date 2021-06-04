"""
here a pre defined grid is generated
no of rows = 71
width of node = 10

color codes stored in _ file for future use
"""

from pj_scripts.node import *
from pj_scripts import draws


def sample_grid(win):
    gap = 10
    width = 710
    total_rows_on_grid = 71
    grid = [[Node(i, j, gap, total_rows_on_grid, PURPLE) for j in range(total_rows_on_grid)] for i in
            range(total_rows_on_grid)]
    with open("E:\\PycharmProjects\\AI_Pathfinding\\big_grid\\sample_maze.txt", 'r') as f:
        for i in grid:
            for j in i:
                con = f.read(1)
                if len(con) > 0:
                    if con == 'b':
                        j.color = BLACK
                    else:
                        j.color = WHITE
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
