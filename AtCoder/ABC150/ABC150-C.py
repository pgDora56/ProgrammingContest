from itertools import permutations

n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
if p == q:
    print(0)
    exit()
base = sorted(p)
pi = 0
qi = 0
for i, v in enumerate(permutations(base, n)):
    if p == v:
        pi = i + 1
    elif q == v:
        qi = i + 1
        
    if pi * qi != 0:
        break
print(abs(pi-qi))


