h, w = map(int, input().split())
canvas = []
for _ in range(h):
    row = input()
    canvas.append(row)

for i in range(h):
    for j in range(w):
        if canvas[i][j] == ".": continue
        candraw = False
        for delta in [-1,1]:
            if 0 <= i + delta < h:
                if canvas[i+delta][j]=="#":
                    candraw = True
                    break
            if 0 <= j + delta < w:
                if canvas[i][j+delta]=="#":
                    candraw = True
                    break
        if not candraw:
            print("No")
            exit(0)
print("Yes")