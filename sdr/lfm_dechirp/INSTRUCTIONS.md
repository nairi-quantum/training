# Exercise — LFM chirp & dechirp  (SDR testbed pod)

**Covers:** Topic 2 (Modulation / I/Q), Topic 5 (Detection & estimation)
**You'll learn:** the FMCW/LFM chirp and the dechirp trick that turns a target's delay into a tone —
the exact signal chain behind Martin's radar/masking work.

## Theory (short)
- An **LFM (linear-FM) chirp** sweeps frequency linearly: `s(t) = exp( jπ · (B/T) · t² )`,
  where `B` = sweep bandwidth, `T` = sweep time, and `slope = B/T`.
- An **echo** from a target at delay `τ` is the same chirp shifted in time: `s(t − τ)`.
- **Dechirp:** multiply the echo by the *conjugate* of the transmitted chirp. The result is a **pure tone**
  whose frequency is the **beat frequency** `f_b = slope · τ = (B/T)·τ`.
- Take the **FFT** of the dechirped signal; the peak sits at `f_b`. (In real radar, `f_b` maps to range.)

## Your task
Open `lfm_dechirp.py` and complete the three `TODO`s in `estimate_beat_freq(...)`:
1. dechirp (echo × conjugate of the transmit chirp),
2. FFT + frequency axis,
3. return `|frequency|` at the FFT peak.

## Check yourself
```bash
python check_dechirp.py
```
It sets known delays, so the expected beat frequency is `(B/T)·τ`, and checks your estimate to within a
couple of FFT bins. Aim for **PASS ✅**.
