# Методичка стр 67
a = float(input('Please, input a: '))
b = float(input('Please, input b: '))
Px = float(input('Please, input x coordinate of P: '))
Py = float(input('Please, input y coordinate of P: '))

x = []
y = []

x.append(Px)
y.append(Py)

Px_new = ((3 * Px * Px + a) / 2 / Py)**2 - 2 * Px
x.append(Px_new)
Py_new = -Py+((3 * Px * Px + a) / 2 / Py)*(Px-Px_new)
y.append(Py_new)

# Будем прибавлять P, пока не будет такая сумма, что икс такой уже есть, причем с противополжным игреком
while -Py_new not in y or x[y.index(-Py_new)] != Px_new:
    Px = Px_new
    Py = Py_new
    Px_new = ((Py - y[0]) / (Px - x[0])) ** 2 - x[0] - Px
    x.append(Px_new)
    Py_new = -y[0] + (Py - y[0]) / (Px - x[0])*(x[0] - Px_new)
    y.append(Py_new)

print(x, y)
print(y.index(-Py_new) + len(y) + 1)
