num =int(input())
def find_max_list(n):
    x = n % 3
    y = int(n/3)
    result = []
    if x == 0:
        for i in range(y):
            result.append(3)
    elif x == 1:
        result.append(2)
        result.append(2)
        for i in range(y - 1):
            result.append(3)
    else:
        result.append(2)
        for i in range(y):
            result.append(3)
    return result
print(find_max_list(num))

