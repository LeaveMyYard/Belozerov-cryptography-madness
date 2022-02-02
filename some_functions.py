import numpy as np


def bin_pow(a: int, n: int, p: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 1:
        return (bin_pow(a, n - 1, p) * a) % p
    else:
        b1 = bin_pow(a, n // 2, p)
        return (b1 * b1) % p


def bin_powers_show(n: int) -> int:
    print("pow= ",n,end="; ")
    n2=int(np.log2(n))
    print("floor(log2(n))= floor(log2(",n,"))= ",n2,end="; \n")
    n_aprox=2**n2
    new_n=n-n_aprox
    if new_n==0:
        return 1
    else:
        return n_aprox*bin_powers_show(new_n)
# bin_pow(21394991,2**21,94847117)
# bin_powers_show(3562221)

def gcd_ext(a: int, p: int) -> (int, int, int):
    if a == 0:
        return p, 0, 1
    gcd, x1, y1 = gcd_ext(p % a, a)
    x = y1 - (p // a) * x1
    y = x1
    return gcd, x, y


def inverse_number(a: int, p: int) -> int:
    gcd, x, y = gcd_ext(a, p)
    if gcd == 1:
        return (x % p + p) % p
    else:
        return -1


def discrete_logs_shanks(h: int, g: int, p: int, show_calculations: bool = False) -> int:
    if show_calculations:
        print("\ndiscrete_logs_shanks, begin:")
        print("h=g^a (mod p)")
    k = int(np.ceil(np.sqrt(p)))
    m = int(np.ceil(np.sqrt(p)))
    if show_calculations:
        print("k= ", k)
        print("m= ", m)

    assert k*m>p, "k*m<=p"


    J = []
    I = {}

    for j in range(m):
        J.append((h * bin_pow(g, j, p)) % p)
    for i in range(1, k + 1):
        I |= {bin_pow(g, m * i, p): i}
    if show_calculations:
        print("h*g^j: ", J)
        print("g^im: ", I.keys())

    i_final = -1
    j_final = -1
    common_num = -1
    for j in range(m):
        if I.get(J[j]) != None:
            i_final = I.get(J[j])
            j_final = j
            common_num = J[j]

    if show_calculations:
        print("(calculations for j start from 0; for i- from 1)")
        print("j= ", j_final, "; i= ", i_final, "; common number= ", common_num)
    a = (i_final * m - j_final)%p
    if show_calculations:
        print("a= i*m-j= ", a)
    assert bin_pow(g, a, p) == h, "wrong answer"

    if show_calculations:
        print("discrete_logs_shanks, end;\n")
    return a

def factorial(a: int)->int:
    return int(np.prod(np.array([i for i in range(1,a+1)])))

def pollard_factorization(n:int, show:bool=False,b:int=1)->int:
    A=bin_pow(2,factorial(b),n)
    p = np.gcd(A - 1, n)
    if show:
        print("B= ",b,"; A= ",A,"; (A-1,n)= ",p)
    if p==1:
        return pollard_factorization(n,show,b+1)
    else:
        return p

print(pollard_factorization(3799,True))
# discrete_logs_shanks(18, 5, 97, True)
