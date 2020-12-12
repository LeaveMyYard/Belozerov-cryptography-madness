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
    M = "POLIBIY"
    C = encrypt(M)
    D = decrypt(C)
    print("M =", M)
    print("C = E(M) =", C)
    print("D = D(C) =", D)
