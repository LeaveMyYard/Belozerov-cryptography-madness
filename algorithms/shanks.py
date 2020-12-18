import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x")
parser.add_argument("g")
parser.add_argument("p")
args = parser.parse_args()
x = int(args.x)
g = int(args.g)
p = int(args.p)

m = k = math.ceil(math.sqrt(p))

print('')
first_row = []
for j in range(0, m):
    num = (g**j * x)%p
    print(num, end=' ')
    first_row.append(num)

print('')

result = ''
for i in range(1, k+1):
    num = (g ** (i*m))%p
    print(num, end=' ')
    if num in first_row:
        j = first_row.index(num)
        result = '\ni=%d, j=%d, y=%d'%(i, j, i*m-j)

print('\n' + result + '\n')

