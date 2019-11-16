while True:
    n = int(input())
    if n == 0: break
    
    trains = []
    for _ in range(n):
        dept, ariv = input().split()
        trains.append((dept, ariv))
    trains.sort(key=lambda x:x[0])
    dcheck = 0
    usecar = 0
    returntime = []
    for tridx in range(len(trains)):
        new = True
        for ariv in returntime:
            if ariv <= trains[tridx][0]:
                new = False
                returntime.remove(ariv)
                break
        if new: usecar += 1
        returntime.append(trains[tridx][1])
    print(usecar)

