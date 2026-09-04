# -*- coding: utf-8 -*-
"""Self-check for the QSDC reliability exercise. Run:  python check_reliability.py"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    from reliability import delivery_prob, session_reliability
except Exception as e:
    print("Could not import reliability.py:", e); raise SystemExit(1)


def dp(p, m):
    return 1 - p ** (m + 1)


ok = True
for p, m in [(0.1, 3), (0.3, 2), (0.5, 3), (0.0, 3)]:
    got, exp = delivery_prob(p, m), dp(p, m)
    if got is None:
        print("delivery_prob returned None — complete the TODO."); ok = False; break
    good = abs(got - exp) < 1e-9
    print(f"delivery_prob(p={p}, retries={m}) = {got:.6f}   expected {exp:.6f}   {'ok' if good else 'OFF'}")
    ok = ok and good

if ok:
    for p, n, m in [(0.1, 4, 3), (0.2, 3, 2)]:
        got, exp = session_reliability(p, n, m), dp(p, m) ** n
        if got is None:
            print("session_reliability returned None — complete the TODO."); ok = False; break
        good = abs(got - exp) < 1e-9
        print(f"session_reliability(p={p}, n={n}, retries={m}) = {got:.6f}   expected {exp:.6f}   {'ok' if good else 'OFF'}")
        ok = ok and good

print("\nRESULT:", "PASS ✅" if ok else "NOT YET ❌  — check the retransmission and 'all must arrive' logic.")
