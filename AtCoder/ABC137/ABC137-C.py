def combi2(a):
    if a == 0: return 0
    return a * (a-1) // 2

n = int(input())

datas = []

for _ in range(n):
    datas.append(sorted(input()))

datas.sort()

total = 0
count = 0
for i in range(n-1):
    if datas[i] == datas[i+1]:
        if count == 0: count = 2
        else: count += 1
    else:
        total += combi2(count)
        count = 0
total += combi2(count)
count = 0
print(total)
