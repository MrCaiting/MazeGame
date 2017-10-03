from mainTest import mainTest
from mainTestSearch import mainTestSearch
from mainTestExtra import mainTestExtra

"All results are displayed here"

"This is the top level main file where all the codes are imported and called" \
"you can modify filename for corresponding parts. For part 1.1 you can select" \
"different methods according to the instruction below."


"Select method of running maze: 0: Depth First Search" \
"                               1: Breadth First Search" \
"                               2: Greedy Best First Search" \
"                               3: A* Search                "
method = 0

filename_maze = 'mediumMaze.txt'
print("Maze Medium Maze Depth First Search: ")
success_maze_0 = mainTest(filename_maze,method)

filename_maze = 'bigMaze.txt'
print("\nMaze Big Maze Depth First Search: ")
success_maze_1 = mainTest(filename_maze,method)

filename_maze = 'openMaze.txt'
print("\nMaze Open Maze Depth First Search: ")
success_maze_2 = mainTest(filename_maze,method)

method = 1

filename_maze = 'mediumMaze.txt'
print("\nMaze Medium Maze Breadth First Search: ")
success_maze_3 = mainTest(filename_maze,method)

filename_maze = 'bigMaze.txt'
print("\nMaze Big Maze Breadth First Search: ")
success_maze_4 = mainTest(filename_maze,method)

filename_maze = 'openMaze.txt'
print("\nMaze Open Maze Breadth First Search: ")
success_maze_5 = mainTest(filename_maze,method)
"Maze multigoal path search running A* algorithm"

method = 2

filename_maze = 'mediumMaze.txt'
print("\nMaze Medium Maze Greedy Best-First Search: ")
success_maze_7 = mainTest(filename_maze,method)

filename_maze = 'bigMaze.txt'
print("\nMaze Big Maze Greedy Best-First Search: ")
success_maze_8 = mainTest(filename_maze,method)

filename_maze = 'openMaze.txt'
print("\nMaze Open Maze Greedy Best-First Search: ")
success_maze_9 = mainTest(filename_maze,method)

method = 3

filename_maze = 'mediumMaze.txt'
print("\nMaze Medium Maze A* Search: ")
success_maze_10 = mainTest(filename_maze,method)

filename_maze = 'bigMaze.txt'
print("\nMaze Big Maze A* Search: ")
success_maze_11 = mainTest(filename_maze,method)

filename_maze = 'openMaze.txt'
print("\nMaze Open Maze A* Search: ")
success_maze_12 = mainTest(filename_maze,method)

"Maze multigoal path search running A* algorithm"

filename_search = 'tinySearch.txt'
print("\nMaze Tiny Search: ")
success_search_0 = mainTestSearch(filename_search)

filename_search = 'smallSearch.txt'
print("\nMaze Small Search: ")
success_search_1 = mainTestSearch(filename_search)

filename_search = 'mediumSearch.txt'
print("\nMaze Medium Search: ")
success_search = mainTestSearch(filename_search)

filename_extra = 'bigDots.txt'
print("\nMaze Extra Credit Big Dots: ")
success_extra = mainTestExtra(filename_extra)