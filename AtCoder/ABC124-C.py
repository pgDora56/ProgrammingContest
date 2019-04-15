s = input()
ans = float('inf')
for j in range(2):
    c = 0
    val = j
    for i in s:
        if val == int(i):
            c += 1
        val = (val + 1) % 2
    ans = min([ans, c])
print(ans)