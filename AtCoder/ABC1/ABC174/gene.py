import random
n = random.randrange(1,2*(10**5)+1)
k = random.randrange(0,2*(10**5)+1)
print(n,k)
a = []
for i in range(n):
    a.append(str(random.randrange(1,10**9+1)))
print(" ".join(a))

