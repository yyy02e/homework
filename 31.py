#10进制小数转化为2进制
def dectobin(x):
    x -= int(x)
    bins = []
    min = 0.0000001
    while x > min:
        x *= 2
        bins.append(1 if x >= 1. else 0)
        x -= int(x)
    return bins
x = float(input())
print(dectobin(x))