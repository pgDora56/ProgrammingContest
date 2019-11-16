n = int(input())
s = input()

if n % 2 == 1:
    print("No")
    exit()

nhalf = int(n/2)
if s[:nhalf] == s[-1 * nhalf:]:
    print("Yes")
else:
    print("No")
