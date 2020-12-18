from __future__ import annotations

import collections

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,?"


def analyze_repeats(text, length=1) -> collections.defaultdict[str, int]:
    letters = collections.defaultdict(lambda: 0)
    text_size = len(text)

    for i in range(length):
        for substr in zip(*[text[j + i :: length] for j in range(length)]):
            letters["".join(substr)] += 1

    return letters


if __name__ == "__main__":
    text = (
        open("letter_counting/bulgakov.txt", encoding="utf-8")
        .read()
        .replace("\n", " ")
        .replace(" ", "_")
        .upper()
    )
    res = analyze_repeats(text, 1)
    print(
        sorted(
            filter(lambda x: all(y in alphabet for y in x[0]), res.items()),
            key=lambda x: x[1],
            reverse=True,
        )
    )
