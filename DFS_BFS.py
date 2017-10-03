from collections import deque
import time

def pacman_bfs(maze,start,end):
    queue = deque([start])
    visited = set()
    height = len(maze)
    width = len(maze[0])
    clk = time.clock()
    parents = {}
    node_expanded = 0
    cost = 0
    parents[start] = None

    while queue:
        cur = queue.popleft()
        if cur == end:
            path = []
            while cur in parents:
                path.append(cur)
                cur = parents[cur]
                cost += 1
            clk_used = time.clock() - clk
            print("Time Used: ", clk_used, " seconds")
            return path, node_expanded
        if cur in visited:
            continue
        visited.add(cur)
        if (cur[0]+1) < height and maze[cur[0]+1][cur[1]] != '%':
            if (cur[0]+1, cur[1]) not in parents:
                parents[(cur[0]+1, cur[1])] = (cur[0], cur[1])
            if (cur[0]+1, cur[1]) not in visited:
                node_expanded += 1
            queue.append((cur[0] + 1, cur[1]))
        if (cur[0]) > 0 and maze[cur[0]-1][cur[1]] != '%':
            if (cur[0]-1, cur[1]) not in parents:
                parents[(cur[0]-1, cur[1])] = (cur[0], cur[1])
            if (cur[0]-1, cur[1]) not in visited:
                node_expanded += 1
            queue.append((cur[0] - 1, cur[1]))
        if (cur[1]+1) < width and maze[cur[0]][cur[1]+1] != '%':
            if (cur[0], cur[1]+1) not in parents:
                parents[(cur[0], cur[1]+1)] = (cur[0], cur[1])
            if (cur[0], cur[1]+1) not in visited:
                node_expanded += 1
            queue.append((cur[0], cur[1] + 1))
        if (cur[1]) > 0 and maze[cur[0]][cur[1]-1] != '%':
            if (cur[0], cur[1]-1) not in parents:
                parents[(cur[0], cur[1]-1)] = (cur[0], cur[1])
            if (cur[0], cur[1]-1) not in visited:
                node_expanded += 1
            queue.append((cur[0], cur[1] - 1))

    return "gg"



def pacman_dfs(maze, start, end):
    stack = [start]
    visited = set()
    height = len(maze)
    width = len(maze[0])
    clk = time.clock()
    parents = {}
    node_expanded = 0
    cost = 0
    parents[start] = None
    while stack:
        cur = stack.pop()
        if cur == end:
            path = []
            while cur in parents:
                path.append(cur)
                cur = parents[cur]
                cost += 1
            clk_used = time.clock() - clk
            print("Time Used: ", clk_used, " seconds")
            return path, node_expanded
        if cur in visited:
            continue
        visited.add(cur)

        if (cur[0]+1) < height and maze[cur[0]+1][cur[1]] != '%':
            if (cur[0]+1, cur[1]) not in parents:
                parents[(cur[0]+1, cur[1])] = (cur[0], cur[1])
            if (cur[0]+1, cur[1]) not in visited:
                node_expanded += 1
            stack.append((cur[0]+1, cur[1]))
        if (cur[0]) > 0 and maze[cur[0]-1][cur[1]] != '%':
            if (cur[0]-1, cur[1]) not in parents:
                parents[(cur[0]-1, cur[1])] = (cur[0], cur[1])
            if (cur[0]-1, cur[1]) not in visited:
                node_expanded += 1
            stack.append((cur[0]-1, cur[1]))
        if (cur[1]+1) < width and maze[cur[0]][cur[1]+1] != '%':
            if (cur[0], cur[1]+1) not in parents:
                parents[(cur[0], cur[1]+1)] = (cur[0], cur[1])
            if (cur[0], cur[1]+1) not in visited:
                node_expanded += 1
            stack.append((cur[0], cur[1]+1))
        if (cur[1]) > 0 and maze[cur[0]][cur[1]-1] != '%':
            if (cur[0], cur[1]-1) not in parents:
                parents[(cur[0], cur[1]-1)] = (cur[0], cur[1])
            if (cur[0], cur[1]-1) not in visited:
                node_expanded += 1
            stack.append((cur[0], cur[1]-1))
    return "gg"

