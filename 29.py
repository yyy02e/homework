import math
import random
def f(x):
    return x ** 2 + 4*x*math.sin(x)
def Monte_Method(a, b):
    result = 0
    # (a,b)是积分区间
    for i in range(1000000):
        x = random.uniform(a, b)
        result += f(x)*(b-a)
        #result是每次面积
    return result / 1000000
final = Monte_Method(2, 3)
print("%.6f" % final)
