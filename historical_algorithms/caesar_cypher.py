alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
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
    M = "CAESAR"
    C = encrypt(M)
    print("M =", M)
    print("C = E(M) =", C)
    print("M = D(C) =", decrypt(C))

