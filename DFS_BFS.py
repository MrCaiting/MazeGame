from collections import deque
import time


def pacman_bfs(maze,start,end):
    queue = deque([start])
    visited = set()
    height = len(maze)
    width = len(maze[0])
    clk = time.clock()
    while queue:
        cur = queue.popleft()
        print(cur)
        if cur == end:
            clk_used = time.clock() - clk
            print("found")
            print("Time Used: ", clk_used, " seconds")
            return "man i am done"
        if cur in visited:
            continue
        visited.add(cur)
        if (cur[0]+1) < height and maze[cur[0]+1][cur[1]] == ' ' or maze[cur[0]+1][cur[1]] == '.':
            queue.append((cur[0]+1,cur[1]))
        if (cur[0]) > 0 and maze[cur[0]-1][cur[1]] == ' ' or maze[cur[0]-1][cur[1]] == '.':
            queue.append((cur[0]-1,cur[1]))
        if (cur[1]+1) < width and maze[cur[0]][cur[1]+1] == ' ' or maze[cur[0]][cur[1]+1] == '.':
            queue.append((cur[0],cur[1]+1))
        if (cur[1]) > 0 and maze[cur[0]][cur[1]-1] == ' ' or maze[cur[0]][cur[1]-1] == '.':
            queue.append((cur[0],cur[1]-1))
    return "gg"


def pacman_dfs(maze,start,end):
    stack = [start]
    visited = set()
    path = set()
    height = len(maze)
    width = len(maze[0])
    clk = time.clock()
    while stack:
        cur = stack.pop()
        if cur == end:
            clk_used = time.clock() - clk
            print("done")
            print("Time Used: ", clk_used, " seconds")
            return visited
        if cur in visited:
            continue
        visited.add(cur)
        if (cur[0]+1) < height and maze[cur[0]+1][cur[1]] == ' ' or maze[cur[0]+1][cur[1]] == '.':
            stack.append((cur[0]+1,cur[1]))
        if (cur[0]) > 0 and maze[cur[0]-1][cur[1]] == ' ' or maze[cur[0]-1][cur[1]] == '.':
            stack.append((cur[0]-1,cur[1]))
        if (cur[1]+1) < width and maze[cur[0]][cur[1]+1] == ' ' or maze[cur[0]][cur[1]+1] == '.':
            stack.append((cur[0],cur[1]+1))
        if (cur[1]) > 0 and maze[cur[0]][cur[1]-1] == ' ' or maze[cur[0]][cur[1]-1] == '.':
            stack.append((cur[0],cur[1]-1))
    return visited