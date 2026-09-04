# Exercise — QKD secure-key-rate & entropy  (Theory/Quantum pod)

**Covers:** Topic 7 (Information theory & physical-layer security) — and the bridge to QKD security.
**You'll learn:** binary entropy, and the famous BB84 secure-key formula and its ~11% QBER threshold.

## Theory (short)
- **Binary entropy** (in bits): `H2(p) = −p·log2(p) − (1−p)·log2(1−p)`, with `H2(0) = H2(1) = 0`.
  It peaks at `H2(0.5) = 1` bit.
- For BB84 QKD, the **asymptotic secure-key fraction** (per sifted bit) is
  `r = 1 − 2·H2(QBER)`, floored at 0 (you can't get a negative key rate).
- Set `r = 0` → `H2(QBER) = 0.5` → the well-known **QBER threshold ≈ 0.11 (11%)**: above it, no secure key.

## Your task
Open `qkd_keyrate.py` and complete:
1. `H2(p)` — binary entropy (return 0.0 for `p ≤ 0` or `p ≥ 1`).
2. `secure_key_rate(qber)` — `max(0, 1 − 2·H2(qber))`.

## Check yourself
```bash
python check_keyrate.py
```
It verifies `H2(0.5)=1`, `H2(0)=0`, that the key rate is positive at low QBER and zero by 12%, and that the
threshold lands near **0.11**. Aim for **PASS ✅**.
