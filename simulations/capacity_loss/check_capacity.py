# -*- coding: utf-8 -*-
"""Self-check for the capacity & link-budget exercise. Run:  python check_capacity.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import math
try:
    from capacity_loss import shannon_capacity, rx_snr_db
except Exception as e:
    print("Could not import capacity_loss.py:", e); raise SystemExit(1)


def cap(b, s):
    return b * math.log2(1 + 10 ** (s / 10))


ok = True
cases = [(1e6, 20), (1e6, 0), (2e6, 10)]
for b, s in cases:
    got, exp = shannon_capacity(b, s), cap(b, s)
    if got is None:
        print("shannon_capacity returned None — complete the TODO."); ok = False; break
    good = abs(got - exp) <= 1e-3 * exp
    print(f"capacity(B={b:.0e}, SNR={s}dB) = {got:.3e}   expected {exp:.3e}   {'ok' if good else 'OFF'}")
    ok = ok and good

if ok:
    for tx, pl, no in [(0, 60, -90), (10, 100, -100), (-30, 40, -110)]:
        got, exp = rx_snr_db(tx, pl, no), tx - pl - no
        if got is None:
            print("rx_snr_db returned None — complete the TODO."); ok = False; break
        good = abs(got - exp) < 1e-9
        print(f"rx_snr_db({tx},{pl},{no}) = {got}   expected {exp}   {'ok' if good else 'OFF'}")
        ok = ok and good

print("\nRESULT:", "PASS ✅" if ok else "NOT YET ❌  — check the log2 capacity formula and the dB subtraction.")
