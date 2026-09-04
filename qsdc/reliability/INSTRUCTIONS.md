# Exercise — Reliability under packet loss  (QSDC sim pod)

**Covers:** Topic 8 (Sync, framing & the classical control channel)
**You'll learn:** why a lossy classical coordination channel hurts QSDC — the core idea of Nathalie's paper.

## Theory (short)
QSDC needs a **classical control channel** for check reports and acknowledgements. If a control message is
lost, the sender **retransmits** — up to `max_retries` times.
- One message is **delivered** as long as *at least one* of its `(max_retries + 1)` attempts gets through.
  If each attempt is lost independently with probability `p_loss`, then
  `P(delivered) = 1 − p_loss^(max_retries + 1)`.
- A QSDC **session** needs *all* `n_msgs` of its control messages to arrive, so
  `P(session ok) = P(delivered)^n_msgs`.

## Your task
Open `reliability.py` and complete:
1. `delivery_prob(p_loss, max_retries)` — probability one message is delivered.
2. `session_reliability(p_loss, n_msgs, max_retries)` — probability the whole session succeeds.

## Check yourself
```bash
python check_reliability.py
```
It compares your functions to the analytical formulas above. Aim for **PASS ✅**.

## Going further (optional)
Plot `session_reliability` vs `p_loss` for a few `max_retries` values — you'll see exactly how retransmissions
buy back reliability, and where it collapses.
