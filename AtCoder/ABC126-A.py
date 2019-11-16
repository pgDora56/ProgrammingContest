n, k = map(int, input().split())
s = input()
dic = {"A": "a", "B": "b", "C": "c"}
print((s[:k-1] if k != 1 else "") + dic[s[k-1]] + (s[k:] if k < n else "") )
