# Методичка стр 67
a = float(input('Please, input a: '))
b = float(input('Please, input b: '))
Px = float(input('Please, input Px: '))
Py = float(input('Please, input Py: '))
Qx = float(input('Please, input Qx: '))
Qy = float(input('Please, input Qy: '))

# Используем формулу 11.2
if Px != Qx:
    Sx = ((Qy - Py) / (Qx - Px)) ** 2 - Px - Qx
    Sy = -Py + (Qy - Py) / (Qx - Px) * (Px - Sx)
    print(Sx, Sy)

# Используем формулу 11.3
elif Px == Qx and Py == Qy:
    Sx = ((3 * Px * Px + a) / 2 / Py) ** 2 - 2 * Px
    Sy = -Py+((3 * Px * Px + a) / 2 / Py)*(Px-Sx)
    print(Sx, Sy)

else:
    print('Нулевая точка')
