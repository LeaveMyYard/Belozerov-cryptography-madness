# something like inverse matrices is computed on other calculators and just put here
import numpy as np

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е',
            'Ж', 'З', 'И', 'Й', 'К', 'Л',
            'М', 'Н', 'О', 'П', 'Р', 'С',
            'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч',
            'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
            'Ю', 'Я', '_', ',', '.', '?', '!']


def f(a):
    return alphabet.index(a)


C = "Т.ИЗС!ЛХЫПЮ!.АИОЩЧЮ!НИ.ЕЧК"

strC = "ЧНВХ_ЬВТ"
strM = "РЕШЕНИЕ"

n = 2
p = len(alphabet)

X = []
Y = []

for i in range(n + 1):
    x1 = []
    y1 = []
    for j in range(n):
        x1.append(f(strM[i * n + j]))
        y1.append(f(strC[i * n + j]))
    X.append(x1)
    Y.append(y1)

X = np.array(X)
Y = np.array(Y)

print("X: ", X.T)
print("Y: ", Y.T)

XX = []
YY = []
print("\nSubstractive:")
for i in range(n):
    XX.append((X[i] - X[n]) % p)
    YY.append((Y[i] - Y[n]) % p)
print("X substractive: \n", np.array(XX).T)
print("Y substractive: \n", np.array(YY).T)

XX_1 = [[23, 35], [14, 14]]

# A=Y*np.linalg.inv(X) mod p
A = (np.matrix(YY).T @ np.matrix(XX_1)) % p
S = (Y[n] - A @ X[n]) % p
print("A: ", A)
print("S: ", S)

A_1 = [[22, 31], [21, 32]]
S_1 = ((-1) * (A_1 @ (np.matrix(S).T))) % p
print("A_1: ", A_1)
print("S_1: \n", S_1)

# check
ANS = []
for i in range(0, len(strC) // n):
    y_n = []
    for j in range(n):
        y_n.append(f(strC[i * n + j]))
    ANS.append((np.matrix(A_1) @ (np.matrix(y_n).T) + S_1) % p)
# print(ANS)

ans = ""
for block in ANS:
    for j in range(n):
        ans += alphabet[int(block[j])]
print(ans)
# %%
# dectryption
ANS = []
for i in range(0, len(C) // n):
    y_n = []
    for j in range(n):
        y_n.append(f(C[i * n + j]))
    ANS.append((np.matrix(A_1) @ (np.matrix(y_n).T) + S_1) % p)
# print(ANS)

ans = ""
for block in ANS:
    for j in range(n):
        ans += alphabet[int(block[j])]
print(ans)
