#!/usr/bin/env python3
"""Digital Modulation & I/Q -- Demo 4: phase offset rotates the constellation.
Motivates carrier synchronization -- and mirrors the phase-reference a homodyne
(coherent / CV quantum) receiver needs. Pure NumPy. Saves phase_offset.png.
"""
import sys, os
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__)); rng=np.random.default_rng(5)
C = np.array([1+1j,1-1j,-1+1j,-1-1j])/np.sqrt(2)     # QPSK, unit energy
N=1500; snr=15
sym=C[rng.integers(0,4,N)]
sigma=np.sqrt(1/(2*10**(snr/10)))
rx=sym+sigma*(rng.standard_normal(N)+1j*rng.standard_normal(N))
theta=np.deg2rad(20); rx_rot=rx*np.exp(1j*theta)

fig,ax=plt.subplots(1,2,figsize=(11,5.2))
for a,data,title in [(ax[0],rx,"Aligned (phase locked)"),(ax[1],rx_rot,"20-degree phase offset (rotated)")]:
    a.scatter(data.real,data.imag,s=6,alpha=0.4,color="C0")
    a.scatter(C.real,C.imag,s=110,color="red",marker="x",linewidths=2,label="ideal QPSK")
    a.axhline(0,color="k",lw=0.6); a.axvline(0,color="k",lw=0.6)
    a.set_title(title); a.set_xlabel("I"); a.set_ylabel("Q"); a.axis("equal"); a.grid(True,alpha=0.3); a.legend(fontsize=8)
fig.suptitle("A phase error rotates the whole constellation -> wrong decisions until synchronized",fontsize=12)
fig.tight_layout(); out=os.path.join(HERE,"phase_offset.png"); fig.savefig(out,dpi=115)
print("saved", os.path.basename(out))
print("Quantum link: a homodyne/coherent (CV) receiver needs the same phase reference (a local oscillator) to read I/Q.")
