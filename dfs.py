import time


def is_valid(row, col):
    return not (0 <= row < 10) or not (0 <= col < 10)


def neighbouring_cells(stack, row, col, path_length, traversed_node):
    stack.append((row, col + 1, path_length + 1, traversed_node + [(row, col + 1)]))
    stack.append((row + 1, col, path_length + 1, traversed_node + [(row + 1, col)]))
    stack.append((row, col - 1, path_length + 1, traversed_node + [(row, col - 1)]))
    stack.append((row - 1, col, path_length + 1, traversed_node + [(row - 1, col)]))


def dfs(maze):
    visited = set()
    stack = [(0, 0, 0, [])]
    start_time = round(time.time() * 1000000)
    grid = maze.grid

    while stack:
        c_row, c_col, path_length, traversed_nodes = stack.pop()

        # Validate position
        if is_valid(c_row, c_col):
            continue

        if (c_row, c_col) in visited:
            continue

        visited.add((c_row, c_col))

        if grid[c_row][c_col] == 'X':
            continue

        if grid[c_row][c_col] == 'G':
            maze.isGoalReached = True
            maze.executionTime = round(time.time() * 1000000) - start_time
            maze.solutionMaze = traversed_nodes
            maze.solutionPathLength = path_length

            return True

        neighbouring_cells(stack, c_row, c_col, path_length, traversed_nodes)
        maze._nodesVisited += 1

    maze.solutionMaze = traversed_nodes
    maze.isGoalReached = False
    maze.executionTime = round(time.time() * 1000000) - start_time

    return False
