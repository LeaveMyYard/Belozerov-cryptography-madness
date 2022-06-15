# Методичка стр 47
n = int(input('Please, input n: '))
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

p, q = factors
print((p-1)*(q-1))
