
def count_frequency(my_list, alphabet):   
    freq = {} 
    for item in alphabet: 
        freq[item] = my_list.count(item)
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))        
    i = 1
    for key, value in sorted_freq.items(): 
        print (str(i) + ' ' + key + ' : ' + str(value))
        i+=1

def replace(ciphertext, alphabet, repl_shm, hide_undefined=False):
    alphabet_array = alphabet.split('|')
    repl_shm_array = repl_shm.split('|')
    decrypted = ''
    for char in ciphertext:
        new_char = repl_shm_array[alphabet_array.index(char)]
        if new_char == ' ':
            if hide_undefined:
                new_char = '#'
            else:
                new_char = char
        decrypted += new_char
    return decrypted



ciphertext = 'БЯРЛХМИЯТЙАГМЮБХЕХТ_МУЪЯМГЬЯРЯМДТЯМЯЬМЬЙМЯДЙЬ_МНЦЙЬМХМШЙЪЬЙЙМРАНУМТЯМПХЛГАГМЙРЯМГМРЯШЯЪГАГМДТЯМНМЬЙРЯМЛЯОЪЯЙМЮЙЪЛЖЙ'
rus_freq_1 = '_ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙХЖШЮЦЩЭФЪ'
rus_freq_2 = '_ОАЕИНТРСЛВКПМУДЯЫЬЗБГЙЧЮХЖШЦЩФЭЪ'
alphabet = 'А|Б|В|Г|Д|Е|Ж|З|И|Й|К|Л|М|Н|О|П|Р|С|Т|У|Ф|Х|Ц|Ч|Ш|Щ|Ъ|Ы|Ь|Э|Ю|Я|_'
repl_shm = ' | |-| | | | |-| | |-|Н|О| | | | |-| | |-| | |-| |-| |-| |-| |_| '

ciphertext_array = [char for char in ciphertext]
count_frequency(ciphertext, alphabet.split('|'))

print('Encrypted message: \n')
print(ciphertext)
print('\n')
print('Decrypted message: \n')
print(replace(ciphertext, alphabet, repl_shm))
print('\n')
print(replace(ciphertext, alphabet, repl_shm, True))


