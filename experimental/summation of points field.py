# Методичка стр 68


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


a = float(input('Please, input a: '))
b = float(input('Please, input b: '))
Px = float(input('Please, input Px: '))
Py = float(input('Please, input Py: '))
Qx = float(input('Please, input Qx: '))
Qy = float(input('Please, input Qy: '))
q = int(input('Please, input order of the field: '))

# Используем формулу 11.2
if Px != Qx:
    inv_Qx_Px, _, _ = gcd_extended(Qx - Px, q)
    Sx = (binpow((Qy - Py) * inv_Qx_Px, 2, q) - Px - Qx) % q
    Sy = (-Py + (Qy - Py) * inv_Qx_Px * (Px - Sx) % q) % q
    print(Sx, Sy)

# Используем формулу 11.3
elif Px == Qx and Py == Qy:
    inv_2, _, _ = gcd_extended(2, q)
    inv_Py, _, _ = gcd_extended(Py, q)
    Sx = (binpow((3 * Px * Px + a) * inv_2 * inv_Py % q, 2, q) - 2 * Px) % q
    Sy = (-Py + ((3 * Px * Px + a) * inv_2 * inv_Py % q) * (Px - Sx) % q) % q
    print(Sx, Sy)

else:
    print('Нулевая точка')
