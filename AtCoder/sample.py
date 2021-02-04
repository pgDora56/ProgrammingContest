import time
import random

start = time.time()
lis = []
for i in range(1,10**5):
    lis.append([random.randrange(i), random.randrange(i)])
print(time.time()-start)


start = time.time()
lis = []
for i in range(1,10**5):
    lis.append((random.randrange(i), random.randrange(i)))
print(time.time()-start)
