#找出两个正整数的最大公约数
def findcd(a,b):
    if a < b:
        a,b = b,a
    x = a % b
    while x != 0:
        a = b
        b = x
        x = a % b
    return b
a = int(input())
b = int(input())
print(findcd(a,b))
