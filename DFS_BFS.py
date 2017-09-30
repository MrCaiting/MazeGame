from collections import deque
import time


<<<<<<< HEAD

def get_size_txt(fname):
    with open(fname) as f:
        row_count = 0
        col_count = 0
        for char in f.read():
            if char == "\n":
                row_count = row_count + 1
            if char != "\n":
                col_count = col_count + 1
    return row_count+1, int(col_count/(row_count+1))


def read_txt(fname,row,col):
    list = []
    with open(fname) as f:
        while True:
            ch = f.read(1)
            if ch != "\n" and ch != '':
                list.append(ch)
            if not ch:
                break
    maze = np.array(list)
    maze = maze.reshape(row, col)

    return maze


row, col = get_size_txt('mediumMaze.txt')


maze = read_txt('mediumMaze.txt', row, col)
# print(row, col)
# print(maze)
# graph = array2graph(maze)
# print(graph)
height = len(maze)
width = len(maze[0])
print(height)
print(width)
found = "found"

print(maze[1][59])


def pacman_bfs(maze, start, end):
=======
def pacman_bfs(maze,start,end):
>>>>>>> 8d27fc125a97c6335e6d088c839859031cb27419
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
        if (cur[0]+1) < height and maze[cur[0]+1][cur[1]] == ' ' or maze[cur[0] + 1][cur[1]] == '.':
            queue.append((cur[0]+1, cur[1]))
        if (cur[0]) > 0 and maze[cur[0]-1][cur[1]] == ' ' or maze[cur[0]-1][cur[1]] == '.':
            queue.append((cur[0]-1, cur[1]))
        if (cur[1]+1) < width and maze[cur[0]][cur[1]+1] == ' ' or maze[cur[0]][cur[1]+1] == '.':
            queue.append((cur[0], cur[1]+1))
        if (cur[1]) > 0 and maze[cur[0]][cur[1]-1] == ' ' or maze[cur[0]][cur[1]-1] == '.':
            queue.append((cur[0], cur[1]-1))
    return "gg"


gg = pacman_bfs(maze, (21, 1), (1, 59))


def pacman_dfs(maze, start, end):
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
            stack.append((cur[0]+1, cur[1]))
        if (cur[0]) > 0 and maze[cur[0]-1][cur[1]] == ' ' or maze[cur[0]-1][cur[1]] == '.':
            stack.append((cur[0]-1, cur[1]))
        if (cur[1]+1) < width and maze[cur[0]][cur[1]+1] == ' ' or maze[cur[0]][cur[1]+1] == '.':
            stack.append((cur[0], cur[1]+1))
        if (cur[1]) > 0 and maze[cur[0]][cur[1]-1] == ' ' or maze[cur[0]][cur[1]-1] == '.':
<<<<<<< HEAD
            stack.append((cur[0], cur[1]-1))
    return visited


wp = pacman_dfs(maze, (21,1), (1,59))
=======
            stack.append((cur[0],cur[1]-1))
    return visited
>>>>>>> 8d27fc125a97c6335e6d088c839859031cb27419
