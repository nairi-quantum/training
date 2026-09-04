# -*- coding: utf-8 -*-
"""Self-check for the LFM dechirp exercise. Run:  python check_dechirp.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    from lfm_dechirp import estimate_beat_freq
except Exception as e:
    print("Could not import lfm_dechirp.py:", e); raise SystemExit(1)

fs, B, T = 1e6, 1e7, 1e-2
slope = B / T
res = 1.0 / T                      # FFT frequency resolution (Hz)
ok = True
print(f"{'tau(us)':>8} {'expected fb':>12} {'your fb':>10}   result")
for tau in [2e-6, 3e-6, 5e-6]:
    exp = slope * tau
    try:
        est = estimate_beat_freq(fs, B, T, tau)
    except Exception as e:
        print("  error while running your code:", e); ok = False; break
    if est is None:
        print("  estimate_beat_freq returned None — complete the TODOs."); ok = False; break
    good = abs(est - exp) <= 2 * res + 1
    print(f"{tau*1e6:>8.1f} {exp:>12.0f} {est:>10.0f}   {'ok' if good else 'OFF'}")
    ok = ok and good

print("\nRESULT:", "PASS ✅  your dechirp finds the beat frequency!" if ok
      else "NOT YET ❌  — check the conjugate multiply, the FFT, and the peak search.")
