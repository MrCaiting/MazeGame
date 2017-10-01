from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np

def MSTdistance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def maze2tree(goals):
    treesize = len(goals)
    s = (treesize,treesize)
    tree = np.zeros(s).astype(int)
    for i in range(treesize):
        for j in range(i+1, treesize):
            tree[i][j] = MSTdistance(goals[i-1], goals[j-1])
    return tree


def findMSTweight(MST_tree):
    return np.sum(MST_tree)
