import utility
import time

def best_first_search(maze, start, end):
    closed = set()
    parents = {}
    g_score = {start: 0}
    fringe = utility.PriorityQueue()
    fringe.push(0, start)
    parents[start] = None
    path = []
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    node_expanded = 0
    clk = time.clock()
    while not fringe.isEmpty():
        curr = fringe.pop()
        if curr == end:
            while curr in parents:
                path.append(curr)
                curr = parents[curr]
            clk_used = time.clock() - clk
            print("Time Used: ", clk_used, " seconds")
            return path, node_expanded

        closed.add(curr)
        "Now we need to check all 4 neighbors of the current node"
        for dx, dy in neighbors:
            neighbor = curr[0] + dx, curr[1] + dy
            g_temp = g_score[curr] + utility.heuristicFcn(curr, neighbor)

            "Need to make sure that the neighbor location is valid"
            if 0 <= neighbor[1] < maze.shape[1]:  # coordinate validation
                if 0 <= neighbor[0] < maze.shape[0]:
                    "Check if the intended neighbor is a wall"
                    if maze[neighbor[0], neighbor[1]] == "%":
                        continue
                else:  # if the y-coordinate is not valid
                    continue
            else:  # if the x-coordinate is not valid
                continue
            """""""mark"""""""
            if neighbor in closed and g_temp >= g_score.get(neighbor, 0):  # skip if the node is closed
                continue
            #
            if g_temp < g_score.get(neighbor, 0) or (neighbor not in [i[1] for
                                                                      i in fringe.elements]):
                parents[neighbor] = curr
                g_score[neighbor] = g_temp
                fringe.push( g_score[neighbor], neighbor)
                node_expanded += 1
    return False
