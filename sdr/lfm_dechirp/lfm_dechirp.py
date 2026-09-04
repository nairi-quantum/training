# -*- coding: utf-8 -*-
"""Exercise: dechirp an FMCW/LFM echo and estimate the beat frequency. Complete the TODOs."""
import numpy as np


def estimate_beat_freq(fs, B, T, tau):
    """
    Transmit an LFM chirp, receive an echo delayed by `tau`, dechirp it,
    and return the estimated beat frequency (Hz). For FMCW:  f_b = (B/T) * tau.
    """
    t = np.arange(0, T, 1 / fs)
    slope = B / T

    tx = np.exp(1j * np.pi * slope * t**2)              # transmitted chirp
    echo = np.exp(1j * np.pi * slope * (t - tau)**2)    # echo, delayed by tau

    # TODO 1 — dechirp: multiply echo by the complex conjugate of tx
    mix = None

    if mix is None:
        return None  # remove once TODO 1 is done

    # TODO 2 — FFT of mix, and the matching frequency axis:
    #   spec  = np.fft.fft(mix)
    #   freqs = np.fft.fftfreq(mix.size, 1 / fs)
    spec = None
    freqs = None

    if spec is None or freqs is None:
        return None  # remove once TODO 2 is done

    # TODO 3 — beat frequency = |freqs[k]| where |spec| is largest
    fb = None

    return None if fb is None else abs(fb)


if __name__ == "__main__":
    print("beat freq:", estimate_beat_freq(fs=1e6, B=1e7, T=1e-2, tau=3e-6), "Hz")
