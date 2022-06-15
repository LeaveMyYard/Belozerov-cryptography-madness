# Методичка стр 87


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

na = int(input('Please, input na: '))
nb = int(input('Please, input nb: '))
ea = int(input('Please, input ea: '))
eb = int(input('Please, input eb: '))

# Для начала разложим число na на произведение простых чисел pa и qa
n_copy = na
factors = []
d = 2
while d ** 2 <= n_copy:
    while n_copy % d == 0:
        factors.append(d)
        n_copy /= d
    d += 1
if n_copy > 1:
    factors.append(int(n_copy))
pa, qa = factors

print('pa:')
print(pa)
print('qa:')
print(qa)

# Вычислим значение функции Эйлера
phia = (pa - 1) * (qa - 1)
print('phia(n):')
print(phia)

# Используя расширенный алгоритм Евклида, находим обратный элемент к ea по модулю phia
da, _, _ = gcd_extended(ea, phia)
da = da % phia
print('da:')
print(da)

print('Length of na: ')
la = len(str(na))
print(la)

# Найдем D_A (x)
DA = ''
# Разобьем наш текст на блоки по той же длине, что и длина n
for i in range(len(M_new) // la):
    block = int(M_new[i * la: i * la + la])
    # Каждый блок этого текста возводим в степень d по модулю n
    new = str(binpow(block, da, na))
    # Если длина получившегося нового блока меньше длины начального, слева добавляем нули
    new = '0' * (la - len(new)) + new
    print(new)
    DA += new

print('D_A: ')
print(DA)

# Для начала разложим число na на произведение простых чисел pa и qa
n_copy = nb
factors = []
d = 2
while d ** 2 <= n_copy:
    while n_copy % d == 0:
        factors.append(d)
        n_copy /= d
    d += 1
if n_copy > 1:
    factors.append(int(n_copy))
pb, qb = factors

print('pb:')
print(pb)
print('qb:')
print(qb)

# Вычислим значение функции Эйлера
phib = (pb - 1) * (qb - 1)
print('phib(n):')
print(phib)

# Используя расширенный алгоритм Евклида, находим обратный элемент к eb по модулю phib
db, _, _ = gcd_extended(eb, phib)
db = db % phia
print('db:')
print(db)

print('Length of nb: ')
lb = len(str(nb))
print(lb)

# Найдем E_Б(D_A (x))
EB = ''
# Разобьем наш текст на блоки по той же длине, что и длина n
for i in range(len(DA) // lb):
    block = int(DA[i * lb: i * lb + lb])
    # Каждый блок этого текста возводим в степень d по модулю n
    new = str(binpow(block, eb, nb))
    # Если длина получившегося нового блока меньше длины начального, слева добавляем нули
    new = '0' * (lb - len(new)) + new
    EB += new

print('E_B: ')
print(EB)

# Найдем D_Б(E_Б(D_A (x)))
DB = ''
# Разобьем наш текст на блоки по той же длине, что и длина n
for i in range(len(EB) // lb):
    block = int(EB[i * lb: i * lb + lb])
    # Каждый блок этого текста возводим в степень d по модулю n
    new = str(binpow(block, db, nb))
    # Если длина получившегося нового блока меньше длины начального, слева добавляем нули
    new = '0' * (lb - len(new)) + new
    DB += new

print('D_B: ')
print(DB)

# Найдем E_A(D_Б(E_Б(D_A (x))))
EA = ''
# Разобьем наш текст на блоки по той же длине, что и длина n
for i in range(len(DB) // la):
    block = int(DB[i * la: i * la + la])
    # Каждый блок этого текста возводим в степень d по модулю n
    new = str(binpow(block, ea, na))
    # Если длина получившегося нового блока меньше длины начального, слева добавляем нули
    new = '0' * (la - len(new)) + new
    EA += new

print('E_A: ')
print(EA)

