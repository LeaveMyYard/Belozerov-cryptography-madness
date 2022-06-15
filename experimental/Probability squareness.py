# Методичка стр 60
import numpy as np


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


def pollard(n):
    # Выбираем произвольное B, если будет недостаточно для того
    # чтобы (p-1) являлся показательно В-гладким
    B = 5
    A = 2
    GCD = 1
    while GCD == 1 or GCD == n:
        # A = 2^(B!)(mod n)
        for j in range(2, B):
            A = binpow(A, j, n)
        _, _, GCD = gcd_extended(A - 1, n)
        # если GCD - не делитель n (не считая 1 и n), то будем повторять процедуру
        B += 1
        A = 2
    return GCD, int(n / GCD)


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


print('Please, input a cipher: ')
# Считываем шифр по столбикам, первое число - количество столбцов, первое - строк
C = np.zeros((5, 6))
for i in range(6):
    integer_map = map(int, input().split())
    integer_list = list(integer_map)
    C[:, i] = integer_list

print(C)
C = C.flatten()
n = int(input('Please, input n: '))
# Находим разложение n на множители
p, q = pollard(n)

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
            'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы',
            'Ь', 'Э', 'Ю', 'Я', '_']

# block_size = int(input('Please, input block sizes: '))

answer = ''
for block in C:
    if binpow(int(block), int((p - 1) / 2), p) == 1 and binpow(int(block), int((q - 1) / 2), q) == 1:
        answer += '0'
    else:
        answer += '1'
print('Answer in binary: ')
print(answer)

final = ''
for i in range(len(answer)//6):
    final += alphabet[int(answer[i * 6: i * 6 + 6], 2)]

print(final)
