n,k = map(int, input().split())
nums = []
for _ in range(n):
    a, b = map(int, input().split())
    nums.append((a,b))
nums.sort(key=lambda x: x[0])
for t in nums:
    k -= t[1]
    if k <= 0:
        print(t[0])
        break
