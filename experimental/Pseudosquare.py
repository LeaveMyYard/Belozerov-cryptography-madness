# Методичка стр 60, стр 37
import random


# Решает задачу ax+by=gcd
# Сначала проверяется, равно ли первое число нулю, если это так, то второе число является делителем,
# а коэффициенты равны 0 и 1, так как “num1 * x + num2 * y = y”
# в том случае, если y = 1, а левое произведение равно нулю.
# Функция возвращает три числа: делитель, коэффициент x и коэффициент y.
# Для её реализации используется рекурсия, делитель получается тем же образом,
# что и в классическом рекурсивным алгоритме, а коэффициенты рекурсивно вычисляются по формулам:
# x = y – (num2 // num1) * x
# y = x
def gcd_extended(a, b):
    if not b:
        return 1, 0, a
    y, x, g = gcd_extended(b, a % b)
    return x, y - (a // b) * x, g


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


n = int(input('Please, input n: '))
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

# Находим квадратичные невычеты каждого делителя рандомным образом
zp = random.randrange(1, p - 1)
while pow(zp, int((p - 1) / 2), p) == 1:
    zp = random.randrange(1, p - 1)

print('zp: ')
print(zp)

zq = random.randrange(1, q - 1)
while pow(zq, int((q - 1) / 2), q) == 1:
    zq = random.randrange(1, q - 1)

print('zq: ')
print(zq)

# По китайской теореме об остатках находим ответ
y = 0
invp, _, _ = gcd_extended(n / p, p)
invq, _, _ = gcd_extended(n / q, q)
y += zp * n / p * invp
y += zq * n / q * invq
print(y % n)
