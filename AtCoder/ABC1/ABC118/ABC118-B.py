n, m = map(int, input().split())
flag = []
for _ in range(m): flag.append(0)
for _ in range(n):
    line = list(map(int, input().split()))
    for i in range(line[0]): flag[line[i+1]-1] += 1
count = 0
for j in range(m):
    if(flag[j] == n): count += 1
print(count)