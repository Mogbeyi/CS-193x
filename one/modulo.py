def modulo(n, x):
    result = 0

    while (n >= x):
        n -= x
        result += 1

        if n == 0:
            result == 0

    return result

print(modulo(22, 10))
print(modulo(20, 10))
