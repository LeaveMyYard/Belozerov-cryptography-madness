# Методичка стр 14
import pandas as pd
C = input('Please, input cipher: ')
C = [int(C[i]+C[i+1]) for i in range(0, len(C)-1, 2)]
print(C)

# Находим для каждого символа его встречаемость в нашем тексте
print(pd.value_counts(C))
sorted =list(pd.value_counts(C).to_dict().keys())

freq = ['_', 'О', 'Т', 'Ж', 'М', 'Я', 'К', 'В', 'И', 'Н', 'К', '.', 'А',
        'С',  'Е',  'П', 'Ы', 'Ь', 'З', 'Б', ',', 'Г', 'Ч', 'Й', 'Х', 'Л',
        'Ю', 'Ш', 'Ц', 'Ш', 'Э', 'Ф', '?', 'Ъ', 'Д']

# Подставляем вместо букв в шифре буквы, которые идут в списке частот под тем же номером
for i in range(len(C)):
    print(freq[sorted.index(C[i])])


