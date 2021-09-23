s = input()
cnt = s.count("R")
if cnt == 2 and s[1] == "S": cnt -= 1
print(cnt)
