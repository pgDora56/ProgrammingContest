n = int(input()) - 1
a = list(map(int,input().split()))
a.sort(reverse=True)
total = 0
for i in a:
    total += i * n
    n -= 2
print(total)
