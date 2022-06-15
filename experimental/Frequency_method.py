# Методичка стр 14
import pandas as pd
C = input('Please, input cipher: ')
C = list(C)

# Находим для каждого символа его встречаемость в нашем тексте
print(pd.value_counts(C))
sorted =list(pd.value_counts(C).to_dict().keys())

freq = ['_', 'O', 'Е', 'А', 'И', 'Т', 'Н', 'С', 'Р', 'В', 'Л', 'К', 'М',
        'Д', 'П', 'У', 'Я', 'Ы', 'Ь', 'З', 'Б', 'Г', 'Ч', 'Й', 'Х', 'Ж',
        'Ю', 'Ш', 'Ц', 'Ш', 'Э', 'Ф', 'Ъ']

# Подставляем вместо букв в шифре буквы, которые идут в списке частот под тем же номером
for i in range(len(C)):
    print(freq[sorted.index(C[i])])


