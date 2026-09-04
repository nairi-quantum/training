# -*- coding: utf-8 -*-
"""Exercise: reliability of a QSDC session over a lossy classical channel. Complete the TODOs."""


def delivery_prob(p_loss, max_retries):
    """Probability ONE control message is delivered, given up to (max_retries + 1) attempts."""
    # TODO: a message fails only if ALL (max_retries + 1) attempts are lost.
    #       return 1 - p_loss ** (max_retries + 1)
    return None


def session_reliability(p_loss, n_msgs, max_retries):
    """Probability ALL n_msgs control messages in a session are delivered."""
    # TODO: every message must get through -> delivery_prob(...) ** n_msgs
    return None


if __name__ == "__main__":
    print("delivery_prob(0.1, 3)      =", delivery_prob(0.1, 3))
    print("session_reliability(0.1,4,3) =", session_reliability(0.1, 4, 3))
