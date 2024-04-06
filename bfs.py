from collections import deque
import time


def is_valid(row, col):
    return not (0 <= row < 10) or not (0 <= col < 10)


def neighbouring_cells(queue, row, col, path_length, traversed_node):
    queue.append((row, col + 1, path_length + 1, traversed_node + [(row, col + 1)]))
    queue.append((row + 1, col, path_length + 1, traversed_node + [(row + 1, col)]))
    queue.append((row, col - 1, path_length + 1, traversed_node + [(row, col - 1)]))
    queue.append((row - 1, col, path_length + 1, traversed_node + [(row - 1, col)]))


def bfs(maze):
    start_time = round(time.time() * 1000000)
    visited = set()
    queue = deque([(0, 0, 0, [])])
    grid = maze.grid

    while queue:
        c_row, c_col, path_length, traversed_nodes = queue.popleft()

        # Validate position
        if is_valid(c_row, c_col):
            continue

        if (c_row, c_col) in visited:
            continue

        visited.add((c_row, c_col))

        if grid[c_row][c_col] == 'X':
            continue

        # Check if the goal is reached
        if grid[c_row][c_col][0] == 'G':
            maze.solutionPathLength = path_length
            maze.solutionMaze = traversed_nodes
            maze.executionTime = round(time.time() * 1000000) - start_time
            maze.isGoalReached = True

            return True

        # Add neighbouring cells to queue
        neighbouring_cells(queue, c_row, c_col, path_length, traversed_nodes)
        maze._nodesVisited += 1

    # No solution
    maze.isGoalReached = False
    maze.executionTime = round(time.time() * 1000000) - start_time
    maze.solutionMaze = traversed_nodes

    return False
