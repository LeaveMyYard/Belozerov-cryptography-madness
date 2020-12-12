# fmt: off
square = [ 
    "KINGD VQEOK",
    "OMABC WRFMI",
    "EFHLP XSHAN",
    "QRSTU YTLBG",
    "VWXYZ ZUPCD",
    "",
    "ZYXWV DCPUZ",
    "UTSRQ GBLTY",
    "PLHFE NAHSX",
    "CBAMO IMFRW",
    "DGNIK KOEQV",
]
# fmt: on


def _encrypt_bigram(two_letters: str) -> str:
    a, b = two_letters[0], two_letters[1]
    ax, ay = [
        (line[:5].index(a), y) for y, line in enumerate(square[:5]) if a in line[:5]
    ][0]
    bx, by = [
        (line[6:].index(b), y) for y, line in enumerate(square[6:]) if b in line[6:]
    ][0]

    return square[ay][6 + bx] + square[6 + by][ax]


def _decrypt_bigram(two_letters: str) -> str:
    a, b = two_letters[0], two_letters[1]
    ax, ay = [
        (line[6:].index(a), y) for y, line in enumerate(square[:5]) if a in line[6:]
    ][0]
    bx, by = [
        (line[:5].index(b), y) for y, line in enumerate(square[6:]) if b in line[:5]
    ][0]

    return square[ay][bx] + square[6 + by][6 + ax]


def encrypt(text: str) -> str:
    return "".join(
        _encrypt_bigram(a + b)
        for (a, b) in zip(text.replace("J", "I")[::2], text.replace("J", "I")[1::2])
    )


def decrypt(text: str) -> str:
    return "".join(_decrypt_bigram(a + b) for (a, b) in zip(text[::2], text[1::2]))


if __name__ == "__main__":
    C = "MOPWTIOMFXNS"
    # C = encrypt(M)
    D = decrypt(C)
    # print("M =", M)
    print("C = E(M) =", C)
    print("D = D(C) =", D)
