def around_tiles(i, j):
    if i % 2 == 0: return [(i-1, j),(i-1, j+1),(i, j-1),(i, j+1),(i+1, j),(i+1, j+1)]
    return [(i-1, j),(i-1, j-1),(i, j-1),(i, j+1),(i+1, j),(i+1, j-1)]

w, h = map(int, input().split())
maps = []
search_queue = []
for i in range(h):
    maps.append(list(map(int, input().split())))

tot = 0
for i in range(h):
    if i in [0, h-1]:
        for j in range(w):
            if maps[i][j] == 0:
                search_queue.append((i, j))
    else:
        for j in [0, w-1]:
            if maps[i][j] == 0:
                search_queue.append((i, j))
history = list(search_queue)
count = 0
while len(search_queue) > 0:
    tile = search_queue.pop(0)
    if not (0 <= tile[0] < h and 0 <= tile[1] < w): continue
    if maps[tile[0]][tile[1]] == 1: continue
    history.append(tile)
    for t in around_tiles(tile[0], tile[1]):
        if not (t in history or t in search_queue): search_queue.append(t)

for i in range(-1, h+1):
    if i in [-1, h]:
        for j in range(-1, w+1):
            history.append((i, j))
    else:
        for j in [-1, w]:
            history.append((i, j))
tot = 0
for i in range(h):
    for j in range(w):
        if maps[i][j] == 1:
            for t in around_tiles(i, j):
                if t in history:
                    tot += 1
print(tot)
