A = input().split()
B = []
for i in range(len(A)):
    x = 1
    for j in range(len(A)):
        if j != i:
            x *= int(A[j])
    B.append(x)
print(B)

