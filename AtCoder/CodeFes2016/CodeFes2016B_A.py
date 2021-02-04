s = input()

cnt = 0
for i in range(16):
    if s[i] != "CODEFESTIVAL2016"[i]:
        cnt += 1
print(cnt)

