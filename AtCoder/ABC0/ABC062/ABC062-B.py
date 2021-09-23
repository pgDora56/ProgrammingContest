h, w = map(int, input().split())
st = ""
for i in range(w+2):
    st += "#"
print(st)

for i in range(h):
    print("#{}#".format(input()))

print(st)
