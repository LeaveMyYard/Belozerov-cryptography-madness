import typing


def bsgs(x, g, p):
    """
    Solve for y in x = g^y mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    """
    from math import ceil, sqrt

    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime
    tbl = {pow(g, i, p): i for i in range(N)}
    c = pow(g, N * (p - 2), p)
    for j in range(N):
        y = (x * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    return None


def factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            yield i


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


if __name__ == "__main__":
    C = "5148154611033774886049492438294008383372872853501067660147906401592062201450665781876473"
    p = 89981741
    g = 2
    h = 76976449
    block_length = len(str(p))
    a = bsgs(h, g, p)
    print("a =", a)

    # C = "073747 127613 201338 222776 758335 502424 595730 925985 939171 182708 742271"
    # p = 994991
    # g = 7
    # h = 659454
    # a = 475

    c1, *c2 = [
        int(str(C)[i - block_length : i])
        for i in range(block_length, len(str(C)) + 1, block_length)
    ]

    # c1, *c2 = [int(c) for c in C.split()]

    print("C_1 =", c1)
    print("C_2 =", c2)

    M = [(m * pow(c1, -1 * a, p)) % p for m in c2]

    text = "".join(str(m).rjust(8, "0") for m in M)

    # print(M)
    print("text =", text)
    print("lenght(text) =", len(text))

    s = ""
    for i in range(0, len(text) - 6, 2):
        s += alphabet[int(text[i : i + 2])]

    print(s)
