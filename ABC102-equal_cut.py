n = int(input())
a = list(map(int, input().split()))
quarter = sum(a) / 4
print(quarter)

def check(a, n, idx, l):
    print("check({}, {}, {}, {})".format(a, n, idx, l))
    tot = 0
    if len(l) > 2:
        for i in range(idx,n):
            tot += a[i]
        l.append(tot)
        print(tot)
        print("return: {}".format(max(l) - min(l)))
        return max(l) - min(l)
    while idx < n:
        if tot + a[idx] >= quarter:
            l2 = list(l)
            l.append(tot)
            l2.append(tot + a[idx])
            s = check(a, n, idx, l) 
            b = check(a, n, idx + 1, l2)
            return min(s, b)
        tot += a[idx]
        idx += 1
    l.append(tot)
    return check(a, n, idx, l)
print(check(a, n, 0, []))


# n = int(input())
# a = [int(i) for i in input().split()]
# for i in range(1,n):
#     a[i]+=a[i-1]
# l,r,ans = 1,3,float("inf")
# for i in range(2,n-1):
#     num, num2 = abs(2*a[l-1]-a[i-1]), abs(2*a[r-1]-a[i-1]-a[n-1])
#     while num>abs(2*a[l]-a[i-1]) and l<i-1:
#         l, num = l+1, abs(2*a[l]-a[i-1])
#     while num2>abs(2*a[r]-a[i-1]-a[-1]) and r<n-1:
#         r, num2 = r+1, abs(2*a[r]-a[i-1]-a[-1])
#     ans = min(ans,max(a[l-1],a[i-1]-a[l-1],a[r-1]-a[i-1],a[-1]-a[r-1])-min(a[l-1],a[i-1]-a[l-1],a[r-1]-a[i-1],a[-1]-a[r-1]))
# print(ans)