import pygame

pygame.init()

WIDTH = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Grid")

DARK_RED = (139, 0, 0)
SPRING_GREEN = (0, 255, 127)
NAVY_BLUE = (0, 0, 128)
AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
MEDIUM_ORCHID = (186, 85, 211)


class Node:
    def __init__(self, row, col, width, total_rows, color=WHITE):
        self.row = row
        self.col = col
        self.color = color
        if row == 0 or col == 0 or row == total_rows - 1 or col == total_rows - 1:
            self.color = BLACK
        self.width = width
        self.total_rows = total_rows
        self.neighbour = []
        self.visited = False

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == WHITE

    def is_closed(self):
        return self.color == AQUA

    def is_open(self):
        return self.color == SPRING_GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == NAVY_BLUE

    def is_end(self):
        return self.color == DARK_RED

    def make_start(self):
        self.color = NAVY_BLUE

    def make_closed(self):
        self.color = AQUA

    def make_open(self):
        self.color = SPRING_GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = DARK_RED

    def make_current(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.row * self.width, self.col * self.width, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbour = []

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # right
            self.neighbour.append(grid[self.row][self.col + 1])

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # down
            self.neighbour.append(grid[self.row + 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # left
            self.neighbour.append(grid[self.row][self.col - 1])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # up
            self.neighbour.append(grid[self.row - 1][self.col])

    def check_neighbours_gap(self, grid, offset):  # for the maze generator
        neighbours = []
        offset = 4
        if self.row < self.total_rows - offset and not grid[self.row + offset][self.col].is_visited():
            neighbours.append(grid[self.row + offset][self.col])

        if self.row > 1 and not grid[self.row - offset][self.col].is_visited():
            neighbours.append(grid[self.row - offset][self.col])

        if self.col < self.total_rows - offset and not grid[self.row][self.col + offset].is_visited():
            neighbours.append(grid[self.row][self.col + offset])

        if self.col > 1 and not grid[self.row][self.col - offset].is_visited():
            neighbours.append(grid[self.row][self.col - offset])

        return neighbours

    def reset(self):
        self.color = WHITE

#
# gap = 20
# WIDTH = 700
# total_rows_on_grid = 35  # total number of rows in the window
# LENGTH = 1150
