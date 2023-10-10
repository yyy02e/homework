a = int(input())
sum = 0
for i in range(2, a):
    if a%i == 0:
        sum = 1
if sum == 0 and a != 1:
    print(a,'是质数')
else:
    print(a,'不是质数')
