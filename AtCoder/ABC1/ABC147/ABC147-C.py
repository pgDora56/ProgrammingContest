n = int(input())
lis = []
for i in range(n):
    l = []
    a = int(input())
    for j in range(a):
        x, y = map(int,input().split())
        l.append([x-1,y])
    lis.append(l)
    
ho_maxcnt = 0
for i in range(1, 2**n):
    ho_cnt = bin(i).count("1")
    if ho_cnt <= ho_maxcnt: continue
    is_ok = True
    for j in range(n):
        jhonest = (i >> j) & 1
        if jhonest == 0:
            continue
        for say in lis[j]:
            if ((i >> say[0]) & 1) ^ say[1]:
                # Mujun
                is_ok = False
                break
        if not is_ok:
            break
    if not is_ok:
        continue
    if ho_cnt > ho_maxcnt:
        ho_maxcnt = ho_cnt
print(ho_maxcnt)
