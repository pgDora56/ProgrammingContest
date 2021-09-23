N = int(input())
for i in range(1,N): N = N * i % (10**9+7)
print(N)
