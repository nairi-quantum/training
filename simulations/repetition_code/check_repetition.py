# -*- coding: utf-8 -*-
"""Self-check for the repetition-code exercise. Run:  python check_repetition.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import math
try:
    from repetition_code import repetition_ber
except Exception as e:
    print("Could not import repetition_code.py:", e); raise SystemExit(1)


def theory3(p):
    return 3 * p**2 - 2 * p**3      # majority-of-3 error probability


N = 300_000
ok = True
for p in [0.05, 0.10, 0.20]:
    try:
        sim = repetition_ber(p, n_rep=3, n_bits=N, seed=int(p * 1000))
    except Exception as e:
        print("  error while running your code:", e); ok = False; break
    if sim is None:
        print("  repetition_ber returned None — complete the TODOs."); ok = False; break
    th = theory3(p)
    tol = 5 * math.sqrt(max(th, 1e-9) * (1 - th) / N) + 3e-4
    good = abs(sim - th) <= tol and sim < p            # matches theory AND beats the raw channel
    print(f"p={p:.2f}  decoded BER={sim:.4e}  theory(3p^2-2p^3)={th:.4e}  (raw p={p})  {'ok' if good else 'OFF'}")
    ok = ok and good

print("\nRESULT:", "PASS ✅  your repetition code corrects errors!" if ok
      else "NOT YET ❌  — check encode (np.repeat), the majority vote, and the BER count.")
