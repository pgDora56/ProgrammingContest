# 動的計画法(DP)の簡単な例

def Fibo(n):
    table = [-1] * n
    table[0] = 0
    table[1] = 1
    for x in range(n - 2): table[x + 2] = table[x] + table[x + 1]
    return table[n-2] + table[n-1]

print(Fibo(100))