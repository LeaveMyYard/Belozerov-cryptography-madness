# Методичка стр 68


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


def Euler_criterion(x, p):
    if binpow(x, int((p - 1) / 2), p) == 1:
        return 1
    elif binpow(x, int((p - 1) / 2), p) == p-1:
        return -1
    else:
        return 0


a = float(input('Please, input a: '))
b = float(input('Please, input b: '))
q = int(input('Please, input order of the field: '))

# Формула 11.4
N = 1 + q
for i in range(q):
    N += Euler_criterion(int(i**3 + a*i + b), q)
    print(Euler_criterion(int(i**3 + a*i + b), q))

print(N)

