# -*- coding: utf-8 -*-
"""Seminar: Channel -- Martin's idea, beam patterns UNDER Rayleigh fading.
In line-of-sight the Rx pattern is a clean beam; in rich (Rayleigh) multipath the
per-element phases are random, so a single snapshot's pattern breaks up -- but
combining N antennas (MRC beamforming) gives DIVERSITY + ARRAY GAIN, which
removes deep fades and lifts the outage capacity.
(a) Rx pattern: clean LOS beam vs several Rayleigh multipath snapshots.
(b) Capacity CDF: SISO Rayleigh vs MRC with N = 2, 4, 8.
(c) 10% outage capacity vs N (diversity gain).
(d) Ergodic capacity vs N at 10 dB (array gain)."""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__)); rng=np.random.default_rng(11)
NAVY="#002070"; BLUE="#2050D0"; ORANGE="#F08010"; GREY="#5a5f6e"; RED="#D01010"; GREEN="#1e9e6a"
plt.rcParams.update({"font.size":10,"axes.titlesize":11.5,"axes.titlecolor":NAVY,"axes.titleweight":"bold"})

fig=plt.figure(figsize=(13.2,9.4))
a=fig.add_subplot(2,2,1,projection="polar")
b=fig.add_subplot(2,2,2); c=fig.add_subplot(2,2,3); d=fig.add_subplot(2,2,4)

# ---------------- (a) LOS beam vs Rayleigh multipath snapshots ----------------
N=8; d_sp=0.5; th=np.linspace(0,2*np.pi,720); thB=np.pi/2; FLOOR=-25
n=np.arange(N)
# LOS: matched weights -> clean beam
steer=lambda ang: np.exp(1j*2*np.pi*d_sp*n[:,None]*np.cos(ang)[None,:])
w_los=np.exp(-1j*2*np.pi*d_sp*n*np.cos(thB))            # conjugate steer to Bob
A=steer(th)                                              # N x len(th)
patt=np.abs(w_los.conj()@A)/N
a.plot(th,np.clip(20*np.log10(patt+1e-6),FLOOR,0)-FLOOR,color=NAVY,lw=2.2,label="LOS (clean beam)")
for s in range(4):
    hcol=(rng.standard_normal(N)+1j*rng.standard_normal(N))/np.sqrt(2)  # Rayleigh per element
    w=(w_los*np.conj(hcol)); w/=np.linalg.norm(w)
    p=np.abs(w.conj()@A); p/=p.max()
    a.plot(th,np.clip(20*np.log10(p+1e-6),FLOOR,0)-FLOOR,lw=0.9,alpha=0.6,color=ORANGE)
a.plot([],[],color=ORANGE,lw=1.2,label="Rayleigh snapshots")
a.set_title("(a) Rx pattern: clean LOS beam vs Rayleigh multipath",va="bottom",pad=16)
a.set_rticks([]); a.set_thetagrids(range(0,360,45)); a.legend(loc="lower right",fontsize=7.6,bbox_to_anchor=(1.18,-0.05))

# ---------------- (b) capacity CDF SISO vs MRC ----------------
snr0=10**(10/10); Ns=120000
def cap_mrc(Nrx):
    G=np.sum(np.abs((rng.standard_normal((Ns,Nrx))+1j*rng.standard_normal((Ns,Nrx)))/np.sqrt(2))**2,axis=1)
    return np.log2(1+snr0*G)
for Nrx,col in [(1,RED),(2,ORANGE),(4,BLUE),(8,GREEN)]:
    C=np.sort(cap_mrc(Nrx)); cdf=np.arange(1,Ns+1)/Ns
    b.plot(C,cdf,color=col,lw=2,label=f"N = {Nrx}"+(" (SISO)" if Nrx==1 else " MRC"))
b.set_title("(b) Capacity CDF at 10 dB: MRC removes the fade tail")
b.set_xlabel("capacity (bits/s/Hz)"); b.set_ylabel("P(C < x)"); b.legend(fontsize=8.5); b.grid(alpha=0.25)
b.axhline(0.1,color=GREY,lw=1,ls=":"); b.text(0.15,0.13,"10% outage line",fontsize=8,color=GREY)

# ---------------- (c) outage capacity vs N ----------------
Nlist=np.arange(1,17); out=[]
for Nrx in Nlist: out.append(np.percentile(cap_mrc(Nrx),10))
c.plot(Nlist,out,"-o",color=BLUE,lw=2,ms=4)
c.set_title("(c) 10% outage capacity vs N (diversity gain)")
c.set_xlabel("number of Rx antennas N"); c.set_ylabel("outage capacity (bits/s/Hz)"); c.grid(alpha=0.25)
c.text(6,out[0]+0.3,"fading penalty shrinks\nas N grows",fontsize=8.5,color=GREY)

# ---------------- (d) ergodic capacity vs N ----------------
erg=[];
for Nrx in Nlist: erg.append(np.mean(cap_mrc(Nrx)))
c_awgn_gain=[np.log2(1+snr0*Nrx) for Nrx in Nlist]  # pure array-gain reference
d.plot(Nlist,erg,"-o",color=ORANGE,lw=2,ms=4,label="Rayleigh + MRC (ergodic)")
d.plot(Nlist,c_awgn_gain,"--",color=GREY,lw=1.6,label="array-gain reference $\\log_2(1+N\\,\\mathrm{SNR})$")
d.set_title("(d) Ergodic capacity vs N at 10 dB (array gain)")
d.set_xlabel("number of Rx antennas N"); d.set_ylabel("ergodic capacity (bits/s/Hz)")
d.legend(fontsize=8.5); d.grid(alpha=0.25)

fig.suptitle("Channel IV: beam patterns under Rayleigh fading -- diversity + array gain restore capacity",
             fontsize=13,color=NAVY,weight="bold",y=0.99)
fig.tight_layout(rect=(0,0,1,0.96))
fig.savefig(os.path.join(HERE,"ch4_beam_rayleigh.png"),dpi=145,bbox_inches="tight")
print("saved ch4_beam_rayleigh.png")
