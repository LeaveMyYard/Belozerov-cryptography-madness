def sqrt(a, n):
    for i in range(n):
        if pow(i, 2, n) == a:
            return i
    return None


print(sqrt(19, 4331))