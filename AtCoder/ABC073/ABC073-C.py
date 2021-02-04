n = int(input())
paper = {}
for _ in range(n):
    x = int(input())
    if x in paper:
        paper[x] += 1
    else:
        paper[x] = 1
count = 0
for i in paper.values():
    if i % 2 != 0: count += 1
print(paper)
print(count)