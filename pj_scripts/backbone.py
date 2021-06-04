from pj_scripts import manual_grid, draws, recursive_bactracker
from mazes_oh_yeaa import gap_2
from big_grid import predefined_grid
from tries.button import *
# from pj_scripts.node import *
from pathf_algos import astar, bfs, dfs


GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_CYAN = (0, 139, 139)
MAROON = (128, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_CYAN = (224, 255, 255)

win = pygame.display.set_mode((1150, 710))
pygame.display.set_caption("AI Project")
win.fill(LIGHT_CYAN)
pygame.draw.rect(win, BLACK, (0, 0, 710, 710), 0)

run = True
grid = None
start = None
end = None

while run or True:
    if run and True:
        maze_1.draw(win)
        maze_2.draw(win)
        maze_3.draw(win)
        title("Choose Your", 700, 0, 450, 90, win)
        title("MAZE!", 700, 70, 450, 90, win)
        draws.py_update_fun()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if maze_1.isOver(pos):
                    grid, start, end, width, gap = predefined_grid.sample_grid(win)
                    print("Sample grid displayed - offset 1")
                    win.fill(LIGHT_CYAN)
                    pygame.draw.rect(win, BLACK, (0, 0, 710, 710), 0)
                    pygame.draw.rect(win, LIGHT_CYAN, (0, 710, 1150, 710), 0)
                    run = False

                if maze_2.isOver(pos):
                    grid, start, end, width, gap = gap_2.make_maze(win, 4)
                    print("Maze offset size 3 generated")
                    win.fill(LIGHT_CYAN)
                    pygame.draw.rect(win, BLACK, (0, 0, 710, 710), 0)
                    pygame.draw.rect(win, LIGHT_CYAN, (0, 710, 1150, 710), 0)
                    run = False

                if maze_3.isOver(pos):
                    grid, start, end, width, gap = manual_grid.self_make(win)
                    print("Manually maze generated")
                    win.fill(LIGHT_CYAN)
                    pygame.draw.rect(win, BLACK, (0, 0, 710, 710), 0)
                    pygame.draw.rect(win, LIGHT_CYAN, (0, 710, 1150, 710), 0)
                    run = False

            if event.type == pygame.MOUSEMOTION:
                if maze_1.isOver(pos):
                    maze_1.button_color = MAROON
                    maze_1.text_color = WHITE
                else:
                    maze_1.button_color = DARK_CYAN
                    maze_1.text_color = BLACK

                if maze_2.isOver(pos):
                    maze_2.button_color = MAROON
                    maze_2.text_color = WHITE
                else:
                    maze_2.button_color = DARK_CYAN
                    maze_2.text_color = BLACK

                if maze_3.isOver(pos):
                    maze_3.button_color = MAROON
                    maze_3.text_color = WHITE
                else:
                    maze_3.button_color = DARK_CYAN
                    maze_3.text_color = BLACK

    if not run:
        draws.draw(win, grid, width, gap)
        algo_1.draw(win)
        algo_2.draw(win)
        algo_3.draw(win)
        title("Choose Your", 700, 0, 450, 90, win)
        title("ALGORITHM!", 700, 70, 450, 90, win)
        draws.py_update_fun()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if algo_1.isOver(pos):
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    astar.algorithm(lambda: draws.draw(win, grid, width, gap), grid, start, end)
                    print("A* running")
                    pass

                if algo_2.isOver(pos):
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    bfs.algorithm(lambda: draws.draw(win, grid, width, gap), grid, start, end)
                    print("BFS running")

                if algo_3.isOver(pos):
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    dfs.algorithm(lambda: draws.draw(win, grid, width, gap), grid, start, end)
                    print("DFS running")

            if event.type == pygame.MOUSEMOTION:
                if algo_1.isOver(pos):
                    algo_1.button_color = MAROON
                    algo_1.text_color = WHITE
                else:
                    algo_1.button_color = DARK_CYAN
                    algo_1.text_color = BLACK

                if algo_2.isOver(pos):
                    algo_2.button_color = MAROON
                    algo_2.text_color = WHITE
                else:
                    algo_2.button_color = DARK_CYAN
                    algo_2.text_color = BLACK

                if algo_3.isOver(pos):
                    algo_3.button_color = MAROON
                    algo_3.text_color = WHITE
                else:
                    algo_3.button_color = DARK_CYAN
                    algo_3.text_color = BLACK

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

