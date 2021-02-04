import sys

sys.setrecursionlimit(10**8)

h, w = map(int,input().split())
town = []
s = (-1, -1)
for i in range(h):
    line = input()
    for cidx in range(len(line)):
        if s != (-1,-1):
            break
        if 's' == line[cidx]:
            s = (i, cidx)
    town.append(list(line))

def search(pnt):
    x, y = pnt
    town[x][y] = "/"
    around = [(i,y) for i in range(max(0,x-1),min(h,x+2))]
    around.extend([(x,i) for i in range(max(0,y-1), min(w,y+2))])
    for p in around:
        if town[p[0]][p[1]] == "g":
            print("Yes")
            exit()
        elif town[p[0]][p[1]] == ".":
            search(p)

search(s)
print("No")
