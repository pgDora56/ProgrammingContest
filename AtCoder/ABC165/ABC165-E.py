n,m = map(int,input().split())

stage = 1
i = 2
pl = [False] * n
pair = [["1","2"]]
pl[0] = True
pl[1] = True
while stage < m:
    if n % i != 0:
        i2 = i
        while pl[i2] or pl[(i2+i)%n]:
            i2 = (i2+1) % n
        stage += 1
        pair.append([str(i2+1), str((i2+i)%n+1)])
        pl[i2] = True
        pl[(i2+i)%n] = True 
    i += 1

for p in pair:
    print(" ".join(p))
    
