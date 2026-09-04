# -*- coding: utf-8 -*-
"""Exercise: Shannon capacity and a simple link budget. Complete the TODOs."""
import math


def shannon_capacity(bandwidth_hz, snr_db):
    """Return the Shannon capacity in bits/s:  C = B * log2(1 + SNR_linear)."""
    # TODO: snr_lin = 10 ** (snr_db / 10);  return bandwidth_hz * log2(1 + snr_lin)
    return None


def rx_snr_db(tx_power_dbm, path_loss_db, noise_power_dbm):
    """Return the received SNR in dB:  P_tx - path_loss - noise_power  (all in dB / dBm)."""
    # TODO: return tx_power_dbm - path_loss_db - noise_power_dbm
    return None


if __name__ == "__main__":
    print("capacity(1 MHz, 20 dB) =", shannon_capacity(1e6, 20), "bits/s")
    print("rx SNR(0 dBm, 60 dB loss, -90 dBm noise) =", rx_snr_db(0, 60, -90), "dB")
