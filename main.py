from mainTest import mainTest
from mainTestSearch import mainTestSearch
from mainTestExtra import mainTestExtra

"This is the top level main file where all the codes are imported and called" \
"you can modify filename for corresponding parts. For part 1.1 you can select" \
"different methods according to the instruction below."

filename_maze = 'bigMaze.txt'
filename_search = 'mediumSearch.txt'
filename_extra = 'bigDots.txt'

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
print("\nMaze Extra Credit: ")
success_extra = mainTestExtra(filename_extra)