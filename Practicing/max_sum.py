n = int(input())
a = list(map(int,input().split()))

dp = [0 for _ in range(n+1)]

for idx in range(n):
    dp[idx+1] = max(dp[idx], dp[idx]+a[idx])

print(dp[n])
