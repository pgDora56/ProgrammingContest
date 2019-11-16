def f(n, x):
    if n >= 0: return n//x+1
    else: return 0

a,b,x = map(int, input().split())
print(f(b,x)-f(a-1,x))

