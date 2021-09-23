import sys

sys.setrecursionlimit(10**6)

n,m,q = map(int,input().split())
score = []
for _ in range(q):
    score.append(list(map(int,input().split())))

def search(lis):
    global n,m,score
    if len(lis)==n:
        total = 0
        for s in score:
            if lis[s[1]-1]-lis[s[0]-1]==s[2]: total += s[3]
        return total
        
    first = 1 if len(lis) == 0 else lis[-1]
    res = []
    for i in range(first, m+1):
        nlis = lis + [i]
        res.append(search(nlis))
    return max(res)

print(search([]))
