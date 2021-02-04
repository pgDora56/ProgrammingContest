h,w,k = map(int,input().split())

cells = []
rowBlack = []
columnBlack = [0] * w
for _ in range(h):
    ipt = input()
    rowBlack.append(ipt.count("#"))
    cells.append(ipt)

for cell in cells:
    for i in range(w):
        if cell[i] == "#":
            columnBlack[i] += 1

total = sum(columnBlack)
cnt = 0
for hbit in range(2**h):
    for wbit in range(2**w):
        decBlack = 0

        hlis = []
        for he in range(h):
            if not hbit >> he & 1: continue
            decBlack += rowBlack[he]
            hlis.append(he)

        for we in range(w):
            if not wbit >> we & 1: continue
            decBlack += columnBlack[we]
            for he in hlis:
                if cells[he][we] == "#":
                    decBlack -= 1

        if total - decBlack == k:
            cnt += 1
print(cnt)

