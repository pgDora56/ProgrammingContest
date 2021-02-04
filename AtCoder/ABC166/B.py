n, k = map(int,input().split())
have = [False] * n
for _ in range(k):
    d = input()
    a = list(map(lambda x: int(x)-1, input().split()))
    for x in a:
        have[x] = True

print(have.count(False))

