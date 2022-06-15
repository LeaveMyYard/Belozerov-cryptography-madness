# Методичка стр 62
import numpy as np

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', ',', '.']


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


h = int(input('Please, input h: '))
p = int(input('Please, input p: '))
g = int(input('Please, input g: '))
c = input('Please, input a cipher: ')
# h = g^a (mod p) - отсюда выяисляем a
a = shenks(h, g, p)
# c1 подбираем из начала сообщения, c1<p
c1 = int(c[:2])
counter = 2
answers = {}
while c1 < p:
    print(c1)
    # c1 = g^r - отсюда вычисляем r
    r = shenks(c1, g, p)
    # r не должен быть больше p-1
    if r > p - 1:
        counter += 2
        c1 = int(c[:counter])
    else:
        # c2 - следующие после c1 блоки той же длины
        for i in range(1, len(c) // counter):
            # D = c2 * (c1^a)^(-1)  (mod p)
            c2 = int(c[i * counter: i * counter + counter])
            print(c2)
            inv, _, _ = gcd_extended(binpow(c1, a, p), p)
            D = str((c2 * inv) % p)
            # дополняем нулями слева, если длина нового блока меньше длины первого блока
            if len(D) != counter:
                D = '0' * (counter - len(D)) + D
            # расшифровываем
            for k in range(0, counter-1, 2):
                if counter not in answers:
                    answers[counter] = alphabet[int(D[k:k+2]) % len(alphabet)]
                else:
                    answers[counter] += alphabet[int(D[k:k+2])% len(alphabet)]
        counter += 2
        c1 = int(c[:counter])
print(answers)

