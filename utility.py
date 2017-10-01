# utility.py
# All the basic data structure that will be used
#

import heapq


class Stack:
    "Stack data structure"
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()


class Queue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):

        return len(self.list) == 0


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, priority, item):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]


    def isEmpty(self):
        return len(self.elements) == 0

    def clear(self):
        while (self.isEmpty()) != 1:
            self.pop()


def heuristicFcn(p, q):
    """
    Using the manhatten distance as the heuristic
    function for Greedy and A star search
    """
    (x1, y1) = p
    (x2, y2) = q
    return abs(x1 - x2) + abs(y1 - y2)
