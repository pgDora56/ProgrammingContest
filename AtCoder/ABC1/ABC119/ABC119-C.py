n, ao, bo, co = map(int, input().split())
l = [int(input()) for _ in range(n)]

def solve(ln, a, b, c):
    if len(l) <= ln:
        if a * b * c > 0:
            return abs(ao - a) + abs(bo - b) + abs(co - c)
        else:
            return float("inf")
    
    x = l[ln]
    return min([
        solve(ln + 1, a, b, c),
        solve(ln + 1, a + x, b, c) + (10 if a > 0 else 0),
        solve(ln + 1, a, b + x, c) + (10 if b > 0 else 0),
        solve(ln + 1, a, b, c + x) + (10 if c > 0 else 0)
    ])
print(solve(0, 0, 0, 0))