import collections


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


def factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            yield i


alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


def analyze_repeats(text, length=1) -> dict[str, int]:
    letters = collections.defaultdict(lambda: 0)
    text_size = len(text)

    for i in range(length):
        for substr in zip(*[text[j + i :: length] for j in range(length)]):
            letters["".join(substr)] += 1

    return dict(letters)


def encrypt(text: str, key: str) -> str:
    return "".join(
        alphabet[
            (alphabet.index(letter) + alphabet.index(key[i % len(key)])) % len(alphabet)
        ]
        for i, letter in enumerate(text)
    )


def decrypt(text: str, key: str) -> str:
    return "".join(
        alphabet[
            (alphabet.index(letter) - alphabet.index(key[i % len(key)])) % len(alphabet)
        ]
        for i, letter in enumerate(text)
    )


def transform(text: str, length: int) -> list[str]:
    return [text[i::length] for i in range(length)]


def analyze(text: str) -> tuple[dict[str, list[int]], list[tuple[int, int]]]:
    res = {}
    # analyze only 2 appeared tetragrams, 2 trigrams and 4 bigrams
    repeats_treshold = {2: 2, 3: 2, 4: 2}
    for substr_size in [2, 3, 4]:
        data = analyze_repeats(text, length=substr_size)
        data = dict(
            filter(lambda x: x[1] >= repeats_treshold[substr_size], data.items())
        )
        data = {substr: list(find_all(text, substr)) for substr in data}
        data = {
            substr: [positions[i] - positions[i - 1] for i in range(1, len(positions))]
            for substr, positions in data.items()
        }
        res |= data

    length_counter = collections.defaultdict(lambda: 0)

    for vals in res.values():
        for dist in vals:
            # length_counter[dist] += 1
            for factor in factors(dist):
                length_counter[factor] += 1

    return res, sorted(length_counter.items(), reverse=True, key=lambda x: x[1])


def get_key_letter(input_letter: str, output_letter: str) -> str:
    """
    if you have an input_letter, that appears in a C subtext and after analysis you
    think, that is could be an output_letter, then the result of the function will be
    the letter, that should be in a key for this to be true
    """
    return alphabet[
        (alphabet.index(input_letter) - alphabet.index(output_letter)) % len(alphabet)
    ]


if __name__ == "__main__":
    # M = "CHAUCER MET A YOUNG LADY AT COURT NAMED PHILIPPA"
    # key = "SHERIDAN"
    # M = M.replace(" ", "")
    # C = encrypt(M, key)
    # print("M =", M)
    # print("key =", key)
    # print("C = E(M) =", C)
    # print("Transform of cyphered:", transform(M, len(key)))
    # print("M = D(C) =", decrypt(C, key))
    C = open("input/vigener_input.txt", encoding="utf-8").read().replace(" ", "")
    # substrings, repeat_factors = analyze(C)
    # # print(substrings)
    # print(repeat_factors)

    assert all(
        letter in alphabet for letter in C
    ), f"No letters in alphabet: {set(letter for letter in C if letter not in alphabet)}"

    transformed_texts = transform(C, 6)
    # print(transformed_texts)
    analyses = [analyze_repeats(subtext) for subtext in transformed_texts]
    most_repeats_in_subtexts = [
        sorted(analysis.items(), reverse=True, key=lambda x: x[1])[:6]
        for analysis in analyses
    ]
    print(*most_repeats_in_subtexts, sep="\n")

    # This step is empiric, do by hands using most_repeats_in_subtexts
    # Example for as in a book
    # # most_repeated_letters are _ОЕА
    # output_as_most_repeated = "_О_О_"
    # input_as_most_repeated = ",ЬИ,М"

    # most_repeated_letters are _ОЕА
    output_as_most_repeated = "__Е___"
    input_as_most_repeated = "РНРМХД"

    generated_key = "".join(
        get_key_letter(inp, out)
        for inp, out in zip(input_as_most_repeated, output_as_most_repeated)
    )
    print(generated_key)
    print(decrypt(C, generated_key))
