import typing

Point = typing.Union[tuple[int, int], typing.Literal[0]]
Curve = tuple[int, int]


def add(P: Point, Q: Point, curve: Curve) -> Point:
    if P == 0:
        return Q
    if Q == 0:
        return P

    xp, yp = P
    xq, yq = Q
    a, b = curve

    try:
        if P != Q:
            s = (yp - yq) * pow(xp - xq, -1)
            xr = s ** 2 - xp - xq
            yr = -yp + s * (xp - xr)
        else:
            s = (3 * xp ** 2 + a) * pow(2 * yp, -1)
            xr = s ** 2 - 2 * xp
            yr = -yp + s * (xp - xr)
        return (xr, yr)
    except ValueError:
        return 0


def inv(P: Point, curve: Curve) -> Point:
    if P == 0:
        return 0

    x, y = P
    return (x, -y)


def mult(n: int, P: Point, curve: Curve) -> Point:
    x, y = P
    a, b = curve

    if n == 0:
        return 0
    if n < 0:
        return inv(mult(abs(n), P, curve), curve)

    R = P
    for i in range(1, n):
        R = add(R, P, curve)

    return R


if __name__ == "__main__":
    curve = (-7, 10)
    P = (1, 2)
    R = mult(-123, P, curve)
    print(R)
