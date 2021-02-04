a, b, k = map(int, input().split())
count = 0
if(a > b):
    tmp = a
    a = b
    b = tmp
for i in range(b, 0, -1):
    if a % i == 0 and b % i == 0:
        count += 1
        if count == k:
            print(i)
            exit(0)