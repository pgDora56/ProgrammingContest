from math import floor
import sys
ns = int(input())
for h in range(1, 3501):
    for n in range(h, 3501):
        if(4 - ns / h - ns / n == 0): continue
        w = float(ns / (4 - ns / h - ns / n) )
        if(w.is_integer() and w > 0):
            print("{} {} {}".format(h, n, int(w)))
            exit()