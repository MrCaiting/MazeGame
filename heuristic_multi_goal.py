import utility as util
import numpy as np
import MST
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

def heuristic_multi_goal(curr_child, goal_list, path_cost, closed_list, heu_val):
    dist_2goal = np.zeros(len(goal_list))
    i = 0
    for goal in goal_list:
        dist_2goal[i] = util.heuristicFcn(curr_child, goal)
        i += 1
    min_dist_2goal = np.amin(dist_2goal)
    list = [curr_child]
    list.extend(goal_list)
    tree = MST.maze2tree(goal_list)
    min_tree = minimum_spanning_tree(tree, overwrite=False)
    min_tree = min_tree.toarray().astype(int)
    print(min_tree)
    MSTweight = MST.findMSTweight(min_tree)
    heuristic = min_dist_2goal + MSTweight #+ path_cost + 1

    if (closed_list == 0) or (heuristic < heu_val):
        hn = heuristic
        cost = path_cost + 1
        flag = 1
    else:
        hn = heu_val
        cost = 0
        flag = 0
    return flag, hn, cost
