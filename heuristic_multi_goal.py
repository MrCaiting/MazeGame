from utility import *
import numpy as np
import MST

def heuristic_multi_goal(curr_child, goal_list, path_cost, closed_list, heu_val):
    dist_2goal = np.zeros(len(goal_list))
    i = 0
    for goal in goal_list:
        dist_2goal[i] = heuristicFcn(curr_child, goal)
        i += 1
    min_index = np.argmin(dist_2goal)
    min_dist_2goal = goal_list[min_index]
    tree = MST.maze2tree(goal_list)
    min_tree = MST.minimum_spanning_tree(tree, overwrite=False)
    min_tree = min_tree.toarray().astype(int)
    MSTweight = MST.findMSTweight(min_tree)
    heuristic = min_dist_2goal + MSTweight + path_cost + 1

    if (curr_child not in closed_list) or (heuristic < heu_val):
        hn = heuristic
        cost = path_cost + 1

    return hn, cost