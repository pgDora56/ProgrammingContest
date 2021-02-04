person = [0 for _ in range(5)]
n = int(input())
for _ in range(n):
    name = input()
    if name[0] == "M":
        person[0] += 1
    elif name[0] == "A":
        person[1] += 1
    elif name[0] == "R":
        person[2] += 1
    elif name[0] == "C":
        person[3] += 1
    elif name[0] == "H":
        person[4] += 1

total = 0
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            total += person[i] * person[j] * person[k]
print(total)