import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.nan)

def get_size_txt(fname):
    with open(fname) as f:
        row_count = 0
        col_count = 0
        for char in f.read():
            if char == "\n":
                row_count= row_count + 1
            if char != "\n":
                col_count = col_count + 1
    return row_count+1, int( col_count/(row_count+1))

def read_txt(fname,row,col):
    list = []
    with open(fname) as f:
        while True:
            ch = f.read(1)
            if ch != "\n" and ch != '':
                list.append(ch)
            if not ch: break
    maze = np.array(list)
    maze = maze.reshape(row,col)

    return maze

row, col = get_size_txt('mediumMaze.txt')
maze = read_txt('mediumMaze.txt',row, col)
print(row, col)
print(maze)

