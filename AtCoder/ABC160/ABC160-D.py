n, x, y = map(int, input().split())
x -= 1
y -= 1
cnt = [0] * (n-1)

def calc(i, j):
    return min(j-i, (abs(i-x)+abs(j-y)+1))

for i in range(n-1):
    for j in range(i+1, n):
        cnt[calc(i,j)-1] += 1

for c in cnt: print(c)
