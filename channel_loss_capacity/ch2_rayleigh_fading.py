# -*- coding: utf-8 -*-
"""Seminar: Channel -- fading (Rayleigh).
(a) Rayleigh envelope PDF + histogram.
(b) A faded power time series (dB) showing deep fades.
(c) Capacity CDF: AWGN vs Rayleigh (same mean SNR) -> outage.
(d) Ergodic capacity vs SNR: AWGN vs Rayleigh."""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__)); rng=np.random.default_rng(7)
NAVY="#002070"; BLUE="#2050D0"; ORANGE="#F08010"; GREY="#5a5f6e"; RED="#D01010"; GREEN="#1e9e6a"
plt.rcParams.update({"font.size":10,"axes.titlesize":12,"axes.titlecolor":NAVY,"axes.titleweight":"bold"})
fig,((a,b),(c,d))=plt.subplots(2,2,figsize=(13.2,9.2))

# ---------------- (a) Rayleigh envelope PDF ----------------
sig=1.0
h=(rng.standard_normal(200000)+1j*rng.standard_normal(200000))*sig/np.sqrt(2)  # E|h|^2=1
r=np.abs(h)
a.hist(r,bins=120,density=True,color=BLUE,alpha=0.35,label="simulated |h|")
rr=np.linspace(0,4,300); pdf=(rr/(sig**2/2))*np.exp(-rr**2/(2*(sig**2/2)))  # sigma_R^2=sig^2/2
a.plot(rr,pdf,color=NAVY,lw=2.2,label=r"Rayleigh $\frac{r}{\sigma^2}e^{-r^2/2\sigma^2}$")
a.set_title("(a) Rayleigh fading envelope |h|"); a.set_xlabel("envelope |h|"); a.set_ylabel("pdf")
a.legend(fontsize=8.5); a.grid(alpha=0.25)
a.text(2.0,0.6,"power $|h|^2$ is\nexponential",fontsize=8.5,color=GREY)

# ---------------- (b) faded power time series ----------------
# correlated (Clarke-like) fading via filtered complex Gaussian
N=2000; fd=0.01  # normalised Doppler
t=np.arange(N)
w=(rng.standard_normal(N)+1j*rng.standard_normal(N))/np.sqrt(2)
# simple lowpass to induce time-correlation
from numpy import convolve
k=np.exp(-np.linspace(0,4,60)); k/=np.sqrt(np.sum(k**2))
hf=convolve(w,k,mode="same"); hf/=np.sqrt(np.mean(np.abs(hf)**2))
pdB=10*np.log10(np.abs(hf)**2+1e-12)
b.plot(t,pdB,color=BLUE,lw=0.9)
b.axhline(0,color=GREY,lw=1,ls="--",label="mean power (0 dB)")
b.axhline(-10,color=RED,lw=1,ls=":",label="-10 dB deep-fade line")
b.set_title("(b) Faded received power over time"); b.set_xlabel("time (samples)"); b.set_ylabel("|h|$^2$ (dB)")
b.set_ylim(-35,10); b.legend(fontsize=8.5,loc="lower right"); b.grid(alpha=0.25)
b.text(60,-30,"deep fades -> bursts of errors\n(diversity / beamforming fixes this)",fontsize=8.5,color=RED)

# ---------------- (c) capacity CDF AWGN vs Rayleigh ----------------
snr0=10**(10/10)  # 10 dB mean
Ns=200000
g=np.abs((rng.standard_normal(Ns)+1j*rng.standard_normal(Ns))/np.sqrt(2))**2
C_ray=np.log2(1+snr0*g); C_awgn=np.log2(1+snr0)
xs=np.sort(C_ray); cdf=np.arange(1,Ns+1)/Ns
c.plot(xs,cdf,color=ORANGE,lw=2.2,label="Rayleigh (fading)")
c.axvline(C_awgn,color=BLUE,lw=2.2,label=f"AWGN = {C_awgn:.2f} b/s/Hz")
# 10% outage capacity
Cout=np.percentile(C_ray,10)
c.axhline(0.1,color=GREY,lw=1,ls=":"); c.plot([Cout],[0.1],"o",color=RED)
c.annotate(f"10% outage\ncapacity = {Cout:.2f}",xy=(Cout,0.1),xytext=(Cout+0.6,0.28),fontsize=8.5,color=RED,
           arrowprops=dict(arrowstyle="->",color=RED))
c.set_title("(c) Capacity CDF at 10 dB mean SNR"); c.set_xlabel("capacity (bits/s/Hz)"); c.set_ylabel("P(C < x)")
c.legend(fontsize=8.5,loc="lower right"); c.grid(alpha=0.25)

# ---------------- (d) ergodic capacity vs SNR ----------------
snr_dB=np.linspace(-5,35,60); erg=[]; awg=[]
gg=np.abs((rng.standard_normal(60000)+1j*rng.standard_normal(60000))/np.sqrt(2))**2
for s in snr_dB:
    S=10**(s/10); erg.append(np.mean(np.log2(1+S*gg))); awg.append(np.log2(1+S))
d.plot(snr_dB,awg,color=BLUE,lw=2.2,label="AWGN (no fading)")
d.plot(snr_dB,erg,color=ORANGE,lw=2.2,label="Rayleigh ergodic")
d.set_title("(d) Ergodic capacity: AWGN vs Rayleigh"); d.set_xlabel("mean SNR (dB)"); d.set_ylabel("capacity (bits/s/Hz)")
d.legend(fontsize=8.5); d.grid(alpha=0.25)
d.text(-3,9,"fading costs capacity\n(and adds outage risk)",fontsize=8.5,color=GREY)

fig.suptitle("Channel II: Rayleigh fading -- envelope, deep fades, and the capacity cost",
             fontsize=13.5,color=NAVY,weight="bold",y=0.995)
fig.tight_layout(rect=(0,0,1,0.965))
fig.savefig(os.path.join(HERE,"ch2_rayleigh_fading.png"),dpi=145,bbox_inches="tight")
print("saved ch2_rayleigh_fading.png")
