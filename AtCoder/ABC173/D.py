from collections import deque
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
score = deque([a.pop(0)])

total = 0

for i in a:
    total += score.popleft()
    score.append(i)
    score.append(i)
print(total)
