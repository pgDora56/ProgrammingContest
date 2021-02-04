from collections import deque
import sys
from copy import deepcopy

sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, p, c):
        self.next = p
        self.score = c
        self.visited = 0
        self.points = []
        self.best_score = -1

    def search(self, step, maxi_search = True):
        if self.visited == 2: return (self.best_score, self.points)
        if self.visited == 1:
            # Loop
            node = tree[self.next]
            pnt = 0
            pnttmp = [self.score]
            if maxi_search:
                best = -float('inf')
                for i in range(step-1):
                    pnt += node.score
                    pnttmp.append(pnt + self.score)
                    node = tree[node.next]
            else:
                best = float('inf')
                for i in range(step-1):
                    pnt += node.score
                    pnttmp.append(pnt + self.score)
                    node = tree[node.next]
            return (best, pnttmp)
        self.visited = 1

        # Not loop
        best, n_points = tree[self.next].search(step, maxi_search)
        print((best, n_points))
        pnttmp = [self.score]
        if maxi_search:
            for p in n_points:
                best = max(best, p)
                pnttmp.append(self.score + p)
        else:
            for p in n_points:
                best = min(best, p)
                pnttmp.append(self.score + p)
        self.points = deepcopy(pnttmp[:-1])
        self.best_score = best
        self.visited = 2
        return (best, pnttmp[:-1])



n, k = map(int,input().split())
p = deque(map(int,input().split()))
c = deque(map(int,input().split()))

tree = []
tree2 = []

for _ in range(n):
    ps = p.popleft() - 1
    cs = c.popleft()
    tree.append(Node(ps,cs))
    tree2.append(Node(ps,cs))

if k <= n:
    b = -float("inf")
    for t in tree:
        bes, _ = t.search(k)
        print(t.points, t.best_score)
        b = max(bes,b)
    print(b)
else:
    b = -float("inf")
    for t in tree:
        bes, _ = t.search(n)
        print(t.points, t.best_score)
        b = max(bes,b)
    print(f"{b=}") # 1周した
    b2 = -float("inf")
    for t in tree2:
        bes, _ = t.search(k%n)
        print(t.points, t.best_score)
        b2 = max(bes,b2)
    print(f"{b2=}") # amari

    if tree[0].points[-1] < 0:
        print(b)
    else:
        full = tree[0].points[-1] * (k // n) + b2
        print(f"{b=} {full=}")
        print(max(b,full))


    
