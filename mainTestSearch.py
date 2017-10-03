import readTXT
from a_star_multigoal import *
import utility
import time
def mainTestSearch(filename):
    row, col = readTXT.get_size_txt(filename)
    maze = readTXT.read_txt(filename, row, col)
    start,goal_list = readTXT.find_multi_goals(maze)
    frontier = PriorityQueue()
    heu_val, visited, path_cost = a_star_multi_init(maze)
    goal_sequence = []
    start_time = time.clock()
    flag, total_cost, node_expanded, goal_sequence = a_star_multigoal(maze, start, goal_list,
                                                                  goal_sequence, frontier,
                                                                  heu_val, visited,
                                                                  path_cost, 0, 0)
    time_used = time.clock() - start_time
    print("Time Used: ", time_used)
    print("Success = ", flag, "\nPath Cost = ", total_cost, "\nNode Expanded = ", node_expanded)
    print("Goal Sequence: ",goal_sequence)
    print("See multiGoalSolution.txt")
    index = 1
    for i, j in goal_sequence:
        if (1 <= index <= 10):
            maze[i][j] = index-1
        if (11 <= index <= 36):
            maze[i][j] = chr(ord('a') + (index-11))
        if (37 <= index <= 62):
            maze[i][j] = chr(ord('A') + (index-37))
        index+= 1

    withPath = open('multiGoalSolution.txt', 'w')
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            withPath.write("%s" % maze[i][j])
        withPath.write("\n")
    return 1