n = int(input())
letters =[
    [],
    [".",",","!","?", " "],
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
    ["j","k","l"],
    ["m","n","o"],
    ["p","q","r","s"],
    ["t","u","v"],
    ["w","x","y","z"]
]
for _ in range(n):
    enter = input()
    ans = ""
    key = 0
    count = 0
    for k in enter:
        if key == 0:
            key = int(k)
            count = 1
        elif k == "0":
            c = count % len(letters[key]) - 1
            ans += letters[key][c]
        else:
            count += 1
        key = int(k)
    print(ans)

