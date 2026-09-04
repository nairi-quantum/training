# -*- coding: utf-8 -*-
"""Exercise: a 3x repetition code over a binary symmetric channel. Complete the TODOs."""
import numpy as np


def repetition_ber(p_flip, n_rep=3, n_bits=200_000, seed=0):
    """Encode each bit n_rep times, send over a BSC (flip prob p_flip), majority-decode,
    and return the decoded bit-error rate."""
    rng = np.random.default_rng(seed)
    bits = rng.integers(0, 2, n_bits)

    # TODO 1 — encode: repeat each bit n_rep times.  hint: np.repeat(bits, n_rep)
    coded = None
    if coded is None:
        return None

    # BSC channel (given): flip each coded bit with probability p_flip
    flips = (rng.random(coded.size) < p_flip).astype(int)
    received = coded ^ flips

    # TODO 2 — majority-vote decode:
    #   reshape 'received' to (n_bits, n_rep), take the mean along axis=1,
    #   decide 1 where mean > 0.5, else 0.
    decoded = None
    if decoded is None:
        return None

    # TODO 3 — return the decoded BER (fraction of decoded bits that differ from 'bits')
    return None


if __name__ == "__main__":
    for p in [0.1, 0.2]:
        print(f"p={p}: raw={p}, decoded(3x)={repetition_ber(p)}")
