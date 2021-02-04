CONST = 10**9+7
n = int(input())
s = input()

chars = {}
for c in s:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1

val = 1
for i in chars.values():
    val = (val * (i+1)) % CONST
print(val-1)
