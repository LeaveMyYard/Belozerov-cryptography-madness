'''
Finding a by known p,g,h and decryption of a message
'''
# %%
import string
from functions import *

# %%


# cryptogram="583866418611596181691162272914107724980680454062385964463717412751167369249705160945729075223247"
# p = 90568823
# g = 5
# h = 47364654
# a= 32695141

num = ([str(i) for i in range(29)])
alphabet = {}

for i in range(29):
    if i < 10:
        num[i] = "0" + num[i]
        alphabet |= {num[i]: string.ascii_lowercase[i]}
    elif i == 26:
        alphabet |= {"26": " "}
    elif i == 27:
        alphabet |= {"27": ","}
    elif i == 28:
        alphabet |= {"28": "."}
    else:
        alphabet |= {num[i]: string.ascii_lowercase[i]}


def decrypt(a1, c1, c2):
    return (c2 * inverse_number(bin_pow(c1, a1, p), p)) % p


# %%

cryptogram = "21394991461339690975594635863701400976220441119109982714798967187475486758063636665365486138041248732144"
p = 94847117
g = 3
h = 56572874
#
# Solution
block_length = 8
letter_length = 2

# a = 3562221

#%%
# cryptogram = "227992085239888300224888"
# p = 97
# g = 5
# h = 83
# Solution

# block_length = 2
# letter_length = 2

# %%
a = discrete_logs_shanks(h, g, p, True)
M = []
ans = ""

# print(alphabet)
print("C1= ", cryptogram[0:block_length])
for i in range(block_length, len(cryptogram), block_length):
    n1=0
    n2=0
    if cryptogram[0:block_length].lstrip("0") == "":
        n1 = 0
    else:
        n1 = int(cryptogram[0:block_length].lstrip("0"))
    if cryptogram[i:i + block_length].lstrip("0")=="":
        n2=0
    else:
        n2=int(cryptogram[i:i + block_length].lstrip("0"))

    M.append(str(decrypt(a, n1, n2)))

    M[(i - block_length) // block_length] = M[(i - block_length) // block_length].zfill(block_length)

    print("C2= ", cryptogram[i:i + block_length], "; M= ", M[(i - block_length) // block_length], end=" ")

    print("\"",end="")
    for j in range(0, len(M[(i - block_length) // block_length]), letter_length):
        ans += alphabet[M[(i - block_length) // block_length][j:letter_length + j]]
        print(alphabet[M[(i - block_length) // block_length][j:letter_length + j]], end="")
    print("\"",end="")
    print()
print(ans)
# a forgetful head makes a weary pair of heels.
