#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Towel 2017

from math import ceil, sqrt


def bsgs(x, g, p):
    """
    Solve for y in x = g^y mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    """
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (x * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


print(bsgs(31, 5, 167))