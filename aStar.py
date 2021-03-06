# aStar.py
# Implementation of the A* search algorithm using
# Manhatten distance as heuristc fucntion

from utility import *
import time


def a_star_search(maze, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    "(1, 1), (1, -1), (-1, 1), (-1, -1)] "   # quick neighbors fiding offset
    close_list = set()
    parents = {}        # List to hold all parents
    node_expanded = 0
    cost_sofar = 0
    g_score = {start: 0}
    f_score = {start: heuristicFcn(start, goal)}

    frontier = PriorityQueue()
    frontier.push(f_score[start], start)
    parents[start] = None
    "Start Timer"
    clk = time.clock()
    while not frontier.isEmpty():
        current = frontier.pop()

        """
        Immediately check if the current node is the goal
        If this is the goal, we need to back track all the
        node that we have visted to get the path
        """
        if current == goal:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
                cost_sofar += 1
            clk_used = time.clock() - clk
            print("Time Used: ", clk_used, " seconds")
            return path, node_expanded

        "If the current node is not our goal, we add it to the close list"
        close_list.add(current)

        "Now we need to check all 4 neighbors of the current node"
        for dx, dy in neighbors:
            neighbor = current[0] + dx, current[1] + dy
            g_temp = g_score[current] + heuristicFcn(current, neighbor)
            f_temp = g_temp + heuristicFcn(neighbor, goal)

            "Need to make sure that the neighbor location is valid"
            if 0 <= neighbor[1] < maze.shape[1]:   # coordinate validation
                if 0 <= neighbor[0] < maze.shape[0]:
                    "Check if the intended neighbor is a wall"
                    if maze[neighbor[0], neighbor[1]] == "%":
                        continue
                else:          # if the y-coordinate is not valid
                    continue
            else:              # if the x-coordinate is not valid
                continue

            if neighbor in close_list and g_temp >= g_score.get(neighbor, 0):
                # skip if the node is closed
                continue

            if g_temp < g_score.get(neighbor, 0) or (neighbor not in [i[1] for
                                                     i in frontier.elements]):
                parents[neighbor] = current
                g_score[neighbor] = g_temp
                f_score[neighbor] = f_temp
                frontier.push(f_score[neighbor], neighbor)
                node_expanded += 1
            else:
                continue
    return False
