# Exercise — Repetition code (error correction)  (Simulations / Theory pod)

**Covers:** Topic 6 (Channel coding & error correction)
**You'll learn:** the simplest forward-error-correction code, and see coding *lower* the error rate.

## Theory (short)
- A **repetition code** sends each bit `n_rep` times (e.g. `1 → 1 1 1`).
- The **binary symmetric channel (BSC)** flips each transmitted bit with probability `p`.
- The receiver **majority-votes** each group of `n_rep` bits back to one bit.
- For `n_rep = 3`, a decoded bit is wrong only if ≥2 of 3 copies flip:
  `P(error) = 3p²(1−p) + p³ = 3p² − 2p³`, which is **smaller than `p`** for small `p` — coding helps.

## Your task
Open `repetition_code.py` and complete the `TODO`s in `repetition_ber(...)`:
1. encode (repeat each bit `n_rep` times),
2. majority-vote decode,
3. return the decoded BER.
(The BSC channel is provided.)

## Check yourself
```bash
python check_repetition.py
```
It compares your decoded BER to `3p² − 2p³` (for `n_rep = 3`) and confirms it beats the raw channel error `p`. Aim for **PASS**.

## The quantum bridge
QKD/QSDC use **error reconciliation** to fix errors on the sifted key, and **quantum error-correcting codes**
protect qubits themselves — both are the quantum descendants of exactly this idea (and Michel's specialty).
