n,k = map(int,input().split())
a = list(map(int,input().split()))
balls = {}

for b in a:
    if b in balls:
        balls[b] += 1
    else:
        balls[b] = 1

ballcnts = list(balls.values())
ballcnts.sort()

req_delete = len(ballcnts) - k
if req_delete <= 0: print(0)
else: print(sum(ballcnts[:req_delete]))
