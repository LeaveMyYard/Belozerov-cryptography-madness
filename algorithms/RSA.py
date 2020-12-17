# import numpy as np
import math

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
    # ",",
    # ".",
]


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    # print(g,x,_)
    if g == 1:
        return x % n


def RSA(s, n, e, kq=None):
    l = len(s)
    print("length of s = ", l)
    k = math.gcd(l, len(str(n)))
    if not kq:
        kq = len(str(n))

    print("k = ", k)
    C = []
    for i in range(len(s)):
        if i % k == 0:
            s3 = s[i : k + i]
            C.append(int(s3))
    print("C = ", C)
    n1 = primfacs(n)
    p = n1[0]
    q = n1[1]
    phi = (p - 1) * (q - 1)
    d = mulinv(e, phi)
    m = []
    for c in C:

        m.append(pow(c, int(d), n))
    print("m = ", m)
    M_tmp = ""
    for i in range(0, len(m)):

        m_s = str(m[i])
        while len(m_s) < kq:
            m_s = "0" + m_s

        M_tmp += m_s
    print(M_tmp)
    MM = ""
    for i in range(0, len(M_tmp), 2):
        m_i = int(M_tmp[i : i + 2])
        MM += alphabet[m_i % len(alphabet)]
    print(MM)

    # ans = ''.join(M)
    # print(ans)


RSA(
    "491794547096837824773497682113110037449993489740770973767593837824",
    974069,
    868121,
    4,
)
