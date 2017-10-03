import numpy as np
import MST
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import time
from utility import *

def heuristic_extra_credit(curr_child, goal_list, path_cost,closed_list, heu_val):
    dist_2goal = np.zeros(len(goal_list))
    i = 0
    for goal in goal_list:
        dist_2goal[i] = heuristicFcn(curr_child, goal)
        i += 1
    min_dist_2goal = np.amin(dist_2goal)
    list = [curr_child]
    list.extend(goal_list)
    tree = MST.maze2tree(goal_list)
    min_tree = minimum_spanning_tree(tree, overwrite=False)
    min_tree = min_tree.toarray().astype(int)
    MSTweight = MST.findMSTweight(min_tree)

    heuristic = 10 * (MSTweight + min_dist_2goal + path_cost)

    if (closed_list == 0) or (heuristic < heu_val):
        hn = heuristic
        cost = path_cost + 1
        flag = 1
    else:
        hn = heu_val
        cost = 0
        flag = 0
    return flag, hn, cost

def a_star_multi_init(maze):
    path_cost = {}
    heu_val = {}
    visited = {}
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            heu_val[(i, j)] = 0
            visited [(i, j)] = 0
            path_cost[(i, j)] = 0
    return heu_val, visited, path_cost


"""
set_all_unvisited(visited, maze)

DESCRIPTION: a helper function used to clear all the points as unvisited
"""


def set_all_unvisited(visited, maze_row, maze_col):
    for i in range(maze_row):
        for j in range(maze_col):
            visited[(i, j)] = 0
    return visited




moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def a_star_extra(maze, current, ToGoGoals, goal_sequence, frontier,
                     heu_val, visited, path_cost, total_cost, node_expanded):
    " If the current node is not valid "
    flag = 0
    if current is None:
        return 0

    " If the current possition is one of the goals "
    if (maze[current[0], current[1]] == '.'):

        " If it is indeed a goal, we need to find out which one"
        for singleGaol in ToGoGoals:
            if (current == singleGaol):
                flag = 1
                break

        if (flag == 1):
            "We need to know that if the current goal is exactly the last one"
            if (len(ToGoGoals) == 1):
                goal_sequence.append(current)
                total_cost = path_cost[current]
                return 1, total_cost, node_expanded, goal_sequence
            else:
                goal_sequence.append(current)
                ToGoGoals.remove(current)
                "Since a goal is found, we need to reset all others unvisited"
                visited = set_all_unvisited(visited, maze.shape[0], maze.shape[1])
                "Update the number of nodes that we have explored"
                #node_expanded += len(frontier.elements)
                #print(node_expanded)
                "Remove all the elements in the priority queue"
                frontier.clear()

    " If the current possition is not a goal "
    visited[current] = 1    # mark the position as visited

    " Trying to go to all different four directions "
    for dx, dy in moves:
        neighbor = current[0] + dx, current[1] + dy

        "Need to make sure that the neighbor's location is valid"
        if 0 <= neighbor[1] < maze.shape[1]:   # coordinate validation
            if 0 <= neighbor[0] < maze.shape[0]:
                "Check if the intended neighbor is a wall"
                if maze[neighbor[0], neighbor[1]] == "%":
                    continue
            else:   # if the y-coordinate is not valid, keep going
                continue
        else:   # if the x-coordinate is not valid, keep going
            continue
        "Now, we have the correct coordinate, calculate new heuristic value"
        nig, new_heu, new_cost = heuristic_extra_credit(neighbor, ToGoGoals, path_cost[current],
                                                       visited[neighbor],
                                                       heu_val[neighbor])
        if (nig == 1):
            path_cost[neighbor]  = new_cost
            heu_val[neighbor] = new_heu
        " push the child on to the p-Queue"
        frontier.push(heu_val[neighbor], neighbor)

        node_expanded += 1
    success = 0

    while (success == 0 and (frontier.isEmpty() is False)):

        currNode = frontier.pop()

        if (visited[(currNode[0], currNode[1])] == 0 and maze[currNode[0], currNode[1]] != '%'):
            success, total_cost, node_expanded, goal_sequence = a_star_extra(maze, currNode, ToGoGoals,
                                                            goal_sequence, frontier,
                                                            heu_val, visited, path_cost,
                                                            total_cost, node_expanded)

    return success, total_cost, node_expanded, goal_sequence
