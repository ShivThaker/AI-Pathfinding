from pj_scripts.node import *
from pj_scripts import draws


def self_make(win):
    gap = 20
    width = 700
    total_rows_on_grid = 35
    grid = [[Node(i, j, gap, total_rows_on_grid) for j in range(total_rows_on_grid)] for i in range(total_rows_on_grid)]

    start = None
    end = None
    run = True

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
                    elif node != end and node != start:
                        node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                i, j = pygame.mouse.get_pos()
                i //= gap
                j //= gap
                if 0 < i < total_rows_on_grid - 1 and 0 < j < total_rows_on_grid - 1:
                    node = grid[i][j]
                    if node == start:
                        start = None
                    elif node == end:
                        end = None
                    node.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    return grid, start, end, width, gap

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = [[Node(i, j, gap, total_rows_on_grid) for j in range(total_rows_on_grid)] for i in range(total_rows_on_grid)]
