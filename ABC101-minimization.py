from math import ceil
n, k = map(int, input().split())
min_idx = list(map(int, input().split())).index(1)
min_count = n
left = min_idx - k + 1
if left < 0: left = 0
for i in [left, min_idx]:
    s_idx, l_idx = i, i + k - 1
    if s_idx < 0: s_idx = 0
    if l_idx > n - 1: l_idx = n - 1
    count = ceil(s_idx / (k - 1)) + ceil((n - 1 - l_idx) / (k - 1)) + 1
    # while s_idx > 0:
    #     s_idx -= k - 1
    #     count += 1
    # while l_idx < n - 1:
    #     l_idx += k - 1
    #     count += 1
    if min_count > count: min_count = count
print(min_count)