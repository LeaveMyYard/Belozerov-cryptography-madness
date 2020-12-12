import collections

text = open("letter_counting/text.txt", encoding="utf-8").read().replace("\n", " ")
letters = collections.defaultdict(lambda: 0)
text_size = len(text)

for letter1, letter2 in zip(text[::2], text[1::2]):
    letters[letter1 + letter2] += 1

for letter1, letter2 in zip(text[1::2], text[2::2]):
    letters[letter1 + letter2] += 1

for letter, count in sorted(letters.items(), key=lambda item: item[1], reverse=True):
    print(letter, "-", count, f"({round(100 * count / text_size, 2)}%)")
