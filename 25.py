def newton(x):
    min = 0.0000001
    guess = x/2
    while abs(guess ** 2 - x) >= min:
        guess = guess - (((guess ** 2)-x) / (guess * 2))
    return guess

print(newton(2000))
print(newton(2))
print(newton(50))