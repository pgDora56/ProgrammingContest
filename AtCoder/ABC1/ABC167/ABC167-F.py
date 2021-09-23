n = int(input())
sent = []
for _ in range(n):
    s = input()
    lis = [0,0]
    for c in s:
        if c == ")" and lis[1] > 0:
            lis[1] -= 1
        elif c == "(":
            lis[1] += 1
        else:
            lis[0] += 1
    if lis != [0,0]: sent.append(lis)

print(sent)

