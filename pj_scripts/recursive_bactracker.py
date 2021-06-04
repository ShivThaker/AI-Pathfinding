# from pj_scripts import draws
# import random
# from pj_scripts.node import *
#
# PURPLE = (128, 0, 128)
#
#
# def remove_wall(a, b, grid):
#     x = (a.row + b.row) // 2
#     y = (a.col + b.col) // 2
#     grid[x][y].reset()
#     return grid
#
#
# def make_maze(win):
#     grid = [[Node(i, j, gap, total_rows_on_grid, PURPLE) for j in range(total_rows_on_grid)] for i in range(total_rows_on_grid)]
#     stack = []
#     for i in range(0, total_rows_on_grid, 2):
#         for j in range(total_rows_on_grid):
#             grid[i][j].make_barrier()
#             grid[j][i].make_barrier()
#
#     current = grid[1][1]
#     stack.append(current)
#     while stack:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#
#         adjacent = current.check_neighbours_gap1(grid)
#
#         if adjacent:
#             chosen_one = random.choice(adjacent)
#             chosen_one.reset()
#             grid = remove_wall(current, chosen_one, grid)
#             current.reset()
#             current = chosen_one
#             if chosen_one not in stack:
#                 stack.append(chosen_one)
#         else:
#             current.reset()
#             current = stack[-1]
#             stack.remove(stack[-1])
#         current.make_current()
#         draws.draw(win, grid, WIDTH, gap)
#     current.reset()
#
#     run = True
#     start = None
#     end = None
#
#     while run:
#         draws.draw(win, grid, WIDTH, gap)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()
#                 quit()
#
#             if pygame.mouse.get_pressed()[0]:
#                 i, j = pygame.mouse.get_pos()
#                 i //= gap
#                 j //= gap
#                 if i < total_rows_on_grid - 1 and j < total_rows_on_grid - 1:
#                     node = grid[i][j]
#                     if not start and node != end and not node.is_barrier():
#                         start = node
#                         start.make_start()
#                     elif not end and node != start and not node.is_barrier():
#                         end = node
#                         end.make_end()
#
#             if pygame.mouse.get_pressed()[2]:
#                 i, j = pygame.mouse.get_pos()
#                 i //= gap
#                 j //= gap
#                 if 0 < i < total_rows_on_grid - 1 and 0 < j < total_rows_on_grid - 1:
#                     node = grid[i][j]
#                     if node == start:
#                         start = None
#                         node.reset()
#                     elif node == end:
#                         end = None
#                         node.reset()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE and start and end:
#                     return grid, start, end
