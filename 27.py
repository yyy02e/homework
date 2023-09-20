def three_newton(x):
    min = 0.0000001
    guess = x
    guess1 = guess - (guess ** 3 - x) / (3 * guess ** 2)
    while abs(guess1 - guess) >= min:
        guess = guess1
        guess1 = guess - (guess ** 3 - x) / (3 * guess ** 2)
    return guess1
c = 10
print(three_newton(c))
#牛顿三次方根迭代式
