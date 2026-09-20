# -*- coding: utf-8 -*-
"""Seminar: Channel -- beamforming (Martin's Tx/Rx beam patterns) and how it fits.
Beamforming gives ARRAY GAIN (fights path loss -> more SNR -> more capacity) and
DIRECTIVITY (steer to Bob, starve Eve -> more secrecy).
(a) Tx beam pattern (ULA) for N = 4, 8, 16 -- more elements, narrower beam.
(b) Rx beam steered to Bob; Eve sits in a sidelobe (physical-layer security).
(c) Array gain 10log10(N) and the SNR it buys.
(d) Shannon capacity with vs without an N=16 beamformer."""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__))
NAVY="#002070"; BLUE="#2050D0"; ORANGE="#F08010"; GREY="#5a5f6e"; RED="#D01010"; GREEN="#1e9e6a"
plt.rcParams.update({"font.size":10,"axes.titlesize":11.5,"axes.titlecolor":NAVY,"axes.titleweight":"bold"})

def af_dB(theta, N, theta0, d=0.5):
    """Normalised ULA array-factor magnitude in dB. theta,theta0 in rad; d in wavelengths."""
    psi = 2*np.pi*d*(np.cos(theta)-np.cos(theta0))
    with np.errstate(invalid="ignore",divide="ignore"):
        af = np.sin(N*psi/2)/(N*np.sin(psi/2))
    af = np.where(np.abs(np.sin(psi/2))<1e-9, 1.0, af)
    return 20*np.log10(np.abs(af)+1e-6)

fig=plt.figure(figsize=(13.2,9.4))
a=fig.add_subplot(2,2,1,projection="polar")
bb=fig.add_subplot(2,2,2,projection="polar")
c=fig.add_subplot(2,2,3)
d=fig.add_subplot(2,2,4)
th=np.linspace(0,2*np.pi,1000); FLOOR=-30

# ---------------- (a) Tx pattern for several N ----------------
for N,col in [(4,GREEN),(8,BLUE),(16,ORANGE)]:
    g=np.clip(af_dB(th,N,np.pi/2),FLOOR,0)-FLOOR
    a.plot(th,g,color=col,lw=1.8,label=f"N = {N}")
a.set_title("(a) Tx beam pattern (broadside): more elements = narrower beam",va="bottom",pad=18)
a.set_rticks([]); a.set_thetagrids(range(0,360,45)); a.legend(loc="lower right",fontsize=8,bbox_to_anchor=(1.15,-0.05))

# ---------------- (b) Rx steered to Bob, Eve in sidelobe ----------------
N=16; thB=np.deg2rad(60); thE=np.deg2rad(115)
g=np.clip(af_dB(th,N,thB),FLOOR,0)-FLOOR
bb.plot(th,g,color=NAVY,lw=1.9)
gB=(np.clip(af_dB(np.array([thB]),N,thB),FLOOR,0)-FLOOR).item()
gE=(np.clip(af_dB(np.array([thE]),N,thB),FLOOR,0)-FLOOR).item(); gE=max(gE,0.2)
bb.plot([thB],[gB],"o",color=GREEN,ms=9); bb.plot([thE],[gE],"s",color=RED,ms=9)
bb.annotate("Bob\n(main lobe)",xy=(thB,gB),xytext=(thB,gB+2),color=GREEN,fontsize=8.5,ha="center")
bb.annotate("Eve\n(sidelobe/null)",xy=(thE,gE),xytext=(thE,12),color=RED,fontsize=8.5,ha="center")
bb.set_title("(b) Rx beam steered to Bob; Eve starved (secrecy)",va="bottom",pad=18)
bb.set_rticks([]); bb.set_thetagrids(range(0,360,45))

# ---------------- (c) array gain vs N ----------------
Nn=np.arange(1,65)
c.plot(Nn,10*np.log10(Nn),color=BLUE,lw=2.4)
for Nx in [4,16,64]:
    c.plot([Nx],[10*np.log10(Nx)],"o",color=ORANGE)
    c.annotate(f"N={Nx}: +{10*np.log10(Nx):.1f} dB",xy=(Nx,10*np.log10(Nx)),
               xytext=(Nx+1,10*np.log10(Nx)-2.2),fontsize=8.5,color=GREY)
c.set_title(r"(c) Array gain = $10\log_{10}N$ (SNR the beamformer buys)")
c.set_xlabel("number of elements N"); c.set_ylabel("array gain (dB)"); c.grid(alpha=0.25)

# ---------------- (d) capacity with/without beamforming ----------------
snr_dB=np.linspace(-10,30,300); snr=10**(snr_dB/10)
Ngain=16; gain=Ngain  # linear array gain
c0=np.log2(1+snr); c1=np.log2(1+gain*snr)
d.plot(snr_dB,c0,color=GREY,lw=2.2,label="no beamforming")
d.plot(snr_dB,c1,color=ORANGE,lw=2.2,label=f"N={Ngain} beamformer (+{10*np.log10(Ngain):.1f} dB)")
d.set_title("(d) Beamforming shifts the capacity curve left")
d.set_xlabel("element SNR (dB)"); d.set_ylabel("capacity (bits/s/Hz)"); d.legend(fontsize=8.5); d.grid(alpha=0.25)
d.text(-9,7,"same capacity at\n~12 dB lower SNR\n= longer reach",fontsize=8.5,color=GREY)

fig.suptitle("Channel III: beamforming (Tx/Rx patterns) -- array gain fights loss, directivity buys secrecy",
             fontsize=13,color=NAVY,weight="bold",y=0.99)
fig.tight_layout(rect=(0,0,1,0.96))
fig.savefig(os.path.join(HERE,"ch3_beam_patterns.png"),dpi=145,bbox_inches="tight")
print("saved ch3_beam_patterns.png")
