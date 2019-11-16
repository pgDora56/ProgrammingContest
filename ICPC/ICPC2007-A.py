while True:
    n = int(input())
    if n == 0: break
    s = []
    for _ in range(n):
        s.append(int(input()))
    print(int((sum(s)-max(s)-min(s))/(n-2)))
