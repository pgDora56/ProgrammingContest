import sys

sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, no):
        self.root = None
        self.no = no
    
    def connect(self, node):
        myroot = self.search()
        yourroot = bridge[node].search()
        if myroot != yourroot:
            bridge[min(myroot,yourroot)].root = bridge[max(myroot,yourroot)]

    def search(self):
        if self.root != None:
            n = self.root.search()
            self.root = bridge[n]
            return n
        else:
            return self.no

n, q = map(int,input().split())
bridge = [Node(i) for i in range(n)]
visited = [False] * n
for i in range(q):
    p, a, b = map(int,input().split())
    if p == 0:
        bridge[a].connect(b)
    else:
        aroot = bridge[a].search()
        broot = bridge[b].search()
        if aroot == broot:
            print("Yes")
        else:
            print("No")

