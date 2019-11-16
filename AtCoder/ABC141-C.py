n, k ,q = map(int,input().split())
scores = [(k-q) for _ in range(n)]
for _ in range(q):
    scores[int(input())-1] += 1
for i in range(n):
    if scores[i] <= 0:
        print("No")
    else:
        print("Yes")
