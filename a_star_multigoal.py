# a_star_multigoal.py

from utility import PriorityQueue
from heuristic_multi_goal import heuristic_multi_goal
import time
"""
a_star_multi_init(maze)

DESCRIPTION:
This function is used to initialize what we need in the actual A star function
Give the maze data as input, we want to acquire some essential properties of
every single point in the maze, including: visited, heu_val, Priority Queue,
and path cost

INPUTS:
maze:           The 2D string matrix that we have got from reading the txt file

OUTPUTS:
heu_val: a dictionary of all the heuristic value corresponded to a single point
visited: if this point has been visited (can ONLY be 0 or 1)
path_cost: the cost to get this point so far
frontier: a p-Queue that we will be using in A star algorithm
"""


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




" All possible movements stored in a single list for future use "
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

"""
This is the modified version of a star algorithm to calculate the path to get
all the goals

INPUTS:
maze:           The 2D string matrix that we have got from reading the txt file
current:        The current position that we are looking at,
    represented in the form of (x,y)
ToGoGoals:      List of goals that we need to visit
goal_sequence:  the ultimate sequence of getting all the goals
nodeInPath:     Integer that represents how many nodes that we have expanded
"""


def a_star_multigoal(maze, current, ToGoGoals, goal_sequence, frontier,
                     heu_val, visited, path_cost, total_cost, node_expanded):
    " If the current node is not valid "
    print(current)
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
                node_expanded += len(frontier.elements)
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
        nig, new_heu, new_cost = heuristic_multi_goal(neighbor, ToGoGoals,
                                                       path_cost[current],
                                                       visited[neighbor],
                                                       heu_val[neighbor])
        if (nig == 1):
            path_cost[neighbor] = new_cost
            heu_val[neighbor] = new_heu
        " push the child on to the p-Queue"
        frontier.push(heu_val[neighbor], neighbor)
    success = 0

    while (success == 0 and (frontier.isEmpty() is False)):
        print("in")
        currNode = frontier.pop()
        if (visited[(currNode[0], currNode[1])] == 0 and maze[currNode[0], currNode[1]] != '%'):
            success, total_cost,
            node_expanded, goal_sequence = a_star_multigoal(maze, currNode, ToGoGoals,
                                                            goal_sequence, frontier,
                                                            heu_val, visited, path_cost,
                                                            total_cost, node_expanded)

    return success, total_cost, node_expanded, goal_sequence
