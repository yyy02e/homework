def insertion(array):
    for i in range(len(array)):
        cur = i
        while array[cur-1]>array[cur] and cur-1 >= 0:
            array[cur-1],array[cur]=array[cur],array[cur-1]
            cur -=1
        print(array)
    return array

array = []
for i in range(0,5):
    a = int(input())
    array.append(a)
print(insertion(array))
