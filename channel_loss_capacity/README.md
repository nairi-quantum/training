# Seminar: Channel — loss, fading & capacity  (presenter: Viktorya; support: Martin)

The channel is the limit every link lives under: signals **lose power** with distance (path loss),
**fluctuate** in multipath (fading), and carry only so many bits (**Shannon capacity**) — and only so
many *secret* bits (**secrecy capacity**). Quantum links face the same physics in sharper form: they are
fundamentally **loss-limited** (the repeaterless PLOB bound). This is the channel layer shared by our SDR
testbed and the future photonic QSDC link.

Builds on the previous seminars — **Nathalie** (SNR & BER) and **Seroj** (I/Q & constellations): here we
see what the *channel* does to those symbols, and Martin adds **beam patterns** as the lever that pushes
loss, fading and secrecy the right way. See also the self-check exercise `simulations/capacity_loss/`.

## Run (no hardware needed)
```bash
python -m pip install numpy matplotlib
python ch1_pathloss_capacity.py    # -> ch1_pathloss_capacity.png
python ch2_rayleigh_fading.py      # -> ch2_rayleigh_fading.png
python ch3_beam_patterns.py        # -> ch3_beam_patterns.png
python ch4_beam_rayleigh.py        # -> ch4_beam_rayleigh.png
```
The rendered PNGs are committed here too, so they can be dropped straight into slides; re-run any script
to modify (frequencies, fibre `alpha`, SNR range, number of array elements `N`, Bob/Eve angles).

## What each demo shows
| Script | Shows | Expected takeaway |
|---|---|---|
| `ch1_pathloss_capacity.py` | Attenuation in dB (free-space vs fibre); PLOB bound `-log2(1-η)`; `C=B·log2(1+SNR)`; secrecy `[C_Bob−C_Eve]+` | Loss adds up in dB; the quantum channel is loss-limited; secrecy needs Bob's channel better than Eve's |
| `ch2_rayleigh_fading.py` | Rayleigh envelope pdf; faded power vs time; capacity CDF + 10% outage; ergodic capacity | Multipath causes deep fades → outage; fading lowers average capacity |
| `ch3_beam_patterns.py` | Tx pattern vs N; Rx beam steered to Bob, Eve in a sidelobe; array gain `10·log10(N)`; capacity shift | Beamforming buys SNR (reach) and directivity (secrecy) |
| `ch4_beam_rayleigh.py` | Clean LOS beam vs Rayleigh snapshots; SISO vs MRC capacity CDF; outage & ergodic vs N | Under fading the beam breaks up, but combining N antennas (diversity) restores capacity |

## How beamforming ties it together (Martin)
- **Array gain** (`+10·log10(N)` dB) fights **path loss** → shifts the Shannon curve left = more reach — `ch3`.
- **Directivity** (main lobe on Bob, null on Eve) raises **secrecy capacity** — `ch3` panel (b).
- **Diversity** (MRC over N antennas) beats **Rayleigh fading** → removes the deep-fade tail, lifts outage — `ch4`.

The classical "Bob-better-than-Eve" requirement is the direct analog of the quantum secret-key rate, which
loss alone caps (PLOB) — so reducing effective loss and leakage is exactly what helps both.
