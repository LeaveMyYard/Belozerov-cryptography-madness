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
Px = float(input('Please, input x coordinate of P: '))
Py = float(input('Please, input y coordinate of P: '))
q = int(input('Please, input order of the field: '))

x = []
y = []

x.append(Px)
y.append(Py)


inv_2, _, _ = gcd_extended(2, q)
inv_Py, _, _ = gcd_extended(Py, q)
Px_new = (binpow((3 * Px * Px + a) * inv_2 * inv_Py % q, 2, q) - 2 * Px) % q
x.append(Px_new)
Py_new = (-Py+((3 * Px * Px + a) * inv_2 * inv_Py % q)*(Px-Px_new) % q) % q
y.append(Py_new)

# Будем прибавлять P, пока не будет такая сумма, что икс такой уже есть, причем с противополжным игреком
while (-Py_new) % q not in y or x[y.index((-Py_new) % q)] != Px_new:
    Px = Px_new
    Py = Py_new
    inv_Px_x0, _, _ = gcd_extended(Px - x[0], q)
    Px_new = (binpow((Py - y[0]) * inv_Px_x0, 2, q) - x[0] - Px) % q
    x.append(Px_new)
    Py_new = (-y[0] + (Py - y[0]) * inv_Px_x0 *(x[0] - Px_new) % q) % q
    y.append(Py_new)

print(x, y)
print(y.index((-Py_new) % q) + len(y) + 1)
