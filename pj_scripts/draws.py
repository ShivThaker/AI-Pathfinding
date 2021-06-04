import pygame

fpsClock = pygame.time.Clock()


def draw(win, grid, width, gap):
    for row in grid:
        for node in row:
            node.draw(win)

    for i in range(0, width, gap):
        pygame.draw.line(win, (0, 0, 0), (0, i), (width, i))
        pygame.draw.line(win, (0, 0, 0), (i, 0), (i, width))
    pygame.display.update()
    fpsClock.tick(60)


def py_update_fun():
    pygame.display.update()
    fpsClock.tick(60)
