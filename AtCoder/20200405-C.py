import itertools
a, b, c = map(int, input().split())
boxes = a + b + c
lis = list(itertools.permutations(range(1,boxes+1)))

cnt = 0
    
for l in lis:
    prev = 0
    flag = True
    for i in range(a):
        if prev > l[i]:
            flag = False
            break
        prev = l[i]

    if not flag:
        continue

    prev = 0
    for i in range(a, a+b):
        if prev > l[i] or l[i-a] > l[i]:
            flag = False
            break
        prev = l[i]

    if not flag:
        continue

    prev = 0
    for i in range(a+b, boxes):
        if prev > l[i] or l[i-b] > l[i]:
            flag = False
            break
        prev = l[i]

    if not flag:
        continue

    cnt += 1

print(cnt)
