s = input() # しらべるやつ
t = input() # これがあるか
len_s = len(s)
len_t = len(t)

sdic = {}
for idx in range(len_s):
    if s[idx] in sdic:
        sdic[s[idx]].append(idx)
    else:
        sdic[s[idx]] = [idx]

now = -1
loop = 0
def move(lis):
    global now, loop
    if now < lis[0]:
        now = lis[0]
        return
    for idx in range(1, len(lis)):
        if now < lis[idx]:
            now = lis[idx]
            return
    loop += 1
    now = lis[0]

for let_t in t:
    if not let_t in sdic:
        print(-1)
        exit()
    move(sdic[let_t])
print(now + 1 + loop * len_s)
