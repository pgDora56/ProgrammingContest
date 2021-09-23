# -*- coding: utf-8 -*-
n = int(input())
hi = list(map(int, input().split()))
flag = False
cnt = 0
while sum(hi)>0:
    flag = False
    for hidx in range(len(hi)):
        if hi[hidx] > 0:
            if not flag:
                cnt += 1
                flag = True
            hi[hidx] -= 1
        else:
            flag = False
print(cnt)
