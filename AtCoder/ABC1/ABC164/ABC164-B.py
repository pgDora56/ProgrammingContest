A,B,C,D = map(int, input().split())

while A > 0 and C > 0:
    C -= B
    if C <= 0:
        print("Yes")
        exit()
    A -= D
    if A <= 0:
        print("No")
        exit()

print(f"{A} {B} {C} {D}")
