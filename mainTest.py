# mainTest.py
# Like the main.c in C, we put all the code here to test different method to run the maze

import readTXT
import aStar
from utility import *

"Read the maze txt file and get everything we need for searching"

row, col = readTXT.get_size_txt('mediumMaze.txt')
maze = readTXT.read_txt('mediumMaze.txt',row, col)
start, end = readTXT.find_enter_exit(maze)

path = aStar.a_star_search(maze, start, end)
print(path)

for i, j in path:
    maze[i][j] = "."

withPath = open('solution.txt', 'w')
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        withPath.write("%s" % maze[i][j])
    withPath.write("\n")

print(path)