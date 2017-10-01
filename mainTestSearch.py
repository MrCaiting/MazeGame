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
flag, total_cost, node_expanded, goal_sequence = a_star_multigoal(maze, start, goal_list,
                                                                  goal_sequence, frontier,
                                                                  heu_val, visited,
                                                                  path_cost, 0, 0)
print(flag, total_cost, node_expanded)
print(goal_sequence)

index = 0
for i, j in goal_sequence:
    if (1 <= index <= 10):
        maze[i][j] = index-1
    if (11 <= index <= 36):
        maze[i][j] = chr(ord('a') + (index-11))
    if (37 <= index <= 62):
        maze[i][j] = chr(ord('A') + (index-37))

withPath = open('multiGoalSolution.txt', 'w')
for i in range(maze.shape[0]):
    for j in range(maze.shape[1]):
        withPath.write("%s" % maze[i][j])
    withPath.write("\n")
