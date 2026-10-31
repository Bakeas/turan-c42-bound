"""
finite_n.py  --  floating-point cross-check (NOT part of the proof).
The exact construction of NOTES.md Section 3 for finite n: K = floor(n/2), s_k = T exp(i phi(k/n)) for k <= K,
P_m = partial sums of the coefficients of exp(-sum_{k<=K} s_k x^k/k), and F_n = |P_n| / sum_{k>K} |P_(n-k)|/k.
Then R_n <= max(T, F_n).  F_n should approach the limit F of the profile (0.68636 for c42_profile_0.68637.json, 0.68620 for 0.6865).
Run:  python crosscheck/finite_n.py [profile.json]      (about a minute; needs numpy; n = 4e6 needs ~3 GB RAM)
"""
import json, os, sys, numpy as np

def _mul(a, b, N):
    m = 1 << int(np.ceil(np.log2(len(a) + len(b))))
    return np.fft.ifft(np.fft.fft(a, m) * np.fft.fft(b, m))[:N]
def _inv(f, N):
    g = np.array([1 / f[0]], complex); m = 1
    while m < N:
        m = min(2 * m, N); g = (2 * np.pad(g, (0, m - len(g))) - _mul(_mul(f[:m], g, m), g, m))[:m]
    return g
def _log(f, N):
    q = _mul(np.arange(1, N) * f[1:N], _inv(f, N), N - 1); out = np.zeros(N, complex); out[1:] = q / np.arange(1, N); return out
def _exp(h, N):
    g = np.ones(1, complex); m = 1
    while m < N:
        m = min(2 * m, N); g = np.pad(g, (0, m - len(g)))
        hm = h[:m] if len(h) >= m else np.pad(h, (0, m - len(h)))
        g = _mul(g, hm - _log(g, m) + np.eye(1, m, 0)[0], m)
    return g[:N]

if __name__ == "__main__":
    prof = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "c42_profile_0.68637.json")))
    T = float(prof["T"]); ph = np.array([float(x) for x in prof["phases"]]); kn = np.arange(25) / 48; beta = np.diff(ph) * 48
    for n in (250_000, 1_000_000, 4_000_000):
        K = n // 2; k = np.arange(1, K + 1); u = k / n; j = np.minimum((u * 48).astype(int), 23)
        S = T * np.exp(1j * (ph[j] + beta[j] * (u - kn[j])))
        hh = np.zeros(n + 1, complex); hh[1:K + 1] = -S / k
        P = np.cumsum(_exp(hh, n + 1)); kk = np.arange(K + 1, n + 1)
        print(f"n = {n:>8}: F_n = {abs(P[n]) / np.sum(np.abs(P[n - kk]) / kk):.8f}   (so R_n <= max(T, F_n) = {max(T, abs(P[n]) / np.sum(np.abs(P[n - kk]) / kk)):.6f})")
