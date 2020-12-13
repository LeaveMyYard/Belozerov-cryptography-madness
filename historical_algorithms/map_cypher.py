import collections


def analyze_repeats(text, length=1) -> dict[str, int]:
    letters = collections.defaultdict(lambda: 0)
    text_size = len(text)

    for i in range(length):
        for substr in zip(*[text[j + i :: length] for j in range(length)]):
            letters["".join(substr)] += 1

    return dict(letters)
