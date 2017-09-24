# aStar.py
# Implementation of the A* search algorithm using
# Manhatten distance as heuristc fucntion

import utility


def a_star_search(maze, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1),
                 (1, -1), (-1, 1), (-1, -1)]    # quick neighbors fiding offset
    close_list = set()
    parents = {}        # List to hold all parents
    path_cost = {}      # path cost that we have so far
    g_score = {start: 0}
    f_score = {start: utility.heuristicFcn(start, goal)}

    frontier = utility.PriorityQueue()
    frontier.push(start, 0)

    parents[start] = None
    path_cost[start] = None

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
            return path

        "If the current node is not our goal, we add it to the close list"
        close_list.add(current)

        "Now we need to check all 8 neighbors of the current node"
        for dx, dy in neighbors:
            neighbor = current[0] + dx, current[1] + dy
            g_temp = g_score[current] + utility.heuristicFcn(current, neighbor)

            "Need to make sure that the neighbor location is valid"
            if 0 <= neighbor[1] < maze.shape[1]:   # coordinate validation
                if 0 <= neighbor[0] < maze.shape[0]:
                    if maze[neighbor[0], neighbor[1]] ==
