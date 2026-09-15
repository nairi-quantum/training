#!/usr/bin/env python3
"""Digital Modulation & I/Q -- Demo 2: BER vs Eb/N0 for BPSK, QPSK, 16-QAM.
Extends Nathalie's BPSK BER to more modulations; measured (Monte Carlo) vs theory.
Pure NumPy. Saves ber_vs_snr.png and prints a table.
"""
import sys, os
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
from math import erfc, sqrt, log2
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)
Q = lambda x: 0.5*erfc(x/sqrt(2))
ebn0_db = np.arange(0, 13)
Nbits = 400_000

def gray4(bits2):  # 2 Gray bits -> 4-PAM level {-3,-1,1,3}
    d = {(0,0):-3,(0,1):-1,(1,1):1,(1,0):3}
    return np.array([d[(a,b)] for a,b in bits2])
def degray4(levels):
    d = {-3:(0,0),-1:(0,1),1:(1,1),3:(1,0)}
    return np.array([d[l] for l in levels]).reshape(-1)

def sim_bpsk(ebn0):
    b = rng.integers(0,2,Nbits); s = 2*b-1.0
    sig = sqrt(1/(2*ebn0))
    r = s + sig*rng.standard_normal(Nbits)
    return np.mean((r>0).astype(int) != b)

def sim_qpsk(ebn0):
    b = rng.integers(0,2,Nbits); bi,bq = b[0::2], b[1::2]
    s = (2*bi-1) + 1j*(2*bq-1); s /= sqrt(2)          # unit energy
    sig = sqrt(1/(2*ebn0*2))
    r = s + sig*(rng.standard_normal(len(s))+1j*rng.standard_normal(len(s)))
    bihat=(r.real>0).astype(int); bqhat=(r.imag>0).astype(int)
    err = np.count_nonzero(bihat!=bi)+np.count_nonzero(bqhat!=bq)
    return err/(2*len(s))

def sim_16qam(ebn0):
    n = (Nbits//4)*4; b = rng.integers(0,2,n).reshape(-1,4)
    I = gray4(list(zip(b[:,0],b[:,1]))); Qd = gray4(list(zip(b[:,2],b[:,3])))
    s = (I + 1j*Qd)/sqrt(10)                          # unit energy
    sig = sqrt(1/(2*ebn0*4))
    r = s + sig*(rng.standard_normal(len(s))+1j*rng.standard_normal(len(s)))
    lv=np.array([-3,-1,1,3])
    Ih = lv[np.argmin(np.abs(r.real[:,None]*sqrt(10)-lv[None,:]),axis=1)]
    Qh = lv[np.argmin(np.abs(r.imag[:,None]*sqrt(10)-lv[None,:]),axis=1)]
    bhat = np.stack([degray4(Ih).reshape(-1,2), degray4(Qh).reshape(-1,2)],axis=1).reshape(len(s),4)
    return np.mean(bhat != b)

curves = {
 "BPSK":  (sim_bpsk,  lambda e: 0.5*erfc(sqrt(e))),
 "QPSK":  (sim_qpsk,  lambda e: 0.5*erfc(sqrt(e))),
 "16-QAM":(sim_16qam, lambda e: 0.375*erfc(sqrt(0.4*e))),   # Gray approx
}
plt.figure(figsize=(8,6))
print(" Eb/N0 |   BPSK    QPSK    16-QAM   (measured)")
sim_store={}
for name,(fn,_) in curves.items():
    sim_store[name]=[fn(10**(s/10)) for s in ebn0_db]
for i,s in enumerate(ebn0_db):
    print(f"  {s:3d}  | {sim_store['BPSK'][i]:.2e} {sim_store['QPSK'][i]:.2e} {sim_store['16-QAM'][i]:.2e}")
for j,(name,(_,th)) in enumerate(curves.items()):
    meas=np.maximum(sim_store[name],1e-6)
    plt.semilogy(ebn0_db, meas, "o", color=f"C{j}", label=f"{name} (sim)")
    plt.semilogy(ebn0_db, np.maximum([th(10**(s/10)) for s in ebn0_db],1e-12), "--", color=f"C{j}", label=f"{name} (theory)")
plt.xlabel("Eb/N0 (dB)"); plt.ylabel("BER"); plt.grid(True, which="both", alpha=0.4)
plt.title("BER vs Eb/N0 -- BPSK / QPSK / 16-QAM"); plt.legend(); plt.ylim(1e-6,1)
out=os.path.join(HERE,"ber_vs_snr.png"); plt.tight_layout(); plt.savefig(out,dpi=120)
print("saved", os.path.basename(out))
print("Takeaway: BPSK and QPSK overlap; 16-QAM needs ~4 dB more for the same BER -> the rate/robustness trade-off.")
