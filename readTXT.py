import numpy as np
np.set_printoptions(threshold=np.nan)


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


def read_txt(fname, row, col):
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


def find_enter_exit(maze):
    enter_row = 0
    enter_col = 0
    exit_row = 0
    exit_col = 0
    for i in range(0, maze.shape[0]-1):
        for j in range(0, maze.shape[1]-1):
            if maze[i][j] == "P":
                enter_row = i
                enter_col = j
            if maze[i][j] == ".":
                exit_row = i
                exit_col = j
    return enter_row, enter_col, exit_row, exit_col


row, col = get_size_txt('mediumMaze.txt')


maze = read_txt('mediumMaze.txt', row, col)
enter_row, enter_col, exit_row, exit_col = find_enter_exit(maze)
print(row, col)
print(maze)
print(maze[enter_row, enter_col], maze[exit_row, exit_col])
