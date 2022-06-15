# Методичка стр 44


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


print('Please, input x, n:')
x = int(input())
n = int(input())
# Находим делители числа n
factors = []
d = 2
# Пробегаем от 2 до корня из n
while d ** 2 <= n:
    # Пока n делится на d, добавляем єтот делитель и делим n на d
    while n % d == 0:
        factors.append(d)
        n /= d
    d += 1
if n > 1:
    factors.append(int(n))

p, q = factors
print('p: ')
print(p)
print('q: ')
print(q)

# Проверяем по критерию Эйлера, является ли квадратичным вычетом
if binpow(x, int((p - 1) / 2), p) == 1 and binpow(x, int((q - 1) / 2), q) == 1:
    print('+')
else:
    print('-')

