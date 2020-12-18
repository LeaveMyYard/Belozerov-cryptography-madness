def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


def primitive_root(p: int) -> int:
    factors = set(Factor(p - 1))
    print(Factor(p - 1))

    for g in range(1, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g

    return None


if __name__ == "__main__":
    print(primitive_root(919))