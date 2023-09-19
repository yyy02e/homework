def binary_search(x):
    min = 0.00000001
    low = 0.0
    if x > 1.0:
        high = x
    else:
        high = 1.0
    g = (low + high) / 2.0
    while abs(g ** 2 - x) >= min:
        if g ** 2 < x:
            low = g
        else:
            high = g
        g = (high + low) / 2.0
    return g

n = 2.0
print(binary_search(n))
