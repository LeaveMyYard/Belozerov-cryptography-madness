import typing
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


def factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            yield i


alphabet = "A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z".split("|")
print(len(alphabet))


if __name__ == "__main__":
    C = "15*27558200262300592658"
    # print(C)
    p = 89
    g = 3
    h = 66
    block_length = 2
    # print(list(factors(len(C))))
    a = bsgs(h, g, p)
    # print("a =", a)

    c1 = int(C.split("*")[0])
    c2_text = C.split("*")[1]

    c2 = [
        int(c2_text[i - block_length : i])
        for i in range(block_length, len(c2_text) + 1, block_length)
    ]

    # c1, *c2 = [int(c) for c in C.split()]

    # print("C_1 =", c1)
    # print("C_2 =", c2)

    M = [(m * pow(c1, -1 * a, p)) % p for m in c2]

    text = "".join(str(m).rjust(block_length, "0") for m in M)

    # print(M)
    # print("text =", text)
    # print("length(text) =", len(text))

    s = ""
    for i in range(0, len(text), 2):
        s += alphabet[int(text[i : i + 2]) % len(alphabet)]

    print(s)