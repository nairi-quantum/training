# -*- coding: utf-8 -*-
"""Exercise: simulate the BER of BPSK over an AWGN channel. Complete the TODOs."""
import numpy as np


def simulate_ber(EbN0_dB, n_bits=500_000, seed=0):
    """Return the simulated bit-error rate of BPSK over AWGN at the given Eb/N0 (in dB)."""
    rng = np.random.default_rng(seed)
    bits = rng.integers(0, 2, n_bits)

    # TODO 1 — BPSK modulate: map bit 0 -> -1.0 and bit 1 -> +1.0
    #   hint: symbols = 2*bits - 1  (as floats)
    symbols = None

    # TODO 2 — noise:
    #   EbN0_lin = 10 ** (EbN0_dB / 10)
    #   sigma    = sqrt( 1 / (2 * EbN0_lin) )
    EbN0_lin = None
    sigma = None

    if symbols is None or sigma is None:
        return None  # remove once TODO 1 & 2 are done

    r = symbols + rng.normal(0.0, sigma, n_bits)

    # TODO 3 — detect: bits_hat = 1 where r > 0, else 0
    bits_hat = None

    # TODO 4 — BER = fraction of positions where bits_hat != bits
    ber = None

    return ber


if __name__ == "__main__":
    for db in [0, 2, 4, 6]:
        print(f"Eb/N0 = {db} dB  ->  BER = {simulate_ber(db)}")
