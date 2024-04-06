import heapq
import time


def is_valid(row, col):
    return not (0 <= row < 10) or not (0 <= col < 10)


def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


def neighbouring_cells(open_list, row, col, goal, path_length, traversed_node):
    heapq.heappush(open_list,
                   (heuristic((row, col - 1), goal), row, col - 1, path_length + 1, traversed_node + [(row, col - 1)]))
    heapq.heappush(open_list,
                   (heuristic((row - 1, col), goal), row - 1, col, path_length + 1, traversed_node + [(row - 1, col)]))
    heapq.heappush(open_list,
                   (heuristic((row, col + 1), goal), row, col + 1, path_length + 1, traversed_node + [(row, col + 1)]))
    heapq.heappush(open_list,
                   (heuristic((row + 1, col), goal), row + 1, col, path_length + 1, traversed_node + [(row + 1, col)]))


def astar(maze, start, goal):
    start_time = round(time.time() * 1000000)
    closed_set = set()
    grid = maze.grid

    open_list = [(heuristic(start, goal), 0, 0, 0, [])]

    while open_list:
        _, c_row, c_col, path_length, traversed_nodes = heapq.heappop(open_list)
        c_position = (c_row, c_col)

        if c_position in closed_set:
            continue

        closed_set.add(c_position)

        # Validate position
        if is_valid(c_row, c_col):
            continue

        if grid[c_row][c_col] == 'X':
            continue

        if grid[c_row][c_col] == 'G':
            maze.isGoalReached = True
            maze.executionTime = round(time.time() * 1000000) - start_time
            maze.solutionMaze = traversed_nodes
            maze.solutionPathLength = path_length
            return True

        # open_list.remove((heuristic(c_position, goal), c_row, c_col, path_length, traversed_nodes))
        # closed_set.add(c_position)

        neighbouring_cells(open_list, c_row, c_col, goal, path_length, traversed_nodes)
        maze.nodesVisited += 1

    maze.isGoalReached = False
    maze.executionTime = round(time.time() * 1000000) - start_time
    maze.solutionMaze = traversed_nodes

    return False
