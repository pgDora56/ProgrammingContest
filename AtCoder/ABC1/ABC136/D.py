s = input()
n = [0] * len(s)
s += "R"

start = 0
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cnt = i - start
        if s[i-1] == "L":
            if cnt % 2 == 1: n[start] += 1
            n[start-1] += cnt // 2
            n[start] += cnt // 2
        else:
            if cnt % 2 == 1: n[i-1] += 1
            n[i-1] += cnt // 2
            n[i] += cnt // 2
        start = i
op = ""
for i in range(len(n)):
    if i != 0: op += " "
    op += str(n[i])
print(op)

