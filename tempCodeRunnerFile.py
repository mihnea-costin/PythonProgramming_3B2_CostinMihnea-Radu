def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        list = fibonacci(n-1)
        list.append(list[-1] + list[-2])
        return list

print(fibonacci(5))