n, m = map(int, input().split())
students = [list(map(int,input().split())) + [float('inf'), -1] for _ in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    for stu in students:
        dist = abs(stu[0]-x) + abs(stu[1]-y) 
        if dist < stu[2]: stu[2], stu[3] = dist, i+1
for stu in students: print(stu[3])
