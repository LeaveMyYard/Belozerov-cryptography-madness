# Методичка стр 53


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


n = int(input('Please, input n (open key): '))

# Для начала разложим число n на произведение простых чисел p и q при помощи (p-1)-метода Полларда
p, q = pollard(n)
print('p:')
print(p)
print('q:')
print(q)

# Вычислим значение функции Эйлера
phi = (p - 1) * (q - 1)
print('phi(n):')
print(phi)

# Используя расширенный алгоритм Евклида, находим обратный элемент к e по модулю phi
e = int(input('Please, input e: '))
d, _, _ = gcd_extended(e, phi)
d = d % phi
print('d:')
print(d)

M = input('Please, input a message: ')

print('Length of n: ')
l = len(str(n))
print(l)

a = input('Please, input, if alphabet is english (e) or russian (r): ')
answers = {}
# Разобьем наш текст на блоки по той же длине, что и длина n
for i in range(len(M) // l):
    block = int(M[i * l: i * l + l])
    # Каждый блок этого текста возводим в степень d по модулю n
    new = str(binpow(block, d, n))
    # Если длина получившегося нового блока меньше длины начального, слева добавляем нули
    new = '0' * (l - len(new)) + new
    # print(new)
    for k in range(l, 1, -2):
        # Поскольку начальный текст может быть разбит на меньшие блоки, чем длина n, будем пробовать
        # различные блоки длины от 2 до длины n включительно
        for j in range(0, k, 2):
            # Переводим числа в буквы
            if a == 'e':
                if k not in answers:
                    answers[k] = chr(65+int(new[j: j+2]))
                else:
                    answers[k] += chr(65 + int(new[j: j + 2]))
            if a == 'r':
                if k not in answers:
                    answers[k] = chr(1040+int(new[j: j+2]))
                else:
                    answers[k] += chr(1040 + int(new[j: j + 2]))
        new = new[2:]

print(answers)
