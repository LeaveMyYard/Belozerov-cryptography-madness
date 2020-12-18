import collections
import random
import copy

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


def analyze_change(change: dict[str, str]) -> dict[tuple[str, str], int]:
    return {
        (i, j): (alphabet.index(i) - alphabet.index(j) + len(alphabet)) % len(alphabet)
        for i, j in change.items()
    }


def analyze_repeats(text, length=1) -> dict[str, int]:
    letters = collections.defaultdict(lambda: 0)
    text_size = len(text)

    for i in range(length):
        for substr in zip(*[text[j + i :: length] for j in range(length)]):
            letters["".join(substr)] += 1

    return dict(letters)


def decrypt(text: str, mapping: dict[str, str]) -> str:
    return "".join(mapping[letter] if letter in mapping else " " for letter in text)


text = (
    open("letter_counting/bulgakov.txt", encoding="utf-8")
    .read()
    .replace("\n", " ")
    .replace(" ", "_")
    .upper()
)
res = analyze_repeats(text, 1)
stats = sorted(
    filter(lambda x: all(y in alphabet for y in x[0]), res.items()),
    key=lambda x: x[1],
    reverse=True,
)
stats = {stat[0]: i for i, stat in enumerate(stats)}


def calc_index(text) -> int:
    data = analyze_repeats(text, 1)
    rp = [x for x, _ in sorted(data.items(), reverse=True, key=lambda x: x[1])]
    return sum(
        ((i - stats[letter]) ** 2) if letter in stats else 10000
        for i, letter in enumerate(rp)
    )


# fmt: off
square = [ 
    "ABCDE",
    "FGHIK",
    "LMNOP",
    "QRSTU",
    "VWXYZ"
]
# fmt: on


def encrypt(text: str) -> str:
    return "".join(
        [
            f"{i + 1}{line.index(letter) + 1}"
            for i, line in enumerate(square)
            if letter in line
        ][0]
        for letter in text.replace("J", "I")
    )


def decrypt(encrypted_text: str) -> str:
    return "".join(
        square[int(i) - 1][int(j) - 1]
        for i, j in zip(encrypted_text[::2], encrypted_text[1::2])
    )


if __name__ == "__main__":
    text = open("input/map_input.txt", encoding="utf-8").read().replace("\n", "")
    text = [i + j for i, j in zip(text[::2], text[1::2])]
    print(text)
    res = analyze_repeats(text, 1)

    stats = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
    print(stats)

    # res = analyze_repeats(text, 2)
    # print(sorted(res.items(), key=lambda x: x[1], reverse=True))

    # most_repeated_letters = "_ОЕАИН"

    # for i in range(300):
    #     index = calc_index(decrypt(text, change))
    #     new_change = change
    #     while (new_index := calc_index(decrypt(text, new_change))) >= index:
    #         new_change = change.copy()
    #         rand_letter1, rand_letter2 = alphabet[random.randint(0, len(alphabet)-1)], alphabet[random.randint(0, len(alphabet)-1)]
    #         new_change[rand_letter1], new_change[rand_letter2] = new_change[rand_letter2], new_change[rand_letter1]

    #     change = new_change
    #     index = new_index
    #     print(i, index)
    #     print(change)
    #     print(decrypt(text, change))
    #     print(text)

    # print(analyze_change(change))
    # print(change)
    # print()
    # print(decrypt(text, change).replace("_", "*").replace(" ", "_").replace("*", " "))
    # print(text)
