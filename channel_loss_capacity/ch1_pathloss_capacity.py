# -*- coding: utf-8 -*-
"""Seminar: Channel -- loss & capacity.
(a) Path loss in dB vs distance: RF free-space (FSPL) vs optical fibre (0.2 dB/km).
(b) Quantum repeaterless bound (PLOB secret-key capacity) vs fibre distance -- loss-limited.
(c) Shannon capacity C = B log2(1+SNR).
(d) Secrecy capacity Cs = [C_Bob - C_Eve]+  (Shannon -> secrecy)."""
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__))
NAVY="#002070"; BLUE="#2050D0"; ORANGE="#F08010"; GREY="#5a5f6e"; RED="#D01010"; GREEN="#1e9e6a"
plt.rcParams.update({"font.size":10,"axes.titlesize":12,"axes.titlecolor":NAVY,"axes.titleweight":"bold"})
fig,((a,b),(c,d))=plt.subplots(2,2,figsize=(13.2,9.2))

# ---------------- (a) path loss dB vs distance ----------------
# RF free-space FSPL(dB) = 20log10(d_km) + 20log10(f_MHz) + 32.44
d_km=np.linspace(0.01,50,400)
for fMHz,col,lab in [(2400,BLUE,"2.4 GHz (Wi-Fi)"),(28000,ORANGE,"28 GHz (mmWave)")]:
    fspl=20*np.log10(d_km)+20*np.log10(fMHz)+32.44
    a.plot(d_km,fspl,color=col,lw=2,label="free-space "+lab)
alpha_fib=0.2  # dB/km at 1550 nm
a.plot(d_km,alpha_fib*d_km,color=GREEN,lw=2.4,ls="--",label="optical fibre (0.2 dB/km)")
a.set_title("(a) Attenuation in dB vs distance"); a.set_xlabel("distance (km)"); a.set_ylabel("loss (dB)")
a.legend(fontsize=8.5,loc="center right"); a.grid(alpha=0.25)
a.text(0.5,150,"free-space: $\\propto 20\\log_{10}d$\nfibre: linear $\\alpha L$",fontsize=8.5,color=GREY)

# ---------------- (b) quantum repeaterless bound (PLOB) ----------------
L=np.linspace(0,300,400)
eta=10**(-alpha_fib*L/10.0)                 # fibre transmittance
K_plob=-np.log2(1-eta+1e-18)                # secret-key capacity, bits/use
b.semilogy(L,K_plob,color=NAVY,lw=2.4,label=r"PLOB bound $-\log_2(1-\eta)$")
b.semilogy(L,1.44*eta,color=ORANGE,lw=1.6,ls=":",label=r"high-loss $\approx 1.44\,\eta$")
b.set_title("(b) Quantum channel is loss-limited (repeaterless bound)")
b.set_xlabel("fibre length L (km)"); b.set_ylabel("secret-key capacity (bits/use)")
b.set_ylim(1e-4,20); b.legend(fontsize=8.5); b.grid(alpha=0.25,which="both")
b.text(150,3,"no repeaterless system\ncan beat this rate",fontsize=8.5,color=RED)

# ---------------- (c) Shannon capacity ----------------
snr_dB=np.linspace(-10,40,400); snr=10**(snr_dB/10)
C=np.log2(1+snr)
c.plot(snr_dB,C,color=BLUE,lw=2.4)
c.set_title(r"(c) Shannon capacity  $C=B\log_2(1+\mathrm{SNR})$")
c.set_xlabel("SNR (dB)"); c.set_ylabel("spectral efficiency C/B (bits/s/Hz)"); c.grid(alpha=0.25)
c.text(-8,10,"low SNR: $C\\approx1.44\\,\\mathrm{SNR}$ (power-limited)\nhigh SNR: $C\\approx\\log_2\\mathrm{SNR}$ (+1 bit / 3 dB)",
       fontsize=8.5,color=GREY)

# ---------------- (d) secrecy capacity ----------------
snrB_dB=np.linspace(-5,35,400); snrB=10**(snrB_dB/10)
for snrE_dB,col in [(0,GREEN),(10,ORANGE),(20,RED)]:
    snrE=10**(snrE_dB/10)
    Cs=np.maximum(np.log2(1+snrB)-np.log2(1+snrE),0)
    d.plot(snrB_dB,Cs,color=col,lw=2,label=f"Eve SNR = {snrE_dB} dB")
d.set_title(r"(d) Secrecy capacity  $C_s=[C_{Bob}-C_{Eve}]^+$")
d.set_xlabel("Bob SNR (dB)"); d.set_ylabel("secrecy capacity (bits/s/Hz)")
d.legend(fontsize=8.5); d.grid(alpha=0.25)
d.text(-4,6.5,"secrecy needs Bob's channel\nBETTER than Eve's",fontsize=8.5,color=GREY)

fig.suptitle("Channel I: loss, capacity, secrecy -- and the quantum repeaterless limit",
             fontsize=13.5,color=NAVY,weight="bold",y=0.995)
fig.tight_layout(rect=(0,0,1,0.965))
fig.savefig(os.path.join(HERE,"ch1_pathloss_capacity.png"),dpi=145,bbox_inches="tight")
print("saved ch1_pathloss_capacity.png")
