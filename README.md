# training — hands-on exercises

Self-checking exercises for the Nairi Quantum learning program. Each exercise:
1. has an **`INSTRUCTIONS.md`** (the theory + what to do),
2. gives you a **code skeleton** with `TODO`s to complete, and
3. comes with a **checker** you run to see if your answer is right — instant PASS/❌ feedback.

## How to do an exercise
```bash
cd <exercise folder>
# read INSTRUCTIONS.md, then fill the TODOs in the skeleton file
python check_*.py        # self-check: PASS ✅ or NOT YET ❌
```
When it passes, commit on a branch and open a Pull Request:
`git checkout -b exercise/<your-name>-<exercise>` → commit → push → PR.

Requires **numpy** (`pip install numpy`).

## Exercise → Pod → Topic map
| Exercise | Pod | Syllabus topic(s) | Folder | Check |
|---|---|---|---|---|
| BER of BPSK | Simulations | 3 — Noise, SNR & BER (+2) | `simulations/ber_bpsk/` | `python check_ber.py` |
| LFM chirp & dechirp | SDR testbed | 2 — Modulation; 5 — Detection | `sdr/lfm_dechirp/` | `python check_dechirp.py` |
| Reliability under packet loss | QSDC sim | 8 — Classical control channel | `qsdc/reliability/` | `python check_reliability.py` |
| QKD secure-key-rate & entropy | Theory/Quantum | 7 — Info theory & security | `theory/qkd_keyrate/` | `python check_keyrate.py` |
| Channel capacity & link loss | Simulations | 4 — Channel: loss & capacity | `simulations/capacity_loss/` | `python check_capacity.py` |
| Repetition code (error correction) | Simulations / Theory | 6 — Channel coding | `simulations/repetition_code/` | `python check_repetition.py` |
| BB84 sifting & QBER | Theory/Quantum | 7 → quantum (first protocol) | `theory/bb84_sifting/` | `python check_bb84.py` |

Start with the exercise for your pod. Everyone is encouraged to do **BER of BPSK** first — it's the foundation the others build on.
