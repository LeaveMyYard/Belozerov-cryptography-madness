# Методичка стр 47


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


p = int(input('Please, input p: '))

# Каноническое разложение числа p-1
factors = []
d = 2
p_1 = p - 1
while d ** 2 <= p_1:
    while p_1 % d == 0:
        factors.append(d)
        p_1 /= d
    d += 1
if p_1 > 1:
    factors.append(int(p_1))
print('Множители числа p-1: ')
print(factors)

# если задано каноническое разложение числа р – 1, то задача решается простой проверкой условий
# g^((p-1)/q)=1(mod p)для любого простого q|p-1
for g in range(2, p-1):
    checker = True
    for q in factors:
        if binpow(g, (p - 1) / q, p) == 1:
            checker = False
    if checker:
        print(g)


