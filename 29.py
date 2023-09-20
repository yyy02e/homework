import math
import numpy as np
def f(x):
    return x ** 2 + 4*x*math.sin(x)
def Monte_Method(a, b):
    # (a,b)是积分区间
    x = np.random.uniform(a, b, 1000000)
    result = 0
    for i in x:
        result += f(i)

    return result / 1000000


final = Monte_Method(2, 3)
print("%.6f" % final)
