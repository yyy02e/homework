def newton(x):
    min = 0.0000001
    #guess = x/2
    guess = x/4
    while abs(guess ** 2 - x) >= min:
        guess = guess - (((guess ** 2)-x) / (guess * 2))
    return guess
print(newton(2))