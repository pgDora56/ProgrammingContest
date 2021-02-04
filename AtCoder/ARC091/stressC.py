import random
def solver1(n,m):
    if n == 1 or m == 1:
        return(n*m-2)
    else:
        return((n-2)*(m-2))

def solver2(n,m):
    cards = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
             for ii in range(max(0,i-1), min(m,i+2)):
                 for jj in range(max(0,j-1), min(n,j+2)):
                     cards[ii][jj] = not cards[ii][jj]
    cnt = 0
    for i in range(m):
        cnt += cards[i].count(True)
    return cnt

#n,m = map(int,input().split())

# loop = True
# while loop:
#     n = random.randrange(1,100)
#     m = random.randrange(1,100)
#     s1 = solver1(n,m)
#     s2 = solver2(n, m)
#     loop = s1 == s2
#     print(loop, s1, s2, n, m)

for n in range(1,100):
    for m in range(1,100):
        s1 = solver1(n,m)
        s2 = solver2(n, m)
        loop = s1 == s2
        print(loop, s1, s2, n, m)
        if not loop:
            input()
