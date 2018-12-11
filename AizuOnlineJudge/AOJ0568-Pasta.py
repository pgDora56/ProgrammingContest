n, k = map(int, input().split())
ans = 0
sche = [0] * (n+1)
dp = [[[0 for i in range(2)] for j in range(4)] for k in range(n+1)]
# dp = [[[0] * 2] * 4] * (n-1) とすると、シャロウになっちゃってダメ
for i in range(k):
    a, b = map(int, input().split())
    sche[a] = b
if(sche[1] != 0): dp[1][sche[1]][0] = 1
else:
    for i in range(1, 4): dp[1][i][0] = 1
for i in range(2, n+1):
    yest = 0
    for j in range(1, 4): yest += dp[i-1][j][0] + dp[i-1][j][1]

    if sche[i] != 0:
        dp[i][sche[i]][0] += (yest - dp[i-1][sche[i]][0] - dp[i-1][sche[i]][1]) % 10000
        dp[i][sche[i]][1] += (dp[i-1][sche[i]][0]) % 10000
    else:
        for j in range(1, 4):
            dp[i][j][0] += (yest - dp[i-1][j][0] - dp[i-1][j][1]) % 10000
            dp[i][j][1] += (dp[i-1][j][0]) % 10000
for i in range(1,4): ans += (dp[n][i][0] + dp[n][i][1]) % 10000
print(ans % 10000)