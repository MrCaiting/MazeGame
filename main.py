from mainTest import mainTest
from mainTestSearch import mainTestSearch

filename_maze = 'openMaze.txt'
filename_search = 'tinySearch.txt'
"Select method of running maze: 0: Depth First Search" \
"                               1: Breadth First Search" \
"                               2: Greedy Best First Search" \
"                               3: A* Search                "
method = 0
print("Maze Single Goal: ")
success_maze = mainTest(filename_maze,method)
"Maze multigoal path search running A* algorithm"
print("\nMaze Multi Goal: ")
success_search = mainTestSearch(filename_search)