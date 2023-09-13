def three_root(n):
    if n < 0:
        cur = -n
    else:
        cur = n
    pre = 0.0001
    low = 0
    high = cur/2
    while abs(high * high * high - cur) > pre:
        if high * high * high > cur:
            high = high - (high - low) / 2
        else:
            high = high + (high - low) / 2
    return high

x = float(input())
if x< 0:
    print("%.5f" % -three_root(x))
else:
    print("%.5f" % three_root(x))
