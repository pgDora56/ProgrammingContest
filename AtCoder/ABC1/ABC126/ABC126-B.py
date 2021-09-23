s = input()
p = int(s[:2])
a = int(s[2:])

if 0 < p < 13 and 0 < a < 13:
    print("AMBIGUOUS")
elif 0 < p < 13 and 0 <= a < 100:
    print("MMYY")
elif 0 <= p < 100 and 0 < a < 13:
    print("YYMM")
else:
    print("NA")