import sys
sys.setrecursionlimit(10**9)

memo = {}
def search(a,b,c,cnt):
    tot = a+b+c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if a in memo:
        if b in memo[a]:
            if c in memo[a][b]:
                return memo[a][b][c]
        else:
            memo[a][b] = {}
    else:
        memo[a] = {}
        memo[a][b] = {}
    chil = 0
    if a==99:
        chil += (cnt+1) * 99
    elif a!=0:
        chil += search(a+1,b,c,cnt+1) * a
    if b==99:
        chil += (cnt+1) * 99
    elif b!=0:
        chil += search(a,b+1,c,cnt+1) * b
    if c==99:
        chil += (cnt+1) * 99
    elif c!=0:
        chil += search(a,b,c+1,cnt+1) * c
    res = chil / tot
    memo[a][b][c] = res
    return chil / tot

a, b, c = map(int, input().split())
print(search(a,b,c,0))
