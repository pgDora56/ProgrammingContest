n = int(input())
totalJPY = 0
for _ in range(n):
    data = input().split()
    if data[1] == "JPY":
        totalJPY += float(data[0])
    else:
        totalJPY += float(data[0]) * 380000
print(totalJPY)