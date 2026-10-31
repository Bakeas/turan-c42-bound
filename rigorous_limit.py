r"""
rigorous_limit.py  --  rigorous (Arb ball arithmetic) upper bound for the limit constant F(g) of a phase profile.

Profile:  g(u) = T exp(i phi(u)) on [0, 1/2],  phi piecewise linear with knots u_j = j/48 (j = 0..24), values psi_j.
Limit equation (NOTES.md, Theorem A):  d(u) = gamma - g(u) (u <= 1/2),  d(u) = gamma (u > 1/2),  gamma = g(0);
    t rho(t) = d(t) + int_0^t d(u) rho(t-u) du,                       0 < t <= 1
    p(t)     = t^(-gamma) + int_0^t (t-v)^(-gamma) rho(v) dv
    F(g)     = |p(1)| / int_0^(1/2) |p(t)| / (1-t) dt
Then limsup R_n <= max(T, F(g)).

Method (a posteriori):  rho~ = piecewise linear on the grid t_i = i/N (N = 48 M; jump allowed at t = 1/2), computed in floats
(any rho~ is allowed).  R = d + d*rho~ - t rho~.  Since |(1/t) int_0^t d(u) e(t-u) du| <= kappa ||e||, kappa = sup|d| < 1,
    ||rho - rho~||_inf <= sup|R/t| / (1 - kappa).
sup|R/t| is bounded cell by cell from the nodal values of R and a bound for R'' (R is C^2 inside each cell).
Everything below the line "rigorous part" is ball arithmetic on exact rational inputs.

The inequalities checked are (C1)-(C4), (D1)-(D3) of NOTES.md, Section 4.

Run:   python rigorous_limit.py c42_profile_0.68637.json 2560    (M = cells per knot interval; 1 to 3 minutes)
       python rigorous_limit.py c42_profile_0.6865.json 640       (version-1.0.0 profile; a few seconds)
Needs: numpy, python-flint (tested with 0.9.0)
"""
import json, math, sys, time
from fractions import Fraction
import numpy as np
from flint import acb, arb, acb_poly, arb_poly, fmpq, ctx

NK = 24                                        # knot intervals on [0, 1/2]


def exact(x):
    """exact rational value of a decimal string or of a binary float"""
    f = Fraction(x)
    return fmpq(f.numerator, f.denominator)


# ------------------------------------------------------------------ float helper: rho~ by collocation
def rho_float(T, ph, M):
    N = 2 * NK * M; h = 1 / N; H = N // 2
    beta = np.diff(ph) * 2 * NK; kn = np.arange(NK + 1) / (2 * NK); gam = T * np.exp(1j * ph[0])
    m = np.arange(N); a = m * h; j = np.minimum(m // M, NK - 1); b = beta[j]
    I0 = (np.exp(1j * b * h) - 1) / (1j * b); I1 = h * np.exp(1j * b * h) / (1j * b) - (np.exp(1j * b * h) - 1) / (1j * b) ** 2
    E = T * np.exp(1j * (ph[j] + b * (a - kn[j])))
    A = np.where(m < H, gam * h / 2 - E * (I0 - I1 / h), gam * h / 2); B = np.where(m < H, gam * h / 2 - E * I1 / h, gam * h / 2)
    def d(u, left):
        jj = min(int(u * 2 * NK), NK - 1)
        return gam - T * np.exp(1j * (ph[jj] + beta[jj] * (u - kn[jj]))) if (u < 0.5 or (u == 0.5 and left)) else gam
    rL = np.zeros(N + 1, complex); rR = np.zeros(N + 1, complex); rR[0] = -1j * T * beta[0] * np.exp(1j * ph[0])
    for i in range(1, N + 1):
        S = np.dot(A[1:i], rL[i - 1:0:-1]) + np.dot(B[:i], rR[i - 1::-1])
        rL[i] = (d(i * h, True) + S) / (i * h - A[0]); rR[i] = rL[i]
        if i == H:
            rR[i] = (gam + S + A[0] * rL[i]) / (i * h)
    return rL, rR


# ------------------------------------------------------------------ rigorous part
def check(T, ph, M, prec=192):
    t_start = time.time()
    rLf, rRf = rho_float(float(T), np.array([float(x) for x in ph]), M)
    ctx.prec = prec
    N = 2 * NK * M; H = N // 2
    h = arb(fmpq(1, N))
    Tq = exact(T); Ta = arb(Tq)
    psi = [arb(exact(x)) for x in ph]
    beta = [(psi[j + 1] - psi[j]) * (2 * NK) for j in range(NK)]
    I = acb(0, 1)
    gam = Ta * acb(0, psi[0]).exp()
    a_re = gam.real                                   # a = Re gamma
    if not (a_re < 1 and a_re > 0):
        sys.exit('FAIL: need 0 < Re(gamma) < 1')
    def cis(x):
        return acb(0, x).exp()
    def phi_at(j, u):                                 # phi on knot interval j at point u (arb)
        return psi[j] + beta[j] * (u - arb(fmpq(j, 2 * NK)))
    # ---- kappa = sup |d|:  |gamma - g(u)| = 2T|sin((phi(u)-psi0)/2)|, phi piecewise linear -> max at knots (|phi-psi0| < pi)
    devs = [abs(psi[j] - psi[0]) for j in range(NK + 1)]
    if not all(x < arb(3) for x in devs):
        sys.exit('FAIL: need |psi_j - psi_0| < 3 (< pi) for the bound on kappa')
    kappa_up = max([Ta.upper()] + [abs(2 * Ta * (x / 2).sin()).upper() for x in devs])     # exact arb points
    if not (kappa_up < 1):
        sys.exit('FAIL: need kappa < 1')
    if not all(abs(b) > 0 for b in beta):
        sys.exit('FAIL: a slope beta_j is not certainly nonzero (this program divides by beta_j)')
    bmax = max(abs(b).upper() for b in beta)
    # ---- rho~ as exact numbers
    def ex(z):
        return acb(exact(float(z.real)), exact(float(z.imag)))
    rL = [acb(0)] + [ex(z) for z in rLf[1:]]          # rL[0] unused (0)
    rR = [ex(z) for z in rRf]
    rho0 = rR[0]
    slope = [(rL[k + 1] - rR[k]) / h for k in range(N)]           # on cell k
    dS = [acb(0)] + [slope[k] - slope[k - 1] for k in range(1, N)]  # slope jumps at nodes 1..N-1
    Jmp = rR[H] - rL[H]
    # ---- moments of d on u-cells:  A_m = int d (1 - x/h),  B_m = int d x/h   (x = u - m h)
    A, B = [], []
    for m in range(N):
        if m < H:
            j = m // M; b = beta[j]; ib = I * b
            e = cis(b * h); I0 = (e - 1) / ib; I1 = h * e / ib - (e - 1) / ib ** 2
            E = Ta * cis(phi_at(j, m * h))
            A.append(gam * h / 2 - E * (I0 - I1 / h)); B.append(gam * h / 2 - E * I1 / h)
        else:
            A.append(gam * h / 2); B.append(gam * h / 2)
    # ---- d at nodes (one-sided), at cell centres (+ d', d''), at half points
    def dval(u_arb, j, der=0):
        z = Ta * cis(phi_at(j, u_arb))
        if der == 0: return gam - z
        if der == 1: return -I * beta[j] * z
        return beta[j] ** 2 * z
    dnodeL = [acb(0)] + [dval(i * h, min(i // M, NK - 1)) if i <= H else gam for i in range(1, N + 1)]
    dnodeR = [acb(0)] + [dval(i * h, min(i // M, NK - 1)) if i < H else gam for i in range(1, N + 1)]
    half = [dval((m + arb(0.5)) * h, m // M) if m < H else gam for m in range(N)]
    dhalf1 = [dval((m + arb(0.5)) * h, m // M, 1) if m < H else acb(0) for m in range(N)]
    dhalf2 = [dval((m + arb(0.5)) * h, m // M, 2) if m < H else acb(0) for m in range(N)]
    # ---- nodal residuals  R(t_i) = d(t_i) + J(t_i) - t_i rho~(t_i),   J(t_i) = sum_m A_m rL[i-m] + B_m rR[i-1-m]
    c1 = (acb_poly(A) * acb_poly(rL)).coeffs(); c2 = (acb_poly(B) * acb_poly(rR)).coeffs()
    get = lambda c, i: c[i] if 0 <= i < len(c) else acb(0)
    J = [acb(0)] + [get(c1, i) + get(c2, i - 1) for i in range(1, N + 1)]
    RL = [acb(0)] + [dnodeL[i] + J[i] - i * h * rL[i] for i in range(1, N + 1)]
    RR = [acb(0)] + [dnodeR[i] + J[i] - i * h * rR[i] for i in range(1, N + 1)]
    # ---- R'' at cell centres:  d'' + d' rho(0) + d rho'(0+) + sum_{k<=i} dS_k d(t_c - t_k) + [i>=H] Jmp d'(t_c - 1/2) - 2 slope_i
    c3 = (acb_poly(dS) * acb_poly(half)).coeffs()
    R2 = []
    for i in range(N):
        v = dhalf2[i] + dhalf1[i] * rho0 + half[i] * slope[0] + get(c3, i) - 2 * slope[i] if i < H else \
            gam * slope[0] + get(c3, i) + Jmp * dhalf1[i - H] - 2 * slope[i]
        R2.append(v)
    sumdS = sum((abs(x) for x in dS[1:]), arb(0))
    B3 = Ta * bmax ** 3 + Ta * bmax ** 2 * abs(rho0) + Ta * bmax * (abs(slope[0]) + sumdS) + abs(Jmp) * Ta * bmax ** 2
    # ---- sup |R/t| over all cells
    Rp0 = abs(-I * beta[0] * Ta * cis(psi[0]) - rho0)     # |R'(0)| = |d'(0) - rho~(0)|
    worst = Rp0 + h / 2 * (abs(R2[0]) + h / 2 * B3)
    for i in range(1, N):
        num = max(abs(RR[i]).upper(), abs(RL[i + 1]).upper()) + h * h / 8 * (abs(R2[i]) + h / 2 * B3)
        b_i = num / (i * h)
        if not b_i.is_finite():
            sys.exit('FAIL: a cell bound is not finite')
        if b_i.upper() > worst.upper():
            worst = b_i
    if not worst.is_finite():
        sys.exit('FAIL: a cell bound is not finite')
    err_rho = worst.upper() / (1 - kappa_up)
    # ---- p~ : moments of u^(-gamma) on cells
    e1, e2 = 1 - gam, 2 - gam
    pw = lambda x, s: acb(0) if x == 0 else acb(x) ** s
    S0 = [(pw(fmpq(m + 1, N), e1) - pw(fmpq(m, N), e1)) / e1 for m in range(N)]
    S1 = [(pw(fmpq(m + 1, N), e2) - pw(fmpq(m, N), e2)) / e2 for m in range(N)]
    G = [(S1[m] - m * h * S0[m]) / h for m in range(N)]
    Ew = [S0[m] - G[m] for m in range(N)]
    q1 = (acb_poly(Ew) * acb_poly(rL)).coeffs(); q2 = (acb_poly(G) * acb_poly(rR)).coeffs()
    p = lambda i: acb(fmpq(i, N)) ** (-gam) + get(q1, i) + get(q2, i - 1)
    p1 = p(N)
    one_a = 1 - a_re
    num_up = abs(p1) + err_rho / one_a
    # ---- denominator lower bound
    Ks = int(math.ceil(N / 1000))                    # t* = Ks/N ~ 0.001
    ts = arb(fmpq(Ks, N))
    Pstar = max([abs(rR[k]).upper() for k in range(Ks + 1)] + [abs(rL[k]).upper() for k in range(1, Ks + 1)])
    Pstar = arb(Pstar)
    if not ((Pstar * ts / one_a).upper() < 0.5):
        sys.exit('FAIL: near-zero lower bound (D2) is not positive; use a larger M')
    part0 = ts ** one_a / one_a - Pstar * ts ** (2 - a_re) / (one_a * (2 - a_re))
    cpow = [(arb(fmpq(m + 1, N)) ** one_a - (arb(fmpq(m, N)) ** one_a if m else arb(0))) / one_a for m in range(H + 1)]
    absdS = [arb(abs(x).upper()) for x in dS[:H + 1]]
    c4 = (arb_poly(absdS) * arb_poly(cpow)).coeffs()
    g1 = abs(gam * (gam + 1)); g2 = abs(gam) * abs(rho0); g3 = abs(slope[0])
    pv = {k: p(k) for k in range(Ks, H + 1)}
    total = part0
    for k in range(Ks, H):
        tk, tk1 = arb(fmpq(k, N)), arb(fmpq(k + 1, N))
        L0 = ((1 - tk) / (1 - tk1)).log(); L1 = (1 - tk) * L0 - h
        lin = abs(pv[k] * L0 + (pv[k + 1] - pv[k]) / h * L1)
        Q = g1 * (tk ** (-a_re - 1) - tk1 ** (-a_re - 1)) / (a_re + 1) + g2 * (tk ** (-a_re) - tk1 ** (-a_re)) / a_re \
            + g3 * (tk1 ** one_a - tk ** one_a) / one_a + (c4[k] if k < len(c4) else arb(0))
        total += lin - h * h / 8 * Q / (1 - tk1)
    corr = err_rho * 2 * arb(0.5) ** (2 - a_re) / (one_a * (2 - a_re))
    den_low = total - corr
    C = Ta                                                     # claimed constant = T
    if not (num_up.is_finite() and den_low.is_finite()):
        sys.exit('FAIL: the bounds for the numerator or the denominator are not finite')
    if not (den_low > 0):                                      # (8) needs a certainly positive denominator
        return dict(N=N, den_low=float(den_low.lower()), RESULT='FAIL: the lower bound for the denominator is not positive')
    F_up = num_up / den_low
    ok = bool(F_up < C)             # |g(u)| = T exactly by construction; den_low > 0 checked above
    return dict(N=N, a_re_gamma=float(a_re.mid()), kappa=float(kappa_up), sup_R_over_t=float(worst.upper()), err_rho=float(err_rho.upper()),
                p1=str(p1), num_up=float(num_up.upper()), den_low=float(den_low.lower()), F_up=float(F_up.upper()),
                RESULT=('PASS: F < T, hence limsup R_n <= T = ' + str(T) if ok else 'FAIL'), seconds=round(time.time() - t_start, 1))


if __name__ == "__main__":
    prof = json.load(open(sys.argv[1]))
    M = int(sys.argv[2]) if len(sys.argv) > 2 else 160
    if len(prof["phases"]) != NK + 1:
        sys.exit(f'FAIL: the profile must have exactly {NK + 1} phases')
    if str(prof.get("knots", "")).replace(" ", "") not in ("j/48", "j/48,j=0..24"):
        sys.exit('FAIL: this program assumes the knots j/48, j = 0..24')
    r = check(prof["T"], prof["phases"], M)
    for k, v in r.items():
        print(f"{k:>14}: {v}")
    sys.exit(0 if r["RESULT"].startswith("PASS") else 1)      # exit code 1 for every FAIL
