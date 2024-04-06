import csv
import os
import random
from math import ceil
from time import sleep

from astar import astar
from bfs import bfs
from dfs import dfs
from maze import Maze


def print_maze(maze):
    for row in maze:
        print(' '.join(row))


def print_search_path(grid, path, start):
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            if (j, i) in path and (j, i) not in [start]:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        sleep(0.5)


def generate_maze(size, goal_x, goal_y, base_density=0):
    start = (0, 0)  # Define starting point (S) and goal point (G)

    for index in range(1, 11):
        maze = [['.' for _ in range(size)] for _ in range(size)]
        density = ceil(int(size * size * base_density))  # distribution of the walls

        for _ in range(density):
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            while (x, y) == start or (x, y) == (goal_x, goal_y) or maze[x][y] == 'X':
                x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            maze[x][y] = 'X'  # walls

        maze[start[0]][start[1]] = 'S'  # start point
        maze[goal_x][goal_y] = 'G'
        save_maze(index, maze)

        base_density += 0.05  # change parameters

    return size, start, (goal_y, goal_x)


def save_maze(file_name, maze_map):
    with open(f'dumps/maze-{file_name}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(maze_map)
        f.seek(0, os.SEEK_END)
        f.seek(f.tell() - 2, os.SEEK_SET)
        f.truncate()


def load_maze(file_name):
    # Load maze from CSV file
    with open(f'dumps/maze-{file_name}.csv', 'r') as f:
        output = list(csv.reader(f))
        f.close()
    return output


def clean_dump_file():
    for _ in range(1, 11):
        os.remove(f'dumps/maze-{_}.csv')


def header():
    print(
        f"{'Run': ^10} {'Algorithm': ^10} {'Solution Path Length': ^20} {'Nodes Expanded': ^20} {'Execution Time (micro seconds)': ^20} {'Status': ^30}")


def visualize_maze(start, goal, algo, target_maze=999):
    if target_maze not in range(1, 11):  # or maze.isGoalReach is False
        print("")

    maze = Maze(load_maze(str(target_maze).strip()))
    if algo == "bfs":
        bfs(maze)
    if algo == "dfs":
        dfs(maze)
    if algo == "a*":
        astar(maze, start, goal)

    print("Problem Maze")
    print_maze(maze.grid)
    print()
    print("Solution")
    print_search_path(maze.grid, maze.solutionMaze, start)
    print(f"Path Length: {maze.solutionPathLength}")
    print(f"Nodes Expanded: {maze.nodesVisited}")
    print(f"Solution: {len(maze.solutionMaze)}")
    print(f"Was Goal reached? {'Yes' if maze.isGoalReached else 'No'}")


def run_all_bfs(start):
    metrics = {
        'solution_path_length': [],
        'nodes_visited': [],
        'execution_time': [],
    }

    header()
    # load all mazes from dumps and run bfs on each
    for i in range(1, 11):
        maze = Maze(load_maze(i))
        status = bfs(maze)

        print(
            f"{str(i):^10} {'BFS':^15} {str(maze.solutionPathLength):^20} {str(maze.nodesVisited):^20} {str(round(maze.executionTime)):^20} {'Pass' if status else 'Fail' : ^40}")

        metrics['solution_path_length'].append(maze.solutionPathLength)
        metrics['nodes_visited'].append(maze.nodesVisited)
        metrics['execution_time'].append(maze.executionTime)

    print()
    print(f"{'Average': ^10} {'BFS':^15} "
          f"{str(sum(metrics['solution_path_length']) / len(metrics['solution_path_length'])):^20} "
          f"{str(sum(metrics['nodes_visited']) / len(metrics['nodes_visited'])): ^20}"
          f"{str(sum(metrics['execution_time']) / len(metrics['execution_time'])): ^20}")
    print()


def run_all_dfs(start):
    metrics = {
        'solution_path_length': [],
        'nodes_visited': [],
        'execution_time': [],
    }

    header()
    # load all mazes from dumps and run dfs on each
    for _ in range(1, 11):
        maze = Maze(load_maze(_))
        status = dfs(maze)
        print(
            f"{str(_):^10} {'DFS':^15} {str(maze.solutionPathLength):^20} {str(maze.nodesVisited):^20} {str(round(maze.executionTime)):^20} {'Pass' if status else 'Fail' : ^40}")

        metrics['solution_path_length'].append(maze.solutionPathLength)
        metrics['nodes_visited'].append(maze.nodesVisited)
        metrics['execution_time'].append(maze.executionTime)

    print()
    print(f"{'Average': ^10} {'DFS':^15} "
          f"{str(sum(metrics['solution_path_length']) / len(metrics['solution_path_length'])):^20} "
          f"{str(sum(metrics['nodes_visited']) / len(metrics['nodes_visited'])): ^20}"
          f"{str(sum(metrics['execution_time']) / len(metrics['execution_time'])): ^20}")
    print()


def run_all_a_start(start, goal):
    metrics = {
        'solution_path_length': [],
        'nodes_visited': [],
        'execution_time': [],
    }

    header()

    # load all mazes from dumps and run astar on each
    for _ in range(1, 11):
        maze = Maze(load_maze(_))
        status = astar(maze, start, goal)
        print(
            f"{str(_):^10} {'A*':^15} {str(maze.solutionPathLength):^20} {str(maze.nodesVisited):^20} {str(round(maze.executionTime)):^20} {'Pass' if status else 'Fail' : ^40}")

        metrics['solution_path_length'].append(maze.solutionPathLength)
        metrics['nodes_visited'].append(maze.nodesVisited)
        metrics['execution_time'].append(maze.executionTime)

    print()
    print(f"{'Average': ^10} {'A*':^15} "
          f"{str(sum(metrics['solution_path_length']) / len(metrics['solution_path_length'])):^20} "
          f"{str(sum(metrics['nodes_visited']) / len(metrics['nodes_visited'])): ^20}"
          f"{str(sum(metrics['execution_time']) / len(metrics['execution_time'])): ^20}")
    print()


def get_user_input(size, start, goal):
    print(
        "To evaluate performance, we will generated 10 different mazes and run them through 3 search algorithms: DFS, "
        "BFS and A*")
    print(f"Maze grid size: {size}")
    print(f"Start point: {start}")
    print(f"Goal point: {goal}")

    while True:
        try:
            algo, maze_number = input("Enter the algorithm and maze no. to visualize ex. DFS,3: ").split(',')

            if algo.lower() not in ['dfs', 'bfs', 'a*']:
                print('Invalid input. Specify the algorithm as either DFS, BFS or A*')

            if int(maze_number) not in range(1, 11):
                print('Invalid input. Specify a value between 1 and 10 inclusive')

            return algo.lower(), maze_number
        except ValueError:
            print("Invalid input.")
