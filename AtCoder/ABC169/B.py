n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
if a[-1] == 0:
    print(0)
    exit()
total = 1
maxi = 10 ** 18
for ae in a:
    total *= ae
    if total > maxi:
        print(-1)
        exit()
print(total)

