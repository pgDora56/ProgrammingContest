# Z = 90
n = int(input())
s = input()
res = ""
for i in s:
    code = ord(i) + n
    if code > 90: code -= 26
    res += chr(code)
print(res)
