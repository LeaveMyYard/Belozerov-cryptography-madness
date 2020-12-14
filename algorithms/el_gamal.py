try:
    from BSGS import bsgs
except ImportError:
    from .BSGS import bsgs


def factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            yield i


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


if __name__ == "__main__":
    # C = 410960335176763805691582014331691624720259031884070026273723273921265044572181276217539160822986
    # p = 62508997
    # g = 2
    # h = 18537252
    # block_length = 8

    C = "073747 127613 201338 222776 758335 502424 595730 925985 939171 182708 742271"
    p = 994991
    g = 7
    h = 659454
    a = 475

    # c1, *c2 = [
    #     int(str(C)[i - block_length : i])
    #     for i in range(block_length, len(str(C)) + 1, block_length)
    # ]

    c1, *c2 = [int(c) for c in C.split()]

    print(c1)

    M = [(m * pow(c1, -a, p)) % p for m in c2]

    text = "".join(str(m).rjust(6, "0") for m in M)

    print("".join(alphabet[int(M[i : i + 2])] for i in range(0, len(text) - 2, 2)))
