n = int(input())
a = []
maxi = [0, 0]
for _ in range(n):
    a.append(int(input()))
    if maxi[0] < a[-1]: 
        maxi[1] = maxi[0]
        maxi[0] = a[-1]
    elif maxi[1] < a[-1]:
        maxi[1] = a[-1]

for x in a:
    if x == maxi[0]: print(maxi[1])
    else: print(maxi[0])




