n, k = map(int,input().split())
r, s, p = map(int,input().split())
t = list(input())
score = 0
for i in range(k):
    if t[i] == "r":
        score += p
    elif t[i] == "s":
        score += r
    else:
        score += s

for i in range(k, len(t)):
    if t[i] != t[i-k]:
        if t[i] == "r":
            score += p
        elif t[i] == "s":
            score += r
        else:
            score += s
    else:
        t[i] = ""

print(score)
