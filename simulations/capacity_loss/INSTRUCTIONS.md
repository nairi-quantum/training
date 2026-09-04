# Exercise — Channel capacity & link loss  (Simulations pod)

**Covers:** Topic 4 (Channel: loss, fading & capacity)
**You'll learn:** the two numbers every link engineer lives by — how much a channel can carry (capacity),
and how loss sets your SNR.

## Theory (short)
- **Shannon capacity** — the maximum error-free rate of a channel of bandwidth `B` at signal-to-noise ratio `SNR`:
  `C = B · log2(1 + SNR)`  (bits/s), with `SNR_linear = 10^(SNR_dB / 10)`.
- **Link budget** — the received SNR in dB is simply power minus losses minus noise:
  `SNR_rx(dB) = P_tx(dBm) − path_loss(dB) − noise_power(dBm)`.
- Together they tell you: given a transmit power and a channel loss, what rate is even possible.

## Your task
Open `capacity_loss.py` and complete:
1. `shannon_capacity(bandwidth_hz, snr_db)` — the capacity formula above.
2. `rx_snr_db(tx_power_dbm, path_loss_db, noise_power_dbm)` — the link-budget SNR.

## Check yourself
```bash
python check_capacity.py
```
Aim for **PASS**.

## The quantum bridge
Quantum channels are **loss-limited**: the achievable secret-key rate is capped by channel transmissivity
(the repeaterless PLOB bound), and Shannon capacity generalizes to **secrecy capacity**. The same dB-loss and
SNR thinking you use here is exactly how we reason about photonic links.
