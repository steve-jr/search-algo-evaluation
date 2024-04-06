from helpers import *


def main():
    size, start, goal = generate_maze(10, 9, 9)

    run_all_bfs(start)
    run_all_dfs(start)
    run_all_a_start(start, goal)

    algo, selected_maze = get_user_input(size, start, goal)
    visualize_maze(start, goal, algo, selected_maze)

    clean_dump_file()


main()
