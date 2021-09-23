n = int(input())
tasks = []
for _ in range(n):
    a,b = map(int,input().split())
    tasks.append((a,b))
tasks.sort(key=lambda x:x[1])
t = 0
for task in tasks:
    t += task[0]
    if t > task[1]:
        print("No")
        exit()
print("Yes")
