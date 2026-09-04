# Exercise — BB84 sifting & QBER  (Theory / Quantum pod)

**Covers:** the bridge from Topic 7 into real quantum — the first quantum protocol you'll simulate.
**You'll learn:** how BB84 keeps only "matched-basis" bits (sifting), and how errors show up as QBER.

## Theory (short)
In **BB84**, Alice sends each bit in a **randomly chosen basis** (Z or X). Bob measures in his **own random basis**.
- When their bases **match**, Bob gets Alice's bit (unless the channel introduced an error).
- When their bases **differ**, Bob's result is random and useless — so it's discarded.
- Keeping only the matched-basis positions is called **sifting**; on average **half** the bits survive.
- The **QBER** (quantum bit-error rate) is the fraction of *sifted* bits where Bob disagrees with Alice.
  With a channel error probability `p`, the QBER should come out ≈ `p`. (If QBER climbs above ~11%, no secure key — see the `qkd_keyrate` exercise.)

## Your task
The simulation of Alice, Bob, and the channel is provided. Open `bb84_sifting.py` and complete:
1. `sift_fraction` — the fraction of positions where the bases match.
2. `qber` — among the **sifted** positions, the fraction where Bob's bit ≠ Alice's bit.

## Check yourself
```bash
python check_bb84.py
```
It checks that ~50% of bits are sifted, that QBER ≈ 0 with a clean channel, and QBER ≈ `p` with errors. Aim for **PASS**.
