import collections

text = open("letter_counting/text.txt", encoding="utf-8").read().replace("\n", " ")
letters = collections.defaultdict(lambda: 0)
text_size = len(text)

for letter in text:
    letters[letter] += 1

for letter, count in sorted(letters.items(), key=lambda item: item[1], reverse=True):
    print(letter, "-", count, f"({round(100 * count / text_size, 2)}%)")
