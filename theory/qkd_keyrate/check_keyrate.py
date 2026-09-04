# -*- coding: utf-8 -*-
"""Self-check for the QKD secure-key-rate exercise. Run:  python check_keyrate.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    from qkd_keyrate import H2, secure_key_rate
except Exception as e:
    print("Could not import qkd_keyrate.py:", e); raise SystemExit(1)


def near(a, b, t=2e-3):
    return a is not None and abs(a - b) <= t


ok = True
for name, got, exp in [("H2(0.5)", H2(0.5), 1.0), ("H2(0.0)", H2(0.0), 0.0), ("H2(0.11)", H2(0.11), 0.4999)]:
    good = near(got, exp)
    print(f"{name} = {got}   ~ {exp}   {'ok' if good else 'OFF'}")
    ok = ok and good

r_lo, r_hi = secure_key_rate(0.02), secure_key_rate(0.12)
print(f"secure_key_rate(0.02) = {r_lo}   (should be > 0)")
print(f"secure_key_rate(0.12) = {r_hi}   (should be 0)")
ok = ok and (r_lo is not None and r_lo > 0)
ok = ok and (r_hi is not None and abs(r_hi) < 1e-9)

# find the QBER threshold where the rate hits zero
thr, p = None, 0.0
if all(x is not None for x in [r_lo, r_hi]):
    while p < 0.5:
        v = secure_key_rate(p)
        if v is None:
            break
        if v <= 1e-9:
            thr = p; break
        p += 0.001
    print(f"QBER threshold where the key rate hits 0: ~{thr:.3f}" if thr is not None else "threshold: n/a",
          " (theory ≈ 0.110)")
    ok = ok and (thr is not None and 0.10 <= thr <= 0.12)

print("\nRESULT:", "PASS ✅  entropy + BB84 threshold correct!" if ok
      else "NOT YET ❌  — check H2 (edge cases + log2) and the r = 1 - 2*H2(qber) floor.")
