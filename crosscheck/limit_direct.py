"""
limit_direct.py  --  floating-point cross-check (NOT part of the proof).
Solves  t p(t) = int_0^t c(u) p(t-u) du  (c = 1 - g on [0,1/2], c = 1 after) directly by product integration,
with p = t^(-gamma) q(t), and prints F = |p(1)| / int_0^(1/2) |p| dt/(1-t).
Test 1: constant phase (Harcos), known value 0.693676.   Test 2: a profile (default c42_profile_0.68637.json, or the file given as argument).
Run:  python crosscheck/limit_direct.py [profile.json]      (seconds; needs numpy)
"""
import json, os, sys, numpy as np

def solve(gfun, N):
    h = 1.0 / N; gam = gfun(0.0)
    k = np.arange(N + 1); u = k * h
    cL = 1 - gfun(np.minimum(u, 0.5)); cR = cL.copy()
    cL[u > 0.5 + 1e-12] = 1; cR[u > 0.5 - 1e-12] = 1
    s = u.astype(complex); e1, e2 = 1 - gam, 2 - gam
    P1 = np.where(k > 0, s ** e1, 0); P2 = np.where(k > 0, s ** e2, 0)
    M0 = (P1[1:] - P1[:-1]) / e1; M1 = (P2[1:] - P2[:-1]) / e2
    w0 = (s[1:] * M0 - M1) / h; w1 = (M1 - s[:-1] * M0) / h
    q = np.zeros(N + 1, complex); q[0] = 1.0
    for i in range(1, N + 1):
        S = np.dot(w0[:i], cL[i:0:-1] * q[:i])
        if i > 1: S += np.dot(w1[:i - 1], cR[i - 1:0:-1] * q[1:i])
        q[i] = S / (P1[i] - w1[i - 1] * cR[0])
    a = gam.real; H = N // 2; t = u[:H + 1]; f = np.abs(q[:H + 1]) / (1 - t)
    R1 = np.where(t > 0, t ** (1 - a), 0); R2 = np.where(t > 0, t ** (2 - a), 0)
    m0 = (R1[1:] - R1[:-1]) / (1 - a); m1 = (R2[1:] - R2[:-1]) / (2 - a)
    den = np.sum((t[1:] * m0 - m1) / h * f[:-1] + (m1 - t[:-1] * m0) / h * f[1:])
    return abs(q[N]) / den

if __name__ == "__main__":
    w = -0.43246 - 0.54237j
    print("Harcos (constant phase), F =", "%.8f" % solve(lambda x: -w + 0 * np.asarray(x), 4000), " (expected 0.693676)")
    prof = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "c42_profile_0.68637.json")))
    T = float(prof["T"]); ph = np.array([float(x) for x in prof["phases"]]); kn = np.arange(25) / 48
    g = lambda x: T * np.exp(1j * np.interp(x, kn, ph))
    for N in (4000, 8000, 16000):
        print(f"profile T = {T}, N = {N:>5}: F = {solve(g, N):.10f}")
