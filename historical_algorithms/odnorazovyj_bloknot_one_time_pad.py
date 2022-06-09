# Encryption
# Finding a key to make message c from message m

alphabet="A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|_".split("|")

m="TOP_SECRET"

c="BEST_HORSE"

def str_encode(s):
    num=""
    for let in s:
        code=str(alphabet.index(let)+1)
        num += code if len(code)>1 else "0"+code
    return int(num)

def str_decode(s):
    s= str(s) if len(str(s))%2==0 else "0"+str(s)
    mes=""
    for i in range(0,len(s),2):
        mes+=alphabet[int(s[i]+s[i+1])-1]
        # print(int(s[i]+s[i+1]))
    return mes

m_e=str_encode(m)
c_e=str_encode(c)

print("Message: ",m_e)

key= m_e^c_e

print("Key: ",key)

print("Check: ")
print()

print("m_e^key=",c_e,"=",str_decode(m_e^key))

print(m_e,c_e^key)
print(m_e==c_e^key)
print()
print(m,str_decode(c_e^key))

# key=19298228641876882617