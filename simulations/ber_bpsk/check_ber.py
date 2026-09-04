# -*- coding: utf-8 -*-
"""Self-check for the BPSK BER exercise. Run:  python check_ber.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import math
try:
    from ber_bpsk import simulate_ber
except Exception as e:
    print("Could not import ber_bpsk.py:", e); raise SystemExit(1)


def theory(db):
    e = 10 ** (db / 10.0)
    return 0.5 * math.erfc(math.sqrt(e))


N = 500_000
pts = [0, 2, 4, 6]
ok = True
print(f"{'Eb/N0(dB)':>10} {'your BER':>12} {'theory':>12}   result")
for db in pts:
    try:
        sim = simulate_ber(db, N, seed=100 + db)
    except Exception as e:
        print("  error while running your code:", e); ok = False; break
    if sim is None:
        print("  simulate_ber returned None — complete the TODOs in ber_bpsk.py."); ok = False; break
    th = theory(db)
    tol = 5 * math.sqrt(max(th, 1e-9) * (1 - th) / N) + 2e-4   # statistical tolerance
    good = abs(sim - th) <= tol
    print(f"{db:>10} {sim:>12.4e} {th:>12.4e}   {'ok' if good else 'OFF'}")
    ok = ok and good

print("\nRESULT:", "PASS ✅  your BPSK BER matches theory!" if ok
      else "NOT YET ❌  — re-check modulation (±1), sigma, detection, and the BER count.")
