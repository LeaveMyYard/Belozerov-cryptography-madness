import typing
import random
from math import floor, sqrt


def bsgs(x, g, p):
    """
    Solve for y in x = g^y mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    """

    m = floor(sqrt(p)) + 1  # phi(p) is p-1 if p is prime
    tbl = {pow(g, i, p): i for i in range(m)}

    c = pow(g, m * (p - 2), p)

    for j in range(m):
        y = (x * pow(c, j, p)) % p
        if y in tbl:
            # print(y, m, tbl[y], j)
            return j * m + tbl[y]

    return None


def sign(m: int, p: int, g: int, a: int) -> int:
    try:
        r = random.randint(1, p - 1)
        s1 = pow(g, r, p)
        rp = pow(r, -1, p - 1)
        s2 = ((m - a * s1) * rp) % (p - 1)
        return (s1, s2)
    except ValueError:
        return sign(m, p, g, a)


def check(m, s1, s2, p, g, h) -> bool:
    return pow(g, m, p) == (pow(h, s1, p) * pow(s1, s2, p)) % p


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,."


if __name__ == "__main__":
    p = 89981741
    g = 2
    h = 76976449
    a = bsgs(h, g, p)

    m = 121312

    s1, s2 = sign(m, p, g, a)
    print(s1, s2)

    print(check(m, s1, s2, p, g, h))
