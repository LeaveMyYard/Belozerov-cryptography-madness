# Методичка стр 18
import numpy as np
from sympy import Matrix


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
            'Ь', 'Э', 'Ю', 'Я', '_', ',', '.', '?', '!']
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']

# Каждая букву соответствует числу
listOfInt = [i for i in range(0, len(alphabet))]
zipbObj = zip(alphabet, listOfInt)
# Create a dictionary from zip object
dictOfWords = dict(zipbObj)

open_c = input('Please, input open cipher: ')
open_m = input('Please, input open message: ')
order = int(input('Please, input an order of affine cipher: '))

# Представим наши строки как набор символов, найдем числовое их соответствие и
# оставим необходимое нам количество
open_c = np.array(list(dictOfWords[i] for i in open_c[:(order+1)*order]))
open_m = np.array(list(dictOfWords[i] for i in open_m[:(order+1)*order]))
open_c_1 = open_c.copy()

# Делаем наш размер нашего шрифта и сообщения таким, чтоб количество строк = порядку шрифта
open_c = open_c.reshape((order+1, order)).T
open_m = open_m.reshape((order+1, order)).T
open_m_orig = open_m.copy()
open_c_orig = open_c.copy()
print(open_c)
print(open_m)

# Вычитая из равенства Y  = АХ_i  + S (для i = 1,2,...) равенство Y_n  = AX_n  + S, получаем систему
open_c = open_c[:, :order+1] - open_c[:, order].reshape((order, 1))
open_c = open_c[:, :order] % len(alphabet)
print(open_c)

open_m = open_m[:, :order+1] - open_m[:, order].reshape((order, 1))
open_m = open_m[:, :order] % len(alphabet)
print(open_m)

# Так как матрица А считается неизвестной, то это равенство можно рассматривать,
# как матричное уравнение относительно А.
# Если матрица в правой части обратима, то уравнение имеет единственное решение
# A = C*M^(-1)
A = np.dot(open_c, Matrix.inv_mod(Matrix(open_m), len(alphabet))) % len(alphabet)
print(A)
print('M:')
print((open_m[0][0] * open_m[1][1] - open_m[0][1] * open_m[1][0]) % len(alphabet))
print(open_m[1][1]% len(alphabet))
print(open_m[0][0] % len(alphabet))
print(-open_m[0][1] % len(alphabet))
print(-open_m[1][0]% len(alphabet))
print( Matrix.inv_mod(Matrix(open_m), len(alphabet)))

# S = C - A * M
S = open_c_orig[:, 0].reshape(order, 1) - np.dot(A, open_m_orig[:, 0].reshape(order, 1)) % len(alphabet)
print((np.dot(A,  open_m_orig[:, 0].reshape(order, 1)) + S) % len(alphabet))

# A_1 = A^(-1)
if order == 2:
    det_A = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % len(alphabet)
    print('determinant of A:')
    print(det_A)
    det_A_inv, _, _ = gcd_extended(det_A, len(alphabet))
    print('inverse determinant of A:')
    print(det_A_inv)
    inv_A = np.zeros((2, 2))
    inv_A[0][0] = (A[1][1] * det_A_inv) % len(alphabet)
    inv_A[1][1] = (A[0][0] * det_A_inv) % len(alphabet)
    inv_A[0][1] = (-A[0][1] * det_A_inv) % len(alphabet)
    inv_A[1][0] = (-A[1][0] * det_A_inv) % len(alphabet)
    print(inv_A)

A_1 = Matrix.inv_mod(Matrix(A), len(alphabet))

# S_1 = -A_1*S
S_1 = (-np.dot(A_1, S)) % len(alphabet)
print(A_1)
print(S_1)

c = list(input('Please, input cipher to decode: '))
c = np.array(list(dictOfWords[i] for i in c))
message = ''
for i in range(0, len(c)-order+1, order):
    m = ((np.dot(A_1, c[i:i+order].reshape(order, 1)) + S_1) % len(alphabet)).flatten()
    for j in range(order):
        message += alphabet[listOfInt.index(m[j])]
print(message)
