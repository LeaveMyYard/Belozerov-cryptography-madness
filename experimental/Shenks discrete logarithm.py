# Методичка стр 48, алгоритмические задачи стр 1
import numpy as np


# Возводим a в степень n по модулю m бинарным методом
# Для этого мы представили n в системе счисления с основанием 2
# Если n - четное число, то a^n = a^(n/2)*a^(n/2)
# Иначе - a^n = a^(n-1)*a
def binpow(a, n, m):
    if n == 0:
        return 1 % m
    if n % 2 == 1:
        return (binpow(a, n-1, m) * a) % m
    else:
        b = binpow(a, n/2, m)
        return (b * b) % m


print('Please, input a, g, p:')
a = int(input())
g = int(input())
p = int(input())

k = int(np.sqrt(p)) + 1
m = k

series_1 = np.zeros((1, m))
series_2 = np.zeros((1, k))

for l in range(m):
    series_1[:, l] = (a * binpow(g, l, p)) % p

for l in range(1, k + 1):
    series_2[:, l - 1] = binpow(g, l * m, p)

print(series_1, series_2)

i_last = 0
j_last = 0

for j in range(m):
    for i in range(k):
        if series_1[0, j] == series_2[0, i]:
            print(series_1[0, j])
            i_last = i + 1
            j_last = j

y = i_last * m - j_last
print(y%p)

print(pow(g,y)%p)
