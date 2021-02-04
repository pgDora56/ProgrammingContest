# AOJ-DPL_1_B-0-1 Knapsack Problem
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp

vi = []
wi = []
n, w = map(int, input().split())
for _ in range(n):
    vt, wt = map(int, input().split())
    vi.append(vt)
    wi.append(wt)

dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for iidx in range(n):
    for widx in range(w+1):
        if widx >= wi[iidx]:
            dp[iidx+1][widx] = max(dp[iidx][widx-wi[iidx]] + vi[iidx], dp[iidx][widx])
        else:
            dp[iidx+1][widx] = dp[iidx][widx]

        print(f"\n\n## i = {iidx+1}, w = {widx}")
        for row in dp:
            print(row)

print(dp[n][w])
