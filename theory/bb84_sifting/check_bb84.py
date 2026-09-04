# -*- coding: utf-8 -*-
"""Self-check for the BB84 sifting exercise. Run:  python check_bb84.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    from bb84_sifting import bb84
except Exception as e:
    print("Could not import bb84_sifting.py:", e); raise SystemExit(1)

ok = True

sf, q = bb84(200_000, 0.0, seed=1)
if sf is None or q is None:
    print("bb84 returned None — complete the TODOs."); ok = False
else:
    good_sf = 0.49 <= sf <= 0.51
    good_q0 = q < 0.005
    print(f"clean channel:  sift_fraction={sf:.3f} (want ~0.50)  QBER={q:.4f} (want ~0)  {'ok' if good_sf and good_q0 else 'OFF'}")
    ok = ok and good_sf and good_q0

if ok:
    sf2, q2 = bb84(200_000, 0.10, seed=2)
    good_q = 0.09 <= q2 <= 0.11
    print(f"10% errors:     sift_fraction={sf2:.3f} (want ~0.50)  QBER={q2:.4f} (want ~0.10)  {'ok' if good_q else 'OFF'}")
    ok = ok and good_q

print("\nRESULT:", "PASS ✅  sifting and QBER are correct!" if ok
      else "NOT YET ❌  — sift_fraction = mean(match); QBER = mean(a_bits[match] != b_bits[match]).")
