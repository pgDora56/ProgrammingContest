from collections import deque

intd = lambda x: int(x) - 1

r, c = map(intd, input().split())
sy, sx = map(intd, input().split())
gy, gx = map(intd, input().split())
fmap = [input() for _ in range(r)]
hand = [[-1] * c for _ in range(r)]

queue = deque()
queue.append((sy,sx))
hand[sy][sx] = 0

while len(queue) > 0:
    loc = queue.popleft()
    nhand = hand[loc[0]][loc[1]] + 1
    checkreq = deque()

    for y in range(max(0,loc[0]-1), min(r,loc[0]+2)):
        checkreq.append((y,loc[1]))
    for x in range(max(0,loc[1]-1), min(c,loc[1]+2)):
        checkreq.append((loc[0], x))
    
    for ch in checkreq:
        y,x = ch
        if fmap[y][x] == ".":
            if hand[y][x] == -1:
                if y == gy and x == gx:
                    print(nhand)
                    exit()
                else:
                    hand[y][x] = nhand
                queue.append((y,x))

