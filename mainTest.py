# mainTest.py

"""
Like the main.c in C, we put all the code here to
test different method to run the maze
"""

import readTXT
from aStar import *
from DFS_BFS import *
from best_first_search import *

"Read the maze txt file and get everything we need for searching"
def mainTest(filename,met):
    row, col = readTXT.get_size_txt(filename)
    maze = readTXT.read_txt(filename, row, col)
    start,end = readTXT.find_enter_exit(maze)
    method_list = (pacman_dfs, pacman_bfs, best_first_search, a_star_search)
    method = met
    path, node = method_list[method](maze, start, end)
    print("Path Cost = ", len(path) - 1, "\nNode Expanded = ", node)
    print("See solution.txt")
    for i, j in path:
        maze[i][j] = "."

    withPath = open('solution.txt', 'w')
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            withPath.write("%s" % maze[i][j])
        withPath.write("\n")
    return 1
