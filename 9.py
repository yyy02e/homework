L = input().split(" ")
def for_sort(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] > s[j]:
                t = s[i]
                s[i] = s[j]
                s[j] = t

def while_sort(s):
    start = 0
    le = 0
    ri = len(s)-1
    while le < ri:
        start = s[le]
        s[le] = s[ri]
        s[ri] = start
        le += 1
        ri -= 1
for_sort(L)
#while_sort(L)
print(L)
