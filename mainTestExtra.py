import readTXT
from extracredit import *
import utility
import time

def mainTestExtra(filename):
    row, col = readTXT.get_size_txt(filename)
    maze = readTXT.read_txt(filename, row, col)
    start,goal_list = readTXT.find_multi_goals(maze)
    frontier = PriorityQueue()
    heu_val, visited, path_cost = a_star_multi_init(maze)
    goal_sequence = []
    start_time = time.clock()
    flag, total_cost, node_expanded, goal_sequence = a_star_extra(maze, start, goal_list,
                                                                  goal_sequence, frontier,
                                                                  heu_val, visited,
                                                                  path_cost, 0, 0)
    time_used = time.clock() - start_time
    print("Time Used: ", time_used)
    print("Success = ", flag, "\nPath Cost = ", total_cost, "\nNode Expanded = ", node_expanded)
    print("Goal Sequence: ",goal_sequence)
    return 1