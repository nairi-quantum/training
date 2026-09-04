# Exercise — BER of BPSK over AWGN  (Simulations pod)

**Covers:** Topic 3 (Noise, SNR & BER), Topic 2 (Modulation)
**You'll learn:** how a digital link is simulated, and how we *measure* it with BER.

## Theory (short)
- **BPSK** sends one bit per symbol: bit `0 → −1`, bit `1 → +1`.
- The **AWGN channel** adds Gaussian noise: `r = s + n`, with `n ~ N(0, σ²)`.
- For unit-energy BPSK, if `Eb/N0` (linear) `= 10^(Eb/N0[dB]/10)`, the noise standard deviation is
  `σ = sqrt( 1 / (2 · Eb/N0_linear) )`.
- **Detection:** decide `1` if `r > 0`, else `0`.
- **BER** = fraction of received bits that differ from the sent bits.
- The theoretical BPSK curve (what your simulation should match) is `BER = 0.5·erfc( sqrt(Eb/N0_linear) )`.

## Your task
Open `ber_bpsk.py` and complete the four `TODO`s in `simulate_ber(...)`:
1. modulate the bits to ±1,
2. compute `σ` and add noise,
3. detect the bits,
4. return the BER.

## Check yourself
```bash
python check_ber.py
```
The checker runs your `simulate_ber` at several Eb/N0 values and compares to the theoretical curve.
You want **PASS ✅** — meaning your simulated BER matches theory within statistical tolerance.

## Going further (optional)
- Plot BER vs Eb/N0 (your points + the theory curve) with matplotlib.
- Extend to **QPSK** (2 bits/symbol) and compare.
