# Seminar: Digital Modulation & I/Q  (presenter: Seroj)

The classical foundation that leads straight into the **CV quantum receiver**: I/Q (amplitude & phase)
is exactly what coherent / homodyne detection measures, and **constellation points ↔ quantum states**.

Builds on the previous seminar (Nathalie: SNR & BER) — here we see *what the symbols are* that noise
scatters, and extend BER to more modulations.

## Run (no hardware needed)
```bash
python -m pip install numpy matplotlib
python constellations_noise.py     # -> constellation_bpsk/qpsk/16qam.png
python ber_vs_snr.py               # -> ber_vs_snr.png  (+ prints a table)
python pulse_shaping_eye.py        # -> pulse_shaping_eye.png
python phase_offset.py             # -> phase_offset.png
```

## What each demo shows
| Script | Shows | Expected takeaway |
|---|---|---|
| `constellations_noise.py` | BPSK/QPSK/16-QAM ideal points + received clouds at Es/N0 = 0,5,10,20 dB | higher SNR → tighter clouds — Nathalie's SNR→BER, *visualized* |
| `ber_vs_snr.py` | measured vs theory BER for the three modulations | BPSK≈QPSK; 16-QAM needs ~4 dB more for the same BER (rate vs robustness) |
| `pulse_shaping_eye.py` | RRC-shaped waveform, **eye diagram**, spectrum for roll-off 0.2 vs 0.5 | shaping narrows bandwidth and keeps the eye open (low ISI) |
| `phase_offset.py` | QPSK constellation with a 20° phase error | a phase error rotates the whole constellation → need synchronization |

## The chirp / SDR part
For the LFM chirp & dechirp demo, use the existing exercise: **`../sdr/lfm_dechirp`** (I/Q of a chirp,
dechirp to a beat tone; connects to FMCW radar / ISAC — Martin's work).

## The quantum bridge (closing message)
> I/Q is amplitude and phase — the same quantities a coherent/homodyne **CV quantum receiver** measures.
> Master the constellation and you already speak the language of continuous-variable quantum communication
> (coherent states in phase space; shot noise as the quantum noise floor; CV-QKD = Gaussian modulation of
> a constellation).
