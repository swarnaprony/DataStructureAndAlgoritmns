def removeEven(num):
    odd = []
    for i in range(0, len(num)):
        if num[i]%2 != 0:
            odd.append(num[i])
    return odd
n=[1, 2, 3, 4, 5, 6, 7, 8]
print(removeEven(n))