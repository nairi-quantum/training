#!/usr/bin/env python3
"""Digital Modulation & I/Q -- Demo 1: constellations under AWGN noise.
Shows BPSK / QPSK / 16-QAM ideal points and how noise scatters them as SNR changes.
Pure NumPy + Matplotlib (no hardware). Saves one PNG per modulation.
"""
import sys, os
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(1)

def unit_energy(c): return c/np.sqrt(np.mean(np.abs(c)**2))

# constellations (normalized to unit average symbol energy)
bpsk  = unit_energy(np.array([-1, 1], dtype=complex))
qpsk  = unit_energy(np.array([1+1j, 1-1j, -1+1j, -1-1j]))
lv    = np.array([-3,-1,1,3])
qam16 = unit_energy(np.array([i+1j*q for q in lv for i in lv]))

mods = {"BPSK": bpsk, "QPSK": qpsk, "16-QAM": qam16}
snrs = [0, 5, 10, 20]   # Es/N0 in dB
N = 2000

for name, C in mods.items():
    fig, ax = plt.subplots(2, 2, figsize=(9, 9))
    for a, snr in zip(ax.ravel(), snrs):
        sym = C[rng.integers(0, len(C), N)]
        sigma = np.sqrt(1/(2*10**(snr/10)))            # per real dim, Es=1
        rx = sym + sigma*(rng.standard_normal(N)+1j*rng.standard_normal(N))
        a.scatter(rx.real, rx.imag, s=4, alpha=0.35, color="C0")
        a.scatter(C.real, C.imag, s=90, color="red", marker="x", linewidths=2, label="ideal")
        a.set_title(f"{name}  |  Es/N0 = {snr} dB"); a.grid(True, alpha=0.3)
        a.set_xlabel("I"); a.set_ylabel("Q"); a.axis("equal"); a.legend(loc="upper right", fontsize=8)
    fig.suptitle(f"{name} constellation under AWGN  ({int(np.log2(len(C)))} bit/symbol)", fontsize=13)
    fig.tight_layout()
    out = os.path.join(HERE, f"constellation_{name.replace('-','').lower()}.png")
    fig.savefig(out, dpi=110); plt.close(fig)
    print("saved", os.path.basename(out))
print("Done. Higher SNR -> tighter clouds around the ideal points (this is Nathalie's SNR->BER, visualized).")
