# a_star_multigoal.py

from utility import *
import time

" All possible movements stored in a single list for future use "
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
" Initialize a closed_list for use "
curr_closed_list = []

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


def a_star_multigoal(maze, current, ToGoGoals, goal_sequence,
                     nodeInPath, curr_closed_list):
    " If the current node is not valid "
    if(current == NULL):
        return goal_sequence

    " Need to check if the current possition is one of the goals "
    if (maze[current[0], current[1] == '.']):
        " If it is indeed a goal, we need to find out which one"
        for singleGaol in ToGoGoals:
            if (current == singleGaol):
                flag = 1
                break

        if (flag == 1):
            "We need to know that if the current goal is exactly the last one"
            if (len(ToGoGoals) == 1):
                goal_sequence.append(current)
                nodeInPath += 1
                return goal_sequence
            else:
                goal_sequence.append(current)
                ToGoGoals.remove(current)




    return
