# combination: 組み合わせ
# cmb = nが大きなときに有効。そうでないときは遅くなる可能性を考慮する。
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot


# 二分探索
import bisect
a=[1,3,5,7,9,11,13,15,17,19]
x=4
insert_index = bisect.bisect_left(a,x)

"""
insert_index=2
"""

a.insert(insert_index,x)
print(a)
"""
Out[1]:[1,3,4,5,7,9,11,13,15,17,19]
"""