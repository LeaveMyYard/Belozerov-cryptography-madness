# Методичка стр 43


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print('Please, input n:')
n = int(input())
# Выбираем произвольное B, если будет недостаточно для того
# чтобы (p-1) являлся показательно В-гладким
B = 5
A = 2
GCD = 1
while GCD == 1 or GCD == n:
    # A = 2^(B!)(mod n)
    for j in range(2, B):
        A = pow(A, j) % n
    GCD = gcd(A - 1, n)
    # если GCD - не делитель n (не считая 1 и n), то будем повторять процедуру
    B += 1
print(A)
print(B)
print(GCD)
print(n / GCD)
