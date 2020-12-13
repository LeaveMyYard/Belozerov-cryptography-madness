import collections

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


if __name__ == "__main__":
    text = open("input/map_input.txt", encoding="utf-8").read().replace("\n", "")
    res = analyze_repeats(text, 1)
    print(sorted(res.items(), key=lambda x: x[1], reverse=True))

    # res = analyze_repeats(text, 2)
    # print(sorted(res.items(), key=lambda x: x[1], reverse=True))

    # most_repeated_letters = "_ОЕАИН"

    change = {
        "Е": "_",
        "К": "О",
        "Б": "Е",
        "Ю": "А",
    }

    print(analyze_change(change))

    print(decrypt(text, change))
