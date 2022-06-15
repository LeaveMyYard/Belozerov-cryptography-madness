# Методичка стр 44, алгоритмические задачи стр 3
import random


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


print('Please, input a, n:')
a = int(input())
n = int(input())

# Найдем множители числа n
n_new = n
factors = []
d = 2
# Пробегаем от 2 до корня из n
while d ** 2 <= n:
    # Пока n делится на d, добавляем этот делитель и делим n на d
    while n % d == 0:
        factors.append(d)
        n /= d
    d += 1
if n > 1:
    factors.append(int(n))

n = n_new

p, q = factors
print('p: ', 'q: ')
print(p, q)

print(a%p)
# Если a - квадратичный вычет, то проделываем следующие действия, если нет, то нет
if binpow(a, int((p - 1) / 2), p) == 1:
    # Если p=4m+3, то  по критерию Эйлера x^(2m+1)=1(mod p)
    if p % 4 == 3:
        m = (p - 3) // 4
        # и поэтому, домножая обе части полученного сравнения на х,
        # получаем y = +- x^(m+1) (mod p)
        up1 = binpow(a, m + 1, p)
        up2 = -binpow(a, m + 1, p) % p
        print(up1, up2)
        print('1')
    # Если p=8m+5, то  по критерию Эйлера x^(4m+2)=1(mod p)
    elif p % 8 == 5:
        # откуда, извлекая корень квадратный из обеих частей сравнения, имеем
        # x^(2m+1)=+-1(mod p)
        m = (p - 5) // 8
        # учитывая, что в этом случае
        # 2^(4m+2)=-1(mod p)
        # получаем y=+-x^(m+1)*2^(2m+1)(mod p)
        # для x^(2m+1)=-1 (mod p)
        if binpow(a, 2 * m + 1, p) == p - 1:
            up1 = (binpow(a, m + 1, p) * binpow(2, 2 * m + 1, p)) % p
            up2 = (-binpow(a, m + 1, p) * binpow(2, 2 * m + 1, p)) % p
            print('2.1')
        # Иначе y = +-x^(m+1)(mod p)
        else:
            up1 = binpow(a, m + 1, p)
            up2 = (-binpow(a, int(m) + 1, p)) % p
            print('2.2')
    # Если p=8m+1...
    elif p % 8 == 1:
        # Пусть p=2^k*t+1, где (t, 2)=1, k>=3
        k = 3
        t = (p - 1) // binpow(2, k)
        print('k: , t: ')
        # Будем подбирать соответсвтующие k и t
        while (p - 1) % binpow(2, k) != 0 or t % 2 != 1:
            k += 1
            t = (p - 1) // binpow(2, k)
        print(k, t)
        # Из критерия Эйлера получаем, что
        # x^(2^(k-1)*t)=1(mod p), откуда имеем x^(2^(k-2)*t)=+-1(mod p)
        # Выберем квадратичный невычет z(mod p)
        z = random.randrange(1, p - 1)
        while binpow(z, int((p - 1) / 2), p) == 1:
            z = random.randrange(1, p - 1)
        # Тогда z^(2^(k-1)*t)=-1(mod p)
        print('z: ')
        print(z)
        # Отсюда, для любого целого s_1, равного 0 или t, получаем
        # x^(2^(k-2)*t)*z^(s_1*2^(k-1))=1(mod p), x^(2^(k-3)*t)*z^(s_1*2^(k-2))=+-1(mod p)
        s = 0
        k -= 1
        # Из последнего равенства аналогичным образом для некоторого целого
        # неотрицательного s_2 получаем
        # x^(2^(k-3)*t)*z^(s_2*2^(k-2))=1(mod p), x^(2^(k-4)*t)*z^(s_2*2^(k-3))=+-1(mod p)
        while k != 0:
            if (binpow(a, binpow(2, k - 1) * t, p) * binpow(z, s, p)) % p != 1:
                s += (p - 1) // 2
            s //= 2
            k -= 1
        # Повторяя эту процедуру еще k-3 раз, получим для некоторого неотрицательного s_(k-1) равенство
        # x^t*z^(2*s_(k-1))=1(mod p)
        print('s_(k-1): ')
        print(s)
        # y = +- x^((t+1)/2)*z^s_(k-1)(mod p)
        up1 = (binpow(a, (t + 1) // 2, p) * binpow(z, s, p)) % p
        up2 = (-binpow(a, (t + 1) // 2, p) * binpow(z, s, p)) % p
        print('3')
else:
    print('No solution')

if binpow(a, int((q - 1) / 2), q) == 1:
    if q % 4 == 3:
        m = (q - 3) // 4
        uq1 = binpow(a, m + 1, q)
        uq2 = -binpow(a, m + 1, q) % q
        print('1')
    elif q % 8 == 5:
        m = (q - 5) // 8
        if binpow(a, 2 * m + 1, q) == q - 1:
            uq1 = (binpow(a, m + 1, q) * binpow(2, 2 * m + 1, q)) % q
            uq2 = (-binpow(a, m + 1, q) * binpow(2, 2 * m + 1, q)) % q
            print('2.1')
        else:
            uq1 = binpow(a, m + 1, q)
            uq2 = (-binpow(a, int(m) + 1, q)) % q
            print('2.2')
    elif q % 8 == 1:
        k = 3
        t = (q - 1) // pow(2, k)
        print(k, t)
        while (q - 1) % pow(2, k) != 0 or t % 2 != 1:
            k += 1
            t = (q - 1) // pow(2, k)
            print(k, t)
        z = random.randrange(1, q - 1)
        while pow(z, int((q - 1) / 2), q) == 1:
            z = random.randrange(1, q - 1)
        print('z: ')
        print(z)
        s = 0
        k -= 1
        while k != 0:
            if (binpow(a, pow(2, k - 1) * t, q) * binpow(z, s, q)) % q != 1:
                s += (q - 1) // 2
            s //= 2
            k -= 1
        print('s_(k-1): ')
        print(s)
        uq1 = (binpow(a, (t + 1) // 2, q) * binpow(z, s, q)) % q
        uq2 = (-binpow(a, (t + 1) // 2, q) * binpow(z, s, q)) % q
        print('3')
else:
    print('No solution')

print(up1, up2, uq1, uq2)

# По китайской теореме об остатках находим ответ
print('ANSWERS: ')

y = 0
invp, _, _ = gcd_extended(n // p, p)
invq, _, _ = gcd_extended(n // q, q)
y += up1 * n // p * invp
y += uq1 * n // q * invq
print(y % n)

y = 0
y += up2 * n // p * invp
y += uq1 * n // q * invq
print(y % n)

y = 0
y += up1 * n // p * invp
y += uq2 * n // q * invq
print(y % n)

y = 0
y += up2 * n // p * invp
y += uq2 * n // q * invq
print(y % n)
