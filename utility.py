# utility. py
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
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


def heuristicFcn(p, q):
    """
    Using the manhatten distance as the heuristic
    function for Greedy and A star search
    """
    (x1, y1) = p
    (x2, y2) = q
    return abs(x1 - x2) + abs(y1 - y2)
