a = 29
g = 5
p = 103
# k = 12
k = 1
m = 12
# k*m > p

A = []
B = []
# Создаем ряды чисел
while k != 12:
    A.append(a*g**(k-1) % p)
    B.append(g**(k*m) % p)
    k = k + 1
#print(A, B)

# Ищем однаковые числа в рядах
for i in A:
    if i in B:
        #print(A.index(i), B.index(i) + 1)
        break
    
# Проверяем равенство
y = (B.index(i) + 1) * m - A.index(i)
print(y)


