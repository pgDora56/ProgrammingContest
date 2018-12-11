import collections as c

n = int(input())
v = list(map(int, input().split()))
v_odd  = []
v_even = []
for i in range(n):
    if i % 2 == 0: v_even.append(v[i])
    else: v_odd.append(v[i])
od_counter = c.Counter(v_odd)
ev_counter = c.Counter(v_even)
odmode = od_counter.most_common()
evmode = ev_counter.most_common()

if odmode[0][0] != evmode[0][0]:
    total = len(v) - odmode[0][1] - evmode[0][1]
    print(total)
else:
    if len(odmode) == 1:
        if len(evmode) == 1:
            print(min(len(v_odd), len(v_even)))
        else:
            print(len(v_even) - evmode[1][1])
    elif len(evmode) == 1:
        print(len(v_odd) - odmode[1][1])
    else:
        odc = len(v) - odmode[0][1] - evmode[1][1]
        evc = len(v) - evmode[0][1] - odmode[1][1]
        print(min(odc, evc))
