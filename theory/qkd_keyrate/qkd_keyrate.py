# -*- coding: utf-8 -*-
"""Exercise: binary entropy and the BB84 secure-key rate. Complete the TODOs."""
import math


def H2(p):
    """Binary entropy in bits: -p*log2(p) - (1-p)*log2(1-p). Return 0.0 for p <= 0 or p >= 1."""
    # TODO: handle the edge cases (p <= 0 or p >= 1 -> return 0.0),
    #       otherwise return -p*log2(p) - (1-p)*log2(1-p)   (use math.log2)
    return None


def secure_key_rate(qber):
    """BB84 asymptotic secure-key fraction: max(0, 1 - 2*H2(qber))."""
    # TODO: use H2 above; floor the result at 0.0
    return None


if __name__ == "__main__":
    print("H2(0.5) =", H2(0.5))
    print("secure_key_rate(0.02) =", secure_key_rate(0.02))
    print("secure_key_rate(0.12) =", secure_key_rate(0.12))
