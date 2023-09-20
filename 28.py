#方法1(BBP公式）
pi = 0
N = 100
for i in range(N):
    pi += 1 / pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print("%.10lf" % pi)
#方法2（蒙特卡洛）
import random
n = 1000 * 1000
k = 0
for i in range(n):
    x,y = random.random(),random.random()
    dist = pow(x**2 + y ** 2,0.5)
    if dist<=1.0:
        k += 1
pi1 = 4 * (k/n)
print("%.10lf" % pi1)
#方法3(梅钦法）
import math
pi2 = 4*(4*math.atan(1/5)-math.atan(1/239))
print("%.10lf" % pi2)
#方法4（无穷级数法）
a = 1
b = 1
sum = 0
while 1/b > 0.000001:
    if a % 2 != 0:
        sum += 1/b
    else:
        sum -= 1/b
    a += 1
    b += 2
pi3 = sum*4
print("%.10lf" % pi3)

