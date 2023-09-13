S = input()
num = 0
for x in S:
    if S.count(x) > 1:
        num += 1
if num >= 1:
    print("Yes")
else:
    print("NO")