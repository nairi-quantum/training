#!/usr/bin/env python3
"""Digital Modulation & I/Q -- Demo 3: pulse shaping (RRC), eye diagram, spectrum.
Shows why we shape pulses: bandwidth control + open eye (low inter-symbol interference).
Pure NumPy. Saves pulse_shaping_eye.png.
"""
import sys, os
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(3)

def rrc(beta, sps, span):
    """Root-raised-cosine taps. span = length in symbols, sps = samples/symbol."""
    N = span*sps; t = (np.arange(-N/2, N/2+1))/sps
    h = np.zeros_like(t)
    for i,ti in enumerate(t):
        if abs(ti) < 1e-8:
            h[i] = 1 - beta + 4*beta/np.pi
        elif beta>0 and abs(abs(ti)-1/(4*beta))<1e-6:
            h[i] = (beta/np.sqrt(2))*((1+2/np.pi)*np.sin(np.pi/(4*beta))+(1-2/np.pi)*np.cos(np.pi/(4*beta)))
        else:
            num = np.sin(np.pi*ti*(1-beta)) + 4*beta*ti*np.cos(np.pi*ti*(1+beta))
            den = np.pi*ti*(1-(4*beta*ti)**2)
            h[i] = num/den
    return h/np.sqrt(np.sum(h**2))

sps=8; span=8; nsym=400
bits = rng.integers(0,2,nsym); sym = 2*bits-1.0     # BPSK for a clear eye
up = np.zeros(nsym*sps); up[::sps]=sym

fig, ax = plt.subplots(2, 2, figsize=(11, 8))

# (0,0) shaped waveform (roll-off 0.35)
h35 = rrc(0.35, sps, span); wav = np.convolve(up, h35, "same")
ax[0,0].plot(wav[:40*sps]); ax[0,0].set_title("RRC-shaped BPSK waveform (beta=0.35)")
ax[0,0].set_xlabel("sample"); ax[0,0].grid(True, alpha=0.3)

# (0,1) eye diagram
seg=2*sps; nseg=(len(wav)-span*sps)//seg
eye=wav[span*sps:span*sps+nseg*seg].reshape(nseg,seg)
for row in eye[:200]: ax[0,1].plot(row, color="C0", alpha=0.15)
ax[0,1].set_title("Eye diagram (open eye = low ISI)"); ax[0,1].set_xlabel("sample within 2 symbols"); ax[0,1].grid(True,alpha=0.3)

# (1,0) spectra for two roll-offs
for beta,c in [(0.2,"C1"),(0.5,"C2")]:
    w=np.convolve(up, rrc(beta,sps,span), "same")
    f=np.fft.fftshift(np.fft.fftfreq(len(w)))
    P=20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(w)))+1e-9)
    ax[1,0].plot(f, P-P.max(), color=c, label=f"beta={beta}")
ax[1,0].set_xlim(-0.25,0.25); ax[1,0].set_ylim(-60,5)
ax[1,0].set_title("Spectrum vs roll-off (smaller beta = narrower band)")
ax[1,0].set_xlabel("normalized freq"); ax[1,0].set_ylabel("dB"); ax[1,0].legend(); ax[1,0].grid(True,alpha=0.3)

# (1,1) unshaped (rectangular) eye for contrast
rect=np.repeat(sym, sps)
seg=2*sps; nseg=len(rect)//seg
eye2=rect[:nseg*seg].reshape(nseg,seg)
for row in eye2[:200]: ax[1,1].plot(row, color="C3", alpha=0.15)
ax[1,1].set_title("Rectangular pulses (wideband; abrupt transitions)")
ax[1,1].set_xlabel("sample within 2 symbols"); ax[1,1].grid(True,alpha=0.3)

fig.suptitle("Pulse shaping: RRC controls bandwidth and keeps the eye open", fontsize=13)
fig.tight_layout()
out=os.path.join(HERE,"pulse_shaping_eye.png"); fig.savefig(out,dpi=110)
print("saved", os.path.basename(out))
print("Takeaway: RRC shaping narrows the spectrum (bandwidth ~ (1+beta)/2/Tsym) and keeps a wide-open eye.")
