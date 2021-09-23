sent = str(input())
tmpsent = sent
lis = []
ss = ""
ss2 = ""
prev = [""]
for i in range(int(len(sent) / 2)):
    pv = []
    for p in prev:
        ss = "0" + p + "1"
        ss2 = "1" + p + "0"
        pv.append(ss)
        pv.append(ss2)
        lis.append(ss)
        lis.append(ss2)
    prev = pv

lis.reverse()
print(lis)
loop = True
while loop:
    loop = False
    for l in lis:
        if tmpsent != tmpsent.replace(l, ''):
            tmpsent = tmpsent.replace(l , '')
            loop = True
            break
print(tmpsent)
print(len(sent) - len(tmpsent))


# def search(let):
#     candi = []
#     for i in range(len(let) - 1):
#         if let[i] != let[i+1]:
#             ss = ""
#             for j in range(i):
#                 ss += str(let[j])
#             for j in range(i+2,len(let)):
#                 ss += let[j]
#             if ss == "":
#                 print(len(sent))
#                 exit(0)
#             candi.append(search(ss))
#     if len(candi) == 0: ncan = [let]
#     else:
#         ncan = sorted(candi, key= lambda x: len(x))
#     return ncan[0]

# print(len(sent)-len(search(sent)))