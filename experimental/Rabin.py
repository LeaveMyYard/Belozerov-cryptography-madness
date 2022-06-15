# Методичка стр 57
import random


def sqrt(p, q, a):
    n = p * q
    # Если a - квадратичный вычет, то проделываем следующие действия, если нет, то нет
    if binpow(a, int((p - 1) / 2), p) == 1:
        # Если p=4m+3, то  по критерию Эйлера x^(2m+1)=1(mod p)
        if p % 4 == 3:
            m = (p - 3) // 4
            # и поэтому, домножая обе части полученного сравнения на х,
            # получаем y = +- x^(m+1) (mod p)
            up1 = binpow(a, m + 1, p)
            up2 = -binpow(a, m + 1, p) % p
            print('1')
        # Если p=8m+5, то  по критерию Эйлера x^(4m+2)=1(mod p)
        elif p % 8 == 5:
            # откуда, извлекая корень квадратный из обеих частей сравнения, имеем
            # x^(2m+1)=+-1(mod p)
            m = (p - 5) // 8
            # учитывая, что в этом случае
            # 2^(4m+2)=-1(mod p)
            # получаем y=+-x^(m+1)*2^(2m+1)(mod p)
            # для x^(2m+1)=-1 (mod p)
            if pow(a, 2 * m + 1, p) == p - 1:
                up1 = (pow(a, m + 1, p) * pow(2, 2 * m + 1, p)) % p
                up2 = (-pow(a, m + 1, p) * pow(2, 2 * m + 1, p)) % p
                print('2.1')
            # Иначе y = +-x^(m+1)(mod p)
            else:
                up1 = pow(a, m + 1, p)
                up2 = (-pow(a, int(m) + 1, p)) % p
                print('2.2')
        # Если p=8m+1...
        elif p % 8 == 1:
            # Пусть p=2^k*t+1, где (t, 2)=1, k>=3
            k = 3
            t = (p - 1) // pow(2, k)
            print('k: , t: ')
            # Будем подбирать соответсвтующие k и t
            while (p - 1) % pow(2, k) != 0 or t % 2 != 1:
                k += 1
                t = (p - 1) // pow(2, k)
            print(k, t)
            # Из критерия Эйлера получаем, что
            # x^(2^(k-1)*t)=1(mod p), откуда имеем x^(2^(k-2)*t)=+-1(mod p)
            # Выберем квадратичный невычет z(mod p)
            z = random.randrange(1, p - 1)
            while pow(z, int((p - 1) / 2), p) == 1:
                z = random.randrange(1, p - 1)
            # Тогда z^(2^(k-1)*t)=-1(mod p)
            print('z: ')
            print(z)
            # Отсюда, для любого целого s_1, равного 0 или t, получаем
            # x^(2^(k-2)*t)*z^(s_1*2^(k-1))=1(mod p), x^(2^(k-3)*t)*z^(s_1*2^(k-2))=+-1(mod p)
            s = 0
            k -= 1
            # Из последнего равенства аналогичным образом для некоторого целого
            # неотрицательного s_2 получаем
            # x^(2^(k-3)*t)*z^(s_2*2^(k-2))=1(mod p), x^(2^(k-4)*t)*z^(s_2*2^(k-3))=+-1(mod p)
            while k != 0:
                if (binpow(a, pow(2, k - 1) * t, p) * binpow(z, s, p)) % p != 1:
                    s += (p - 1) // 2
                s //= 2
                k -= 1
            # Повторяя эту процедуру еще k-3 раз, получим для некоторого неотрицательного s_(k-1) равенство
            # x^t*z^(2*s_(k-1))=1(mod p)
            print('s_(k-1): ')
            print(s)
            # y = +- x^((t+1)/2)*z^s_(k-1)(mod p)
            up1 = (binpow(a, (t + 1) // 2, p) * binpow(z, s, p)) % p
            up2 = (-binpow(a, (t + 1) // 2, p) * binpow(z, s, p)) % p
            print('3')
    else:
        print('No solution')

    if binpow(a, int((q - 1) / 2), q) == 1:
        if q % 4 == 3:
            m = (q - 3) // 4
            uq1 = binpow(a, m + 1, q)
            uq2 = -binpow(a, m + 1, q) % q
            print('1')
        elif q % 8 == 5:
            m = (q - 5) // 8
            if binpow(a, 2 * m + 1, q) == q - 1:
                uq1 = (binpow(a, m + 1, q) * binpow(2, 2 * m + 1, q)) % q
                uq2 = (-binpow(a, m + 1, q) * binpow(2, 2 * m + 1, q)) % q
                print('2.1')
            else:
                uq1 = binpow(a, m + 1, q)
                uq2 = (-binpow(a, int(m) + 1, q)) % q
                print('2.2')
        elif q % 8 == 1:
            k = 3
            t = (q - 1) // pow(2, k)
            print(k, t)
            while (q - 1) % pow(2, k) != 0 or t % 2 != 1:
                k += 1
                t = (q - 1) // pow(2, k)
                print(k, t)
            z = random.randrange(1, q - 1)
            while pow(z, int((q - 1) / 2), q) == 1:
                z = random.randrange(1, q - 1)
            print('z: ')
            print(z)
            s = 0
            k -= 1
            while k != 0:
                if (binpow(a, pow(2, k - 1) * t, q) * binpow(z, s, q)) % q != 1:
                    s += (q - 1) // 2
                s //= 2
                k -= 1
            print('s_(k-1): ')
            print(s)
            uq1 = (binpow(a, (t + 1) // 2, q) * binpow(z, s, q)) % q
            uq2 = (-binpow(a, (t + 1) // 2, q) * binpow(z, s, q)) % q
            print('3')
    else:
        print('No solution')

    print(up1, up2, uq1, uq2)

    y1 = 0
    inv_p, _, _ = gcd_extended(n / p, p)
    inv_q, _, _ = gcd_extended(n / q, q)
    y1 += up1 * n / p * inv_p
    y1 += uq1 * n / q * inv_q

    y2 = 0
    y2 += up2 * n / p * inv_p
    y2 += uq1 * n / q * inv_q

    y3 = 0
    y3 += up1 * n / p * inv_p
    y3 += uq2 * n / q * inv_q

    y4 = 0
    y4 += up2 * n / p * inv_p
    y4 += uq2 * n / q * inv_q

    return int(y1 % n), int(y2 % n), int(y3 % n), int(y4 % n)


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


C = input('Please, input a cipher: ')
n = int(input('Please, input n: '))
p, q = pollard(n)
print(p, q)
l = len(str(n))
answers = ''
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', ',', '.']
for i in range(len(C) // l):
    y1, y2, y3, y4 = sqrt(p, q, int(C[i * l: i * l + l]))
    y1 = '0' * (l - len(str(y1))) + str(y1)
    y2 = '0' * (l - len(str(y2))) + str(y2)
    y3 = '0' * (l - len(str(y3))) + str(y3)
    y4 = '0' * (l - len(str(y4))) + str(y4)
    y = [y1, y2, y3, y4]
    print(y)
    for j in range(0, l, 2):
        print(y1, y2, y3, y4)
        if y1 in y:
            if int(y1[j: j+2]) >= len(alphabet):
                y.remove(y1)
        if y2 in y:
            if int(y2[j: j+2]) >= len(alphabet):
                y.remove(y2)
        if y3 in y:
            if int(y3[j: j+2]) >= len(alphabet):
                y.remove(y3)
        if y4 in y:
            if int(y4[j: j+2]) >= len(alphabet):
                y.remove(y4)
    for j in range(0, l, 2):
        answers += alphabet[int(y[0][j:j + 2])]

    print(answers)
