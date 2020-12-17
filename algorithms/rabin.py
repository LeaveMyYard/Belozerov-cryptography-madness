from functools import reduce

# бинарный метод возведения в степень по модулю
def modexp(x, y, n):
    a = 1
    while y != 0:
        d = y % 2
        y = y // 2
        if d != 0:
            a = a * x % n
        x = x * x % n
    return a


# факторизация числа n перебором всех возможных делителей
def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


# символ Лежандра
def legendre(a, p):
    a %= p
    res = 0
    if a == 2:
        res = 1 if ((p * p - 1) / 8) % 2 == 0 else -1
    elif a == -1:
        res = 1 if ((p - 1) / 2) % 2 == 0 else -1
    elif a == 1:
        res = 1
    else:
        divisors = primfacs(a)
        if len(divisors) == 1:
            res = legendre(p % a, a)
            if (p - 1) * (a - 1) / 4 % 2 != 0:
                res = -res
        else:
            res = 1
            for div in divisors:
                res *= legendre(div, p)

    return res


# расширеный рекурсивный алгоритм Эвклида
# находит x,y: a*x+b*y=gcd(a,b)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# Китайская теорема об остатках. Алгоритм Гарнера
def chinese_remainder(a, n):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    # попарное совмещение a_i, n_i
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        # находим r_i, s_i: r_i*n_i+s_i*p=1
        # тогда x=sum(a_i*s_i*p)
        sum += a_i * egcd(p, n_i)[1] * p
    return sum % prod


# Квадратный корень по простому модулю("Handbook of Applied Cryptography"стр.100)
def square_root_mod(a, p):
    if legendre(a, p) == -1:
        return 0
    b = 2
    # Нахожу случайное b, такое что (b,p)=-1 (b - квадр невычет)
    while legendre(b, p) != -1:
        b += 1
    # Представляю p-1 в виде p-1=2s*t, где t - нечетное
    s = 0
    t = p - 1
    while t % 2 == 0:
        t //= 2
        s += 1
    # Вычисляю a^(-1)(mod p) - обратный элемент в кольце Zp
    g, x, y = egcd(a, p)
    if g == 1:
        inv = x % p
    c = modexp(b, t, p)
    r = modexp(a, int((t + 1) / 2), p)
    for i in range(1, s):
        d = modexp(r ** 2 * inv, 2 ** (s - i - 1), p)
        # if d=-1(mod p)
        if d + 1 == p:
            r = (r * c) % p
        c = (c * c) % p
    return r


# Нахождение корней по китайской теореме об остатках
def sqrt_mod(a, p, q):
    rp = square_root_mod(a, p)
    rq = square_root_mod(a, q)
    a1 = [rp, rq]
    a2 = [rp, -rq]
    a3 = [-rp, rq]
    a4 = [-rp, -rq]
    n = [p, q]
    return (
        chinese_remainder(a1, n),
        chinese_remainder(a2, n),
        chinese_remainder(a3, n),
        chinese_remainder(a4, n),
    )


# перевод полученных числовых значений блока в текст
def decryption(l, p, q, m):
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        " ",
        ",",
        ".",
    ]
    ans = ""
    for i in l:
        print(i)
        a = sqrt_mod(i, p, q)
        print(a)
        for j in a:
            txt = str(j)
            while len(txt) < m:
                txt = "0" + txt
            count = 0
            w = 0
            while w != m:
                if int(txt[w : w + 2]) <= len(alphabet):
                    count += 1
                w += 2
            if count == m / 2:
                v = 0
                z = ""
                while v != m:
                    z += alphabet[int(txt[v : v + 2])]
                    ans += alphabet[int(txt[v : v + 2])]
                    v += 2
                print(z)
    return ans


def Rabin(string, n, m):
    p = primfacs(n)[0]
    q = primfacs(n)[1]
    l = []
    i = 0
    while i != len(string):
        l.append(int(string[i : i + m]))
        i += m
    print("Секретный ключ: p=" + str(p) + ", q=" + str(q))
    return decryption(l, p, q, m)


# входные данные
c = "011055242294483160750316501598754251285614254510"
n = 71093863
m = len(str(n))

print(Rabin(c, n, m))

