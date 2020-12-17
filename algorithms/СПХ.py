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

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def Evk(a,b):               #расширенный алгоритм Евклида
    xa, ya = 1, 0
    xb, yb = 0, 1
    while b != 0:
        t = a
        T = (xa, ya)
        a = b
        xa, ya = xb, yb
        q = t // b
        b = t - q * b
        xb = T[0] - q * xb
        yb = T[1] - q * yb
    return xa

print("Поиск решения уравнения a^x = b (mod p)")


while True:
    print('Введите простое число p')
    p = int(input())
    if IsPrime(p):
        break

_factorization = Factor(p - 1)
qi = {i:_factorization.count(i) for i in set(_factorization)} # qi - словарь, ключ - множитель в разложении,
# значение - степень.

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())

b0 = b

r = dict() #создаем словарь для ri, там будет хитрость
tup = [] #создаем список, который потом будет переделан под кортеж и передан в значение словаря

    
for key in qi:
    for j in range(key):
        tup.append(a ** (j * (p - 1) // key) % p)  #складываем в словарь значения для a в разных степенях
    r[key] = tuple(tup)
    print(r[key])
    tup.clear()

#теперь r - таблица значений для поиска a
#состав r: ключ - qi, значение - кортеж ai в степени, j - индекс элемента в кортеже

x = [] #на сумму xi

chineese_theorem = dict() #словарик для финального хранения qi - ключ, N = x (mod qi)

#x0 находим вне цикла каким-то образом


#теперь одна из самых громоздких функций в коде

for q in r:
    # print("q is ", q)
    b_i = b ** ((p - 1) // q) % p #нашли первую b_i для x0
    # print(b_i)
    x.append(r[q].index(b_i))
    degree = 0                            #нахождение массива x1...xi
    
    for j in range(qi[q] - 1):
        degree += x[j] * q ** j
        b_i = (b // a ** degree) ** ((p - 1) // q ** (j + 2)) % p
        # print("here b_i is ", b_i)
        x.append(r[q].index(b_i))  # нахождение x[j+1]
    xx = 0
    # print("len is ", len(x))
    for i in range(len(x)):
        xx += x[i] * q ** i
    # print("xx is ", xx)

    #не так всё просто, в модуле нужно учитывать степень, поэтому
    deg = qi[q]
    chineese_theorem[q ** deg] = xx

    x = [] #очищаем массив


#и, наконец, реализация китайской теоремы об остатках через алгоритм Гаусса
M = 1
x = 0
for q in chineese_theorem:
    M*=q

for mi in chineese_theorem:
    b = M/mi
    c = chineese_theorem[mi]
    xi = Evk(b,mi)
    x += xi*c*b

x = int(x % M)

print(a, "^", x, " = ", b0 , "mod(", p, ")")