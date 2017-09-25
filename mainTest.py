# mainTest.py
# Like the main.c in C, we put all the code here to test different method to run the maze

import readTXT
from aStar import *
from DFS_BFS import *
from utility import *

"Read the maze txt file and get everything we need for searching"

row, col = readTXT.get_size_txt('mediumMaze.txt')
maze = readTXT.read_txt('mediumMaze.txt',row, col)
start, end = readTXT.find_enter_exit(maze)
method_list = (pacman_dfs, pacman_bfs, a_star_search)
method = 0
path = method_list[method](maze, start, end)
print(path)

if method == 2:
    for i, j in path:
        maze[i][j] = "."

    withPath = open('solution.txt', 'w')
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            withPath.write("%s" % maze[i][j])
        withPath.write("\n")

    print(path)