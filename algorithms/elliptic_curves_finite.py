import typing

Point = typing.Union[tuple[int, int], typing.Literal[0]]
Curve = tuple[int, int, int]


def add(P: Point, Q: Point, curve: Curve) -> Point:
    if P == 0:
        return Q
    if Q == 0:
        return P

    xp, yp = P
    xq, yq = Q
    a, b, p = curve

    try:
        if P != Q:
            s = ((yp - yq + p) % p) * pow((xp - xq + p) % p, -1, p)
            xr = (s ** 2 - xp - xq) % p
            yr = (-yp + s * (xp - xr)) % p
        else:
            s = (3 * xp ** 2 + a) * pow(2 * yp, -1, p)
            xr = (s ** 2 - 2 * xp) % p
            yr = (-yp + s * (xp - xr)) % p
        return (xr, yr)
    except ValueError:
        return 0


def inv(P: Point, curve: Curve) -> Point:
    if P == 0:
        return 0

    x, y = P
    return (x, curve[2] - y)


def mult(n: int, P: Point, curve: Curve) -> Point:
    """Naive method"""

    x, y = P
    a, b, p = curve

    if n == 0:
        return 0
    if n < 0:
        return inv(mult(abs(n), P, curve), curve)

    R = P
    for i in range(1, n):
        R = add(R, P, curve)

    return R


def curve_order(curve: Curve) -> int:
    """Naive method"""

    points = set()
    a, b, p = curve
    for x in range(0, p):
        r = (x ** 3 + a * x + b) % p
        for y in range(0, p):
            if pow(y, 2, p) == r:
                points.add((x, y))

    return len(points)


def point_order(P: Point, curve: Curve) -> int:
    i = 2
    while True:
        if mult(i, P, curve) == 0:
            return i
        i += 1


if __name__ == "__main__":
    curve = (2, 3, 97)
    P = (3, 6)
    print(point_order(P, curve))

    # print("2 *", P, "=", P2)
    # print(add(p2, P, curve))
