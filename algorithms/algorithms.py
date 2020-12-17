def mod(a, b):
    """
    Ввел для удобства использования
    в функции solve,
    так очевиднее, что куда передается нежели c %
    """
    return a % b


## ExtendedGCD
# *********************************************************
def ExtendedGCD(a, b):
    """
    Из книги Т. Корман <<Алгоритмы. Построение и Анализ>>
    стр 966
    """
    if b == 0:
        return a, 1, 0
    d1, x1, y1 = ExtendedGCD(b, mod(a, b))
    d, x, y = d1, y1, x1 - (a / b) * y1
    return d, x, y


## EulerPhi
# *********************************************************


def EulerPhi(input):
    """
    Функция Эйлера
    varphi(n), где n — натуральное число,
    равна количеству натуральных чисел,
    не больших n и взаимно простых с ним.
    """
    res = 1
    i = 2
    while i * i <= input:
        # пока i^2 <= input
        p = 1
        while input % i == 0:
            input /= i  # если не взаимно просты, делим
            p *= i  # произведение делителей i втч и кратных
        p /= i
        if p != 0:
            # если мы хоть раз делили на текущее i
            # то общее произведение делителей
            # умножаем на (i - 1)*i^(число раз - 1)
            res *= p * (i - 1)
        i += 1
    n = input - 1
    # input - уже изменен
    if n == 0:
        return res
    else:
        # умножаем на (input - 1)*input^(число раз - 1)
        # но число раз = 1
        return n * res


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