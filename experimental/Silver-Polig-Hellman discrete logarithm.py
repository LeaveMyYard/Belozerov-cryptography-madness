# Методичка стр 49, алгоритмические задачи стр 2
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


print('Please, input a, g, p:')
a = int(input())
g = int(input())
p = int(input())

# Каноническое разложение числа p-1
factors = []
d = 2
p_1 = p - 1
while d ** 2 <= p_1:
    while p_1 % d == 0:
        factors.append(d)
        p_1 /= d
    d += 1
if p_1 > 1:
    factors.append(int(p_1))
print('Множители числа p-1: ')
print(factors)

# Отделяем сами множители и количество встреченных их раз
factors = np.array(factors)
(factors, counts) = np.unique(factors, return_counts=True)
print('Сколько раз встречались множители: ')
print(counts)

# Множители возводим в ту степень, в которой они были в p-1
d = dict.fromkeys(pow(factors, counts))
print('Множители, возведенные в свои степени: ')
print(d)

for i in range(len(factors)):
    y_k_g_k = 0
    for k in range(counts[i]):
        inv, _, _ = gcd_extended(pow(g, y_k_g_k), p)
        a_q_pow = pow(a * inv, int((p - 1) / pow(factors[i], k+1)), p)
        print('left: : ')
        print(a_q_pow)
        for j in range(factors[i]):
            print('g^(p-1)/q')
            print(pow(pow(g, int((p - 1) / factors[i]), p), j, p))
            if pow(pow(g, int((p - 1) / factors[i]), p), j, p) == a_q_pow:
                y_k_g_k += j * pow(int(factors[i]), k)
                print(y_k_g_k)
                if k == counts[i] - 1:
                    d[pow(factors[i], counts[i])] = y_k_g_k

print(d)

# По китайском теореме об остатках
y = 0
for key in d.keys():
    inv, _, _ = gcd_extended((p - 1)/key, key)
    y += (d[key] * (p - 1) / key * inv)

print(y % (p-1))
