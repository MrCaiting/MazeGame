import readTXT
from collections import deque
import time
row, col = readTXT.get_size_txt('mediumMaze.txt')
maze = readTXT.read_txt('mediumMaze.txt',row, col)
start, end = readTXT.find_enter_exit(maze)

height = len(maze)
width = len(maze[0])

found = "found"

def pacman_bfs(maze,start,end):
    queue = deque([start])
    visited = set()
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

gg = pacman_bfs(maze,start,end)

def pacman_dfs(maze,start,end):
    stack = [start]
    visited = set()
    path = set()
    clk = time.clock()
    while stack:
        cur = stack.pop()
        if cur == end:
            clk_used = time.clock()
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

wp = pacman_dfs(maze,start,end)

