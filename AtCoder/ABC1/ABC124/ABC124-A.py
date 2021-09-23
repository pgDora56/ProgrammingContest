a, b  = map(int, input().split())
if a < b: print(2 * b - 1)
elif b < a: print(2 * a - 1)
else: print(a + b)