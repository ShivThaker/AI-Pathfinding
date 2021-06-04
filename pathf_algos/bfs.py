from collections import deque
import pygame


def backtrace(parent, start, end, draw):
    path = deque([end])
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.popleft().make_end()
    path.pop()
    for node in path:
        node.color = (186, 85, 211)
        draw()


def algorithm(draw, grid, start, end):
    parent = {}
    queue = deque()  # queue will be the double sided Q
    queue.append(start)
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        node = queue.popleft()
        if not node.is_start():
            node.make_closed()
        node.visited = True
        if node == end:
            backtrace(parent, start, end, draw)
            for row in grid:
                for node in row:
                    node.visited = False
            return True
        for adjacent in node.neighbour:  # [node] or [] if not fount, as the 2nd parameter
            if node not in queue and not adjacent.visited:
                if not adjacent.is_end():
                    adjacent.make_open()
                parent[adjacent] = node  # <<<<< record its parent
                queue.append(adjacent)
        draw()
    return False
