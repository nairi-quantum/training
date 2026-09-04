# -*- coding: utf-8 -*-
"""Exercise: BB84 sifting and QBER. Complete the TODOs."""
import numpy as np


def bb84(n=200_000, p_error=0.0, seed=0):
    """Simulate BB84 over n qubits with channel error probability p_error.
    Return (sift_fraction, qber)."""
    rng = np.random.default_rng(seed)
    a_bits = rng.integers(0, 2, n)      # Alice's random bits
    a_bases = rng.integers(0, 2, n)     # Alice's bases  (0 = Z, 1 = X)
    b_bases = rng.integers(0, 2, n)     # Bob's bases

    match = (a_bases == b_bases)        # where the two bases agree

    # Bob's measured bit (given):
    #   matched basis -> Alice's bit, flipped with probability p_error
    #   mismatched basis -> a random bit
    noise = rng.random(n) < p_error
    b_bits = np.where(match, np.where(noise, 1 - a_bits, a_bits), rng.integers(0, 2, n))

    # TODO 1 — sift_fraction: fraction of positions where the bases match
    sift_fraction = None

    # TODO 2 — qber: among the MATCHED positions only, the fraction where b_bits != a_bits
    #   hint: compare a_bits[match] with b_bits[match]
    qber = None

    return sift_fraction, qber


if __name__ == "__main__":
    print("clean channel :", bb84(200_000, 0.00, seed=1))
    print("5% errors     :", bb84(200_000, 0.05, seed=2))
