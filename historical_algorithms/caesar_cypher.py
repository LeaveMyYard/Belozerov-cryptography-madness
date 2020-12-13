alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
shift = 3


def encrypt(text: str) -> str:
    return "".join(
        alphabet[(alphabet.index(letter) + shift) % len(alphabet)] for letter in text
    )


def decrypt(text: str) -> str:
    return "".join(
        alphabet[(alphabet.index(letter) + len(alphabet) - shift) % len(alphabet)]
        for letter in text
    )


if __name__ == "__main__":
    # M = "CAESAR"
    # C = encrypt(M)
    # print("M =", M)
    # print("C = E(M) =", C)
    # print("M = D(C) =", decrypt(C))

    text = open("input/map_input.txt", encoding="utf-8").read().replace("\n", "")
    for shift in range(1, len(alphabet)):
        print(decrypt(text))
