import readTXT
from a_star_multigoal import *
import utility

row, col = readTXT.get_size_txt('mediumSearch.txt')
maze = readTXT.read_txt('mediumSearch.txt', row, col)
print(maze[4][4])
start,goal_list = readTXT.find_multi_goals(maze)
print(start, goal_list)
frontier = PriorityQueue()
heu_val, visited, path_cost = a_star_multi_init(maze)
print(type(path_cost))
print(path_cost[start])
goal_sequence = []
flag, total_cost, node_expanded = a_star_multigoal(maze, start, goal_list, goal_sequence, frontier, heu_val, visited, path_cost, 0, 0)
print(flag, total_cost, node_expanded)
