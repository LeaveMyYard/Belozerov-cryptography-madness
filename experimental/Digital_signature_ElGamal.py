# Методичка стр 87
import random
import numpy as np


def shenks(a, g, p):
    # Выбрать два натуральных числа  m и k такие, что mk>p
    k = int(np.sqrt(p)) + 1
    m = k

    # Вычислить два ряда чисел
    # x, gx, ..., g^(m-1)x (mod p)
    # g^m, g^(2*m), ..., g^(km) (mod p)
    series_1 = np.zeros((1, m))
    series_2 = np.zeros((1, k))

    for l in range(m):
        series_1[:, l] = (a * binpow(g, l, p)) % p

    for l in range(1, k + 1):
        series_2[:, l - 1] = binpow(g, l * m, p)

    # Найти такие i и j, для которых выполняется равенство
    # g^(im)=g^j*x
    i_last = 0
    j_last = 0

    for j in range(m):
        for i in range(k):
            if series_1[0, j] == series_2[0, i]:
                i_last = i + 1
                j_last = j

    # Число y = im-j подать на выход.
    y = i_last * m - j_last
    y = y % p
    print(pow(g, y, p))
    return y


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


alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
            'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы',
            'Ь', 'Э', 'Ю', 'Я']

M = input('Please, input a message to falsificare: ')

# Переведем текст в числа
M_new = ''
for letter in M:
    new = str(alphabet.index(letter))
    new = '0' * (2 - len(new)) + new
    M_new += new
print(M_new)

p = int(input('Please, input p: '))
g = int(input('Please, input g: '))
h = int(input('Please, input h: '))

# выбираем случайное число r из Z*_(p-1);
random.seed(1)
r = random.randint(1, p - 1)
counter = 2
# r и p-1 должны быть взаимнопростыми, поэтому добьемся этого
r1, _, gcd = gcd_extended(r, p-1)
while gcd != 1:
    random.seed(counter)
    r = random.randint(1, p - 1)
    r1, _, gcd = gcd_extended(r, p-1)
    counter += 1

print('r: ')
print(r)

# вычисляем s_1 = g^r(mod p)
s1 = binpow(g, r, p)
print('s1: ')
print(s1)

# r' = r^(-1) (mod p-1)
print('r^(-1): ')
print(r1)

# h = g^a (mod p) - отсюда выяисляем a
a = shenks(h, g, p)
print('a: ')
print(a)

S = []
# Разбиваем наше сообщение по буквам и шифруем s2 = (M-a*s1)*r' (mod p-1)
for i in range(0, len(M_new), 2):
    s2 = (int(M_new[i: i+2]) - a * s1) * r1 % (p-1)
    S.append(s2)

# Выведем полученные s_2:
print('s_2: ')
print(S)

# S = (s1, s2)

# Боб проверяет справедливость сравнения g^M = h^(s_1)*s_1^(s_2) (mod p)
for i in range(0, len(M_new), 2):
    print('Left part: ')
    print(binpow(g, int(M_new[i: i+2]), p))
    s2 = S[i // 2]
    print('Right part: ')
    print(binpow(h, s1, p) * binpow(s1, s2, p) % p)
