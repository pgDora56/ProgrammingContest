# ふくしま Python
# ACずみ
n = int(input())
a = list(map(lambda x: int(x)-1,input().split()))
cnt = 0
for idx in range(len(a)):
    lovers_love = a[a[idx]]
    if lovers_love == -1:
        continue
    if lovers_love == idx:
        cnt += 1
        a[a[idx]] = -1
print(cnt)
