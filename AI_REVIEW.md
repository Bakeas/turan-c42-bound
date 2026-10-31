# AI referee reviews of NOTES.md (versions 1.0.0 and 1.1.0)

*Written by a separate AI instance (Claude Code, Claude Opus 5.5). It is not a human referee report. The first part reviews version 1.0.0; its gap G1, gap G2 and minor remarks M1–M3 were addressed in version 1.1.0. The section "Version 1.1.0" at the end reviews version 1.1.0; its remarks R1–R4 and W1–W6 were addressed afterwards (R5 is on the safe side and was left as it is). A final check of those changes by the same instance found them correct and made three more small remarks (the knots field "j/480" was accepted, the wording on how `independent_check.py` stops, an old running time in a comment); these were addressed too. Line numbers in that section refer to the files it reviewed.*

Scope: NOTES.md and README.md only (Sections 1–4; Section 5 is not part of the proof).
`rigorous_limit.py`, `expected_output_M640.txt` and `crosscheck/` were **not** opened while writing this review.

Severity labels: **error** (the argument is wrong as written), **gap** (a step is missing or only
sketched, but can be filled), **minor** (wording, precision, or a harmless inaccuracy).

**Summary.** I found no mathematical error. Lemma 1, Lemma 2 and Lemma 3 are correct.
Theorem A is correct for this profile. There is one real (but easily fixed) gap: two steps of
Theorem A use $a\ge 0$, while the theorem only assumes $a<1$. The profile has $a=0.1661>0$, so the
main result is not affected. The other remarks are about presentation.

---

## Section 1 — Lemma 1 (normalization)

No issues found. Both directions are correct (renumbering is allowed because power sums are
symmetric in the $z_j$).

- *Minor (context, not checked).* The sentence "$C_{42}=\limsup R_n$" depends on how the external
  repository defines C42; that cannot be checked from these files. It does not matter for the
  claim: an upper bound for $\limsup R_n$ is also an upper bound for $\liminf R_n$ and for $\inf_n R_n$.

## Section 2 — Lemma 2 (Harcos's linearization)

- Statement, $D_n\ge 1/n$: no issues found (the term $k=n$ gives $|P_0|/n=1/n$).
- Step 1: no issues found. $\sum_{k>K}(\sigma_k/k)P_{n-k}=\lambda\sum|P_{n-k}|/k=\lambda D_n=P_n$, and $|\sigma_k|=|P_n|/D_n$.
- Step 2: no issues found. $w_0=1$, so $x^nW(1/x)$ is monic, and $W(x)=\prod(1-z_jx)$.
- Step 3: no issues found (formal logarithm respects congruences mod $x^{n+1}$).
- Step 4: no issues found. $K\ge\lfloor n/2\rfloor$ gives $2K+2\ge n+1$, so the quadratic and higher terms of the second exponential vanish mod $x^{n+1}$; the summation $\sum_{m\le n}w_m=P_n-\sum_k(\sigma_k/k)P_{n-k}$ is correct.
- *Minor.* The hypothesis $n\ge3$ is not used.

## Section 3 — the profile and Theorem A

**Definitions, construction, (1).** No issues found. For $k\le K$ we have $k/n\le 1/2$, and $|s_k|=T$.

**Statement of Theorem A.**
- **Gap (G1).** The theorem assumes only $a<1$, but two steps of the proof use $a\ge0$:
  - (B2): "Since $v^{-a}$ is decreasing" — true only for $a\ge0$;
  - Step 5: "$h_n(t)\le 2C\,t^{-a}$" uses $(\lceil nt\rceil/n)^{-a}\le t^{-a}$, true only for $a\ge0$.

  Both are easy to repair for $a<0$ (compare with left-endpoint sums; and for $a\le 0$ the function is
  simply bounded by $2C$). Simplest fix: assume $0\le a<1$ in Theorem A. **The main result is not
  affected**, since here $a=0.16611>0$ (I checked this in ball arithmetic).
- *Minor.* $\kappa<1$ already implies $a<1$: $|d|=T$ on $(\tfrac12,1]$, so $\kappa\ge T=|\gamma|>a$. The hypothesis $a<1$ is redundant.

**Bound (3).** No issues found. $|1-e^{i\theta}|\le|\theta|$ and $\varphi$ is Lipschitz with constant $\Lambda$; on $(\tfrac12,1]$, $T\le 2Tu$.

**Step 1 (discrete identities).** No issues found. I re-derived $\sum P_mx^m=\exp(\sum c_kx^k/k)$, $d_k=d(k/n)$ for all $k$ (including $k>K$, since $k>\lfloor n/2\rfloor\Rightarrow k/n>\tfrac12$), $a_j=\Gamma(j+1-\gamma)/(\Gamma(1-\gamma)j!)$, the recursion $m\delta_m=\sum d_k\delta_{m-k}$ and (5).

**Step 2 (continuous problem).**
- *Minor (M1).* $X$ should be the bounded **measurable** (e.g. Borel) functions with the sup norm, otherwise the integrals in $\mathcal K$ are not defined. With that change $X$ is a Banach space and the Neumann-series argument is correct.
- Contraction, uniqueness, $\|\rho\|\le B=M/(1-\kappa)$: no issues found.
- Continuity of $\mathcal Kf$ ($L^1*L^\infty$ is continuous): no issues found.
- Regularity of $\rho$: no issues found. $d(t)/t\to -iT\beta_0e^{i\psi_0}$; $|\mathcal K\rho|\le MBt/2$; jump only at $\tfrac12$, left-continuous.
- Function $p$: no issues found. The lower bound $|p|\ge t^{-a}(1-Bt/(1-a))$ is positive for small $t$ (for any sign of $a$), and the upper bound gives a finite denominator.

**Step 3 (convergence $\rho_n\to\rho$).**
- (6) and the uniform bound $|\rho_n(m)|\le M+\kappa B=B$: no issues found.
- Error recursion and $\max|e_m|\le\sup(|\tau_m|/t_m)/(1-\kappa)$ (induction): no issues found.
- Splitting of $\tau_m$: no issues found. I re-checked the identity, the bound $MBt_m/n$ for the last cell, the "at most two bad cells, only when $t_m>\tfrac12$" claim (jump of $d$ at $u=\tfrac12$ and of $\rho(t_m-\cdot)$ at $u=t_m-\tfrac12$), the oscillation $2\kappa B$ on bad cells, and the constant $(MB+8\kappa B)/n$.
- *Minor.* The first cell $[0,t_1]$ contains $u=0$, where $d$ is not defined. Set $d(0)=0$ (its limit); a single point does not change any integral.

**Step 4 (asymptotics of $P_j$).**
- $\eta_l$, $C_\eta<\infty$, the formula for $\Pi_n(j)$ (terms $i=0$, $i=j$, and $1\le i\le j-1$), the bound $|\Gamma(1-\gamma)|Bn^{a-1}\to0$: no issues found.
- (B2): correct for $a\ge0$, see **G1**. The constant $C$ is correct for $a\ge 0$ ($n^{a-1}\le1\le t^{-a}$ and $t^{1-a}\le t^{-a}$).
- **Gap (G2, presentation).** (B1) is a sketch. Each bullet is correct, but some details are left to the reader: (i) the cost of replacing $\rho_n(j-l)$ by $\rho((j-l)/n)$ is at most $C_\eta\max_m|e_m|/(1-a)$; (ii) the Riemann sum misses one cell of width $1/n$ near $v=t$ (contribution $O(1/n)$); (iii) the uniform convergence of the Riemann sums of $u\mapsto u^{-\gamma}\rho(t-u)$ on $[\delta,t]$ uses that $u^{-\gamma}$ is uniformly continuous on $[\delta,1]$ and that $\rho$ has one jump. All of these are routine; a referee would accept them, but writing them out would make the proof complete.

**Step 5 (conclusion).**
- Rewriting $F_n$ with $L=n-K-1=\lceil n/2\rceil-1$: no issues found ($j=n-k$).
- Numerator, the $j=0$ term, the step-function representation $h_n$, pointwise convergence, $L/n\to\tfrac12$, dominated convergence: no issues found, except the use of $a\ge0$ in the domination (**G1**). The bound $1/(1-j/n)<2$ is correct since $j\le L<n/2$.
- Final line $\limsup R_n\le\max(T,F)$: no issues found.

**Sanity check (Harcos's case).** No issues found. I re-derived $\rho=0$ on $(0,\tfrac12]$, $\rho=\gamma/t$ on $(\tfrac12,1]$ and the formula. I evaluated it independently in ball arithmetic (series $\sum_k 2^{-(w+k+1)}/(w+k+1)$): $F=0.693676303\ldots$ for $w=-0.43246-0.54237i$, as stated.

## Section 4 — the profile and the certified inequality

**Profile properties** (all re-computed by me in ball arithmetic from the JSON file):
- $a=\operatorname{Re}\gamma=0.1661094476\ldots$: correct.
- $\max_j|\psi_j-\psi_0|=0.775207\ldots<\pi$: correct (the phases are increasing).
- $\max_{(0,1/2]}|d|=2T\sin(0.775207/2)=0.518954\ldots\le0.519$: correct; hence $\kappa=T=0.6865$.
- Slopes $1.1999\le|\beta_j|\le5.8227$: correct.
- *Minor (M2).* "All slopes $\beta_j$ are nonzero" is not used anywhere in the proof. Presumably the program needs it (closed-form moments divide by $\beta$). It would be clearer to say so.

**Lemma 3.** No issues found ($e=\mathcal Ke+R/t$, $e$ bounded).
- *Minor (M3).* The sup is pointwise, so at $t=\tfrac12$ (where $\tilde\rho$ jumps) a convention for $\tilde\rho(\tfrac12)$ is needed. (C1) evaluates both one-sided values $R(t_H^\pm)$, which covers either convention. (Since only integrals of $e$ enter $p$, an ess-sup version would also suffice.)

**Bound (8).** No issues found ($|p-\tilde p|\le\varepsilon\int_0^t(t-v)^{-a}dv$).

**Description of the program (C1)–(D3).** I checked the mathematics of each step (not the code):
- Grid ($N=48M$ makes all knots and $\tfrac12$ grid points): no issues found.
- (C1): no issues found (moments against the two hat functions give an exact discrete convolution).
- (C2): no issues found. I re-derived the formula independently by writing
  $\tilde\rho(v)=\tilde\rho(0)+\sigma_0v+\sum_k\Delta_k(v-t_k)_++J\,\mathbf 1_{v>1/2}$, which gives
  $\int_0^td(t-v)\tilde\rho(v)dv=\tilde\rho(0)D_1(t)+\sigma_0D_2(t)+\sum_k\Delta_kD_2(t-t_k)+JD_1(t-\tfrac12)$ with $D_1'=d$, $D_2'=D_1$.
- (C3): no issues found ($|d^{(r)}|=T|\beta_j|^r$ on each piece, $d'=0$ on $(\tfrac12,1]$, and the $-2\sigma_i$ term has zero derivative).
- (C4): no issues found. For complex-valued $R$ the Rolle form of the interpolation error is not valid, but the Peano-kernel form is (the kernel has one sign), as the text says. The cell-0 bound $|R/t|\le|R'(0^+)|+\tfrac h2\sup|R''|$ and $R'(0^+)=d'(0)-\tilde\rho(0)$ are correct.
- (D1): no issues found.
- (D2): no issues found. *Minor:* the positivity check is not actually needed, because $|\tilde p|/(1-t)\ge|\tilde p|\ge t^{-a}-P_*t^{1-a}/(1-a)$ holds even where the right side is negative.
- (D3): no issues found. The bound $\int_{\rm cell}|\tilde p-L|\le\frac{h^2}8\int_{\rm cell}|\tilde p''|$ is correct for $\tilde p\in W^{2,1}$ (the Peano kernel integrates to $(s-a)(b-s)/2\le h^2/8$); $\tilde p''$ is correct and its singular terms $(t-t_k)^{-a}$ are integrable. The bound $\int_0^{1/2}t^{1-a}/((1-a)(1-t))\le 2\cdot2^{a-2}/((1-a)(2-a))$ is correct.
- Output table: internally consistent: $\varepsilon=\sup|R/t|/(1-T)$ (6.76e-6/0.3135 = 2.16e-5; 1.69e-6/0.3135 = 5.39e-6). The ratio of the *rounded* displayed values, 0.391133/0.569980 = 0.686222, differs from the stated 0.686221 only in the last digit (rounding of the displayed numbers). The actual program output (section "Comparison" below), 0.3911324677 / 0.5699807818 = 0.6862204, agrees with the table.

## Overall verdict

The reduction (Lemma 2), the limit theorem (Theorem A) and the a posteriori bound (Lemma 3, (8)) are
correct. The only thing that needs fixing is **G1** (add $a\ge0$ to Theorem A, or repair two lines);
it does not affect the result for this profile. **G2** is a presentation issue. The truth of the
main claim then depends only on the certified inequality $F<0.6865$, which I checked independently
(next section).

## Comparison: independent checker vs `rigorous_limit.py`

`independent_check.py` was written from NOTES.md only, before opening `rigorous_limit.py`.
Same a-posteriori principle (Lemma 3 and (8)), but a different implementation:
- convolutions through the "ramp" form $\tilde\rho=\tilde\rho(0)+\sigma_0v+\sum\Delta_k(v-t_k)_++J\mathbf 1_{v>1/2}$ and the closed forms $D_1,D_2,G_1,G_2$ (instead of hat-function moments);
- $\sup_{\rm cell}|R''|$ by an interval enclosure on each cell (instead of the centre value plus a global $B_3$);
- $\kappa=T$ verified via $|d|\le T\max_j|\psi_j-\psi_0|$ with $\max_j|\psi_j-\psi_0|<1$;
- near-zero cut $t_*=8h$ (instead of $\approx10^{-3}$); the $\varepsilon$-correction via $1/(1-t)\le1+2t$.

Tested first on small grids (M = 2, 10, 40, 80: FAIL as expected; M = 160: PASS, 0.686430).
Also tested on Harcos's constant-phase profile, where the exact value is known (0.6936763):
it gives upper bounds 0.6937682 (M=40) and 0.6937030 (M=160), above the true value and converging to it.

Results at M = 640 (N = 30720), python-flint 0.9.0, 192 bits:

| quantity | `independent_check.py` | `rigorous_limit.py` |
|---|---|---|
| $\sup\lvert R/t\rvert$ | 1.6914e-6 (worst cell at $t=1/48$) | 1.6915e-6 |
| $\varepsilon$ | 5.3953e-6 | 5.3955e-6 |
| $\tilde p(1)$ | 0.2459093205407 − 0.3041515278788 i | 0.2459093205407 − 0.3041515278788 i |
| upper bound for $\lvert p(1)\rvert$ | 0.3911325 | 0.3911325 |
| lower bound for $\int_0^{1/2}\lvert p\rvert/(1-t)$ | 0.5699833 | 0.5699808 |
| **upper bound for F** | **0.6862175** | **0.6862204** |
| result | PASS | PASS |
| time | 3.9 s | 7.8 s |

The two bounds agree to $3\cdot10^{-6}$; mine is a little smaller only because of the smaller
near-zero cut $t_*$. `rigorous_limit.py` reproduces `expected_output_M640.txt` (F_up = 0.6862204484).
Both are well below $T=0.6865$ (margin $2.8\cdot10^{-4}$).


---

# Version 1.1.0

Review of the version received on 31 Oct 2026 (claim $C_{42}\le0.68637$, profile `c42_profile_0.68637.json`).
All runs: Windows 10, python-flint 0.9.0, numpy, Python from the `c7` environment.

**What changed since the version reviewed above.** I compared every file with the copies I had read
in the first review:
- `NOTES.md`, `README.md`, `rigorous_limit.py`: changed (reviewed below).
- `independent_check.py`: only the three lines after the imports (`if not __debug__: sys.exit(...)`) were added. Nothing else changed (checked with `diff` against the file I wrote).
- `c42_profile_0.6865.json`: unchanged. `expected_output_M640.txt`: only the line `seconds` changed (5.2 → 5.1).
- New files: `c42_profile_0.68637.json`, `expected_output_0.68637_M2560.txt`, `expected_independent_0.68637_M2560.txt`, `AI_REVIEW.md`, `CITATION.cff`.
- `AI_REVIEW.md` is the part of this file above (the review of version 1.0.0), with one added header line. That line is accurate: G1, G2 and M1–M3 are now addressed in `NOTES.md` (checked in item 4).

**Summary.**
- Both programs print PASS for the new profile: $F\le0.6863615$ (`independent_check.py`, $M=2560$) and $F\le0.6863660$ (`rigorous_limit.py`, $M=2560$). Both are below $T=0.68637$, but the margin is only about $4\cdot10^{-6}$ to $9\cdot10^{-6}$.
- The fix works: `pinho_bug.json` now gives FAIL. Version 1.0.0 gave PASS with "$F\le-2.73$".
- In both programs, PASS is printed only when every hypothesis has been checked, and no check can be removed by `python -O`. I found no input that gives a false PASS. I list five robustness remarks (R1–R5). None of them leads to a false statement about $C_{42}$.
- All the profile facts in Section 4 are correct (recomputed in ball arithmetic), and so is the SHA-256.
- Every number in the changed text matches the program outputs. The new proof text (Theorem A with $a\ge0$, the full (B1)) is correct. I have only small wording remarks (W1–W6).

## 1. Runs on `c42_profile_0.68637.json`

| | `independent_check.py`, $M=1280$ | `independent_check.py`, $M=2560$ | `rigorous_limit.py`, $M=1280$ | `rigorous_limit.py`, $M=2560$ |
|---|---|---|---|---|
| $N$ | 61 440 | 122 880 | 61 440 | 122 880 |
| $\sup\lvert R/t\rvert$ | 4.2169e-7 | 1.0546e-7 | 4.2170e-7 | 1.05464e-7 |
| $\varepsilon$ | 1.3446e-6 | 3.3626e-7 | 1.3446e-6 | 3.36268e-7 |
| upper bound for $\lvert p(1)\rvert$ | 0.3913028 | 0.3913016 | 0.39130280 | 0.39130159 |
| lower bound for the denominator | 0.5701092 | 0.5701101 | 0.57010586 | 0.57010638 |
| **upper bound for F** | **0.6863646956** | **0.6863614529** | **0.6863686636** | **0.6863659160** |
| result | PASS | PASS | PASS | PASS |
| time on this machine | 10 s | 23 s | 20 s | 129 s |

- The near-zero cut of `independent_check.py` at $M=2560$ is $t_*=13h\approx1.1\cdot10^{-4}$ (`rigorous_limit.py`: $123h\approx1.0\cdot10^{-3}$). The worst cell is the one just after the first knot ($t=1/48$) in both programs.
- `rigorous_limit.py` at $M=2560$ reproduces `expected_output_0.68637_M2560.txt` in `num_up`, `den_low` and `F_up` (all printed digits). `sup_R_over_t` and `p1` differ only after about 11 significant digits. The reason is that the floating-point $\tilde\rho$ is slightly different on this machine, which is allowed ($\tilde\rho$ may be any function). The same holds for `independent_check.py` against `expected_independent_0.68637_M2560.txt` (only `p~(1)` after 15 digits, and the times, differ).
- Time: on this machine `rigorous_limit.py` at $M=2560$ needed 2 min 9 s. The expected file says 45.5 s and the README says "about 1 minute". Users of slower machines should expect a few minutes.

## 2. The fix (Ricardo Pinho's example), and when PASS can be printed

**Test.** `pinho_bug.json` (the line given by the author), saved outside the folder, $M=2$:

| program | output |
|---|---|
| `rigorous_limit.py` 1.1.0 | `den_low: -18.6227...`, `RESULT: FAIL: the lower bound for the denominator is not positive` |
| `rigorous_limit.py` 1.1.0 with `python -O` | the same FAIL |
| `rigorous_limit.py` 1.0.0 (my copy of the old file) | `den_low: -18.6227...`, `F_up: -2.7313`, `RESULT: PASS` (the bug) |
| `independent_check.py` | $M=2$: stops (assert $\lvert\beta h\rvert<\tfrac12$; here $\lvert\beta\rvert$ is up to 76.8); $M=4,8,40,160$: FAIL with $F\le5.03,\ 1.68,\ 1.149,\ 1.1304$ |
| `independent_check.py` with `python -O` | stops at once: "run this program without python -O" (exit code 1) |

For this profile the true value is $F\approx1.12915$ (`crosscheck/limit_direct.py`, $N=16000$). So a PASS would have claimed something false. At larger $M$, `rigorous_limit.py` also gives an honest FAIL ($M=8,40,160$: `den_low` $=0.155,\ 1.618,\ 1.677$, `F_up` $=36.0,\ 1.269,\ 1.138$).

**Code audit of `rigorous_limit.py` 1.1.0.** There is no `assert` left in the file (checked with grep). The hypotheses that the bound uses, and where they are checked:

| hypothesis | where | what happens if it fails | tested with |
|---|---|---|---|
| $0<a<1$ | line 70 | `sys.exit('FAIL: ...')` | $T=0.6$, $\psi_0=2$ |
| $\lvert\psi_j-\psi_0\rvert<3$ (needed for "$\lvert d\rvert$ is largest at a knot") | line 78 | `sys.exit('FAIL: ...')` | phases from 0 to 3.5 |
| $\kappa<1$ (with $\kappa\le\max(T,\max_j2T\lvert\sin((\psi_j-\psi_0)/2)\rvert)$) | lines 80–82 | `sys.exit('FAIL: ...')` | $T=1.2$ |
| positivity in (D2) | line 155 | `sys.exit('FAIL: ...')` | $T=0.99$, $a=0.99$ |
| lower bound for the denominator certainly $>0$ | line 174 | returns `RESULT='FAIL: ...'` | `pinho_bug.json` |
| $F_{\rm up}<T$ certainly | line 177 | `RESULT: FAIL` | $T=0.68$ with the 1.0.0 phases |

All of these are ordinary `if` tests on Arb balls, which are true only when certainly true, so `python -O` cannot remove them. The text `PASS` appears only on line 180, and only when `ok` is true, which needs all six. The quantities that are not tested are true by construction: $\lvert g\rvert=T$, and the knots and $\tfrac12$ are grid points because $N=48M$. I also re-read the rigorous part line by line (moments $A_m,B_m$, nodal residuals, $R''$ and $B_3$, the cell bounds, $\tilde p$, (D2), (D3), the $\varepsilon$-corrections). It agrees with (C1)–(D3) and with my own derivation.

**`independent_check.py`.** Its checks are `assert`s: $\lvert\psi_j-\psi_0\rvert<1$ (so $\kappa=T$), $T<1$, $0<a<1$, 25 phases, $\lvert\beta_jh\rvert<\tfrac12$ (series tail), equal one-sided values of $\tilde\rho$ except at $\tfrac12$, and the denominator lower bound $>0$ (line 254; it was there already in version 1.0.0). Under `python -O` the new lines 37–38 stop the program before any computation (tested). So here too PASS needs every check.

**Other ways a bad profile could get a false PASS.** I found none. Remarks R1–R5 are about robustness. None of them can make either program certify a false inequality for the profile it actually computes with.
- **R1 (NaN in the maximum over cells, both programs).** `rigorous_limit.py` (line 135, `if b_i.upper() > worst.upper()`) and `independent_check.py` (line 209, `max(..., key=...)`) skip a cell whose bound is NaN, because comparisons with NaN are false. I could not reach this case. The only NaN source is a zero slope (division by $i\beta_j$ in `rigorous_limit.py`), and that also makes the floating-point $\tilde\rho$ NaN, so the program stops with `ValueError` (tested). In `independent_check.py` a NaN in $\tilde\rho$ stops at the assert $\tilde\rho^-_i=\tilde\rho^+_i$, and a NaN would also reach $\tilde p(1)$. Still, one line (`if not worst.is_finite(): FAIL`) would make this airtight.
- **R2 (extra phases, `rigorous_limit.py`).** The program uses only the first 25 phases and ignores the rest. With a 26th value added to the 1.0.0 profile it still prints PASS (tested, $M=320$). The certified statement is then about the first 25 values, so the claim stays true, but the file says something different from what was checked. Suggestion: FAIL unless there are exactly 25 phases (`independent_check.py` already asserts this).
- **R3 (the "knots" field, both programs).** Neither program reads it. Both assume $j/48$, as NOTES.md defines. Same comment as R2.
- **R4 (exit code, both programs).** FAIL sometimes ends with exit code 0: in `rigorous_limit.py` for a non-positive denominator and for $F_{\rm up}\ge T$, and in `independent_check.py` for $F_{\rm up}\ge T$. A script that tests only the exit code would take such a FAIL for success. Suggestion: `sys.exit(1)` after every FAIL.
- **R5 (the (D2) check is stricter than needed, `rigorous_limit.py`).** For the test profile $T=0.99$, $\psi_0=0$, $\psi_j\in\{0.95,0.96\}$ ($a=0.99$), `rigorous_limit.py` gives FAIL at every $M$, because $t_*\approx10^{-3}$ does not shrink. `independent_check.py` gives PASS ($F\le0.5723$ at $M=40$, $F\le0.4283$ at $M=160$), and floating point gives $F\approx0.41838$. This errs on the safe side, so it is not a soundness problem; the positivity is not needed mathematically (see (D2) in the first review).
- A zero slope $\beta_j=0$ makes `rigorous_limit.py` stop with a `ValueError` instead of a clean FAIL (safe). `independent_check.py` handles $\beta_j=0$ (power series; for example Harcos's constant-phase profile).

## 3. Profile facts, recomputed in ball arithmetic

My own script reads the file as bytes, parses each decimal string as an exact rational, and works at 256 bits.

| fact (NOTES.md, Section 4) | my value | verdict |
|---|---|---|
| SHA-256 of `c42_profile_0.68637.json` | `dcea4edbec1d5935f2f04d4d1b5b8379e2d2d7d78072a1f089c7abbe11ded395` (688 bytes, LF line ends) | matches |
| $a=\operatorname{Re}\gamma=0.16609\ldots\in(0,1)$ | $[0.166099900545702\pm5\cdot10^{-16}]$ | correct |
| $\max_j\lvert\psi_j-\psi_0\rvert=0.7753<\pi$ | $[0.775291147613909\pm4\cdot10^{-16}]$, at $j=24$ (the phases increase) | correct |
| $\lvert d\rvert\le0.5190$ on $(0,\tfrac12]$ | knot formula $2T\sin(0.775291/2)=0.518909081\ldots$; direct enclosure over 48 000 sub-intervals (no monotonicity argument used): $\sup\lvert d\rvert\le0.518909083$ | correct |
| $\kappa=T=0.68637<1$ | $\sup_{(0,1/2]}\lvert d\rvert<T$ and $\lvert d\rvert=T$ on $(\tfrac12,1]$ | correct |
| $1.20\le\lvert\beta_j\rvert\le5.82$, all nonzero | $\min=1.2001916941\ldots$ ($j=11$), $\max=5.8165451538\ldots$ ($j=0$); all $\beta_j>0$ | correct (the lower bound holds with a margin of only $2\cdot10^{-4}$) |

- The hash is that of the file with LF line ends. A Git checkout on Windows with `core.autocrlf=true` would change the bytes and therefore the hash. A `.gitattributes` line such as `*.json -text` would prevent this.
- For comparison, the 1.0.0 profile has $1.1999\le\lvert\beta_j\rvert\le5.8227$. That is consistent with the old text "$1.19\le\lvert\beta_j\rvert\le5.83$", and the new text correctly uses new numbers.

## 4. Review of the changes in NOTES.md and README.md

**Versions paragraph (NOTES.md).** Correct. Each statement was checked: the bug, the false PASS of 1.0.0 (reproduced above), the new FAIL, "about 0.570" for both profiles (0.5701064 and 0.5699808), and "`independent_check.py` already made this check" (its line 254, present in 1.0.0).
- **W1.** "The proof is the same for both" is true for the mathematics, but the text of the proof did change in 1.1.0. Theorem A now assumes $a\ge0$ instead of $a<1$, $X$ consists of measurable functions, $d(0)=0$ is a stated convention, Lemma 2 holds for $n\ge2$, (B1) is written out in full, and (C4) has a remark on $\tilde\rho(\tfrac12)$. The paragraph on the second checker says so, but the Versions paragraph does not. Suggestion: add one sentence to Versions. The README's Versions list also does not mention the fix; a short "fixes a bug in `rigorous_limit.py`, see NOTES.md" would help.

**Changed proof text** (reviewed like the rest of the proof):
- Lemma 2 and the construction with $n\ge2$: no issues found ($2K+2>n$ for every $K\ge\lfloor n/2\rfloor$; for $n=2$, $K=1$ and $D_2=\tfrac12$).
- $d(0)=0$: no issues found.
- Theorem A, "assume $\kappa<1$ and $a\ge0$; then $a\le\lvert\gamma\rvert=T\le\kappa<1$": no issues found. This closes **G1**: (B2) and the bound $h_n\le2Ct^{-a}$ in Step 5 are now valid.
- $X$ = bounded Borel-measurable functions: no issues found (M1).
- (B1), the new proof: no issues found in the argument. I checked items 1–6 and the final estimate $2C_\eta B\delta^{1-a}/(1-a)$. This closes **G2**.
  - **W2 (minor).** In item 6 the first cell of the sum, $(\lfloor\delta n\rfloor/n,(\lfloor\delta n\rfloor+1)/n]$, can reach below $\delta$. So on the cells, $\lvert u^{-\gamma}\rvert$ is bounded by $(\delta/2)^{-a}$, not $\delta^{-a}$ (in the oscillation bound and in the jump-cell bound $2\delta^{-a}B$). This needs $n\ge2/\delta$, which is implicit. It is harmless, because these terms carry a factor $\omega(1/n)$ or $1/n$.
- **W3.** Section 4, the slopes: "needed only by the program" — there are now two programs. Only `rigorous_limit.py` divides by $\beta_j$; `independent_check.py` does not need $\beta_j\ne0$.
- (C4), the new bullet on $\tilde\rho(\tfrac12)$: correct (M3).

**The sentence on when PASS is printed.** Correct, and it matches the code (item 2).
- **W4.** The list of checked hypotheses could also name $\lvert\psi_j-\psi_0\rvert<3$, which the bound for $\kappa$ needs.

**The tables (Section 4).** Every entry agrees with the program outputs, rounded:
- 0.68637, $M=1280$: 4.2170e-7 → "4.22e-7", 1.3446e-6 → "1.35e-6", 0.39130280 → "0.391303", 0.57010586 → "0.570105", 0.68636866 → "0.6863687"; the PASS is correct.
- 0.68637, $M=2560$: 1.0546e-7 → "1.06e-7", 3.3627e-7 → "3.37e-7", 0.39130159 → "0.391302", 0.57010638 → "0.570106", 0.68636592 → "0.6863660". The PASS is correct.
- 0.6865, $M=320$ (run again here): 6.7563e-6 → "6.76e-6", 2.1551e-5 → "2.16e-5", 0.39115183 → "0.391152", 0.56997322 → "0.569973", 0.68626352 → "0.686264". The PASS is correct.
- 0.6865, $M=640$: as in the first review. The PASS is correct.
- The margin "$T-F\ge4\cdot10^{-6}$": $0.68637-0.6863659160=4.08\cdot10^{-6}$. Correct.
- **W5 (minor).** The new tables round in the safe direction: upper bounds up and lower bounds down (1.0546e-7 → 1.06e-7, 1.3446e-6 → 1.35e-6, 0.57010586 → 0.570105, 0.68636592 → 0.6863660). The 1.0.0 table has one entry rounded down, $\sup\lvert R/t\rvert$ 1.6915e-6 → "1.69e-6" (already so in 1.0.0). Harmless.

**The paragraph on the second checker.** All statements are correct:
- written from NOTES.md only, before `rigorous_limit.py` was opened;
- the three listed differences;
- $0.6863647$ and $0.6863615$ (my 0.6863646956 and 0.6863614529, rounded up);
- $0.6863687$ and $0.6863660$ for `rigorous_limit.py`;
- agreement on $\sup\lvert R/t\rvert$ to four digits (4.2169e-7 against 4.2170e-7 at $M=1280$, 1.0546e-7 against 1.05464e-7 at $M=2560$);
- agreement on $\lvert p(1)\rvert$ to seven decimals;
- the smaller bounds are due to the smaller cut: my denominator bound is 0.5701101 against 0.5701064, and almost all of the difference comes from $[0,t_*]$;
- $0.6862175$ against $0.6862204$ for the 1.0.0 profile;
- Harcos's case, with upper bounds 0.6937682 ($M=40$) and 0.6937030 ($M=160$) above 0.6936763;
- the list of incorporated remarks.

One honest caveat that the text could add: the two programs are independent *code*, written by two AI instances, but they use the same mathematical route (Lemma 3 and (8)). A shared mistake in Lemma 3 or (8) would not be caught by running both. I re-derived Lemma 3 and (8) by hand in the first review and found them correct.

**Section 5 (not part of the proof).**
- Direct solver: correct. `crosscheck/limit_direct.py` prints 0.6863600809 ($N=16000$) for the new profile ("0.68636008"), 0.6862011165 for the 1.0.0 profile ("0.68620112"), and 0.69367605 for Harcos's case ("0.693676").
- Finite $n$: correct. `crosscheck/finite_n.py` prints 0.68641645, 0.68637834 and 0.68636596 for $n=2.5\cdot10^5,\ 10^6,\ 4\cdot10^6$ ("0.6864165, 0.6863783, 0.6863660"; 15 s here). The values decrease towards 0.68636.
- The checker's error bound: correct. For $M=40$ the cell bound of `rigorous_limit.py` is $\sup\lvert R/t\rvert\le4.2241\cdot10^{-4}$ ("4.22e-4"); mine is $4.2215\cdot10^{-4}$. My own evaluation of the true $\lvert R/t\rvert$ (Gauss–Legendre on every smooth piece, 300 points per cell, with the $\tilde\rho$ of `rigorous_limit.py`) gives $4.1660\cdot10^{-4}$ in the worst cell, just after $t=1/48$ ("4.17e-4"). In 10 other sampled cells the true value is $\le3.9\cdot10^{-4}$.
- **W6.** On "the best value of this family" (0.6863655 with 24 equal pieces): I cannot reproduce the optimization, so this is not checked. The wording can confuse readers, because this very profile already has $F\approx0.6863601<0.6863655$. Presumably 0.6863655 is the best value of $\max(T,F)$, reached where $F=T$, so it would help to say so. "Within $10^{-5}$": $0.68637-0.6863655=4.5\cdot10^{-6}$. Correct.

**Acknowledgement.** No issues found. It agrees with the Versions paragraph.

**README.md.**
- Every number agrees with the outputs: 0.68637, 0.6863660, 0.6863615, the commands, the two expected files, 0.68636 for finite $n$, and Harcos's 0.693676.
- The times ("about 1 minute", "about 30 seconds") depend on the machine. Here they were 129 s and 23 s.
- The files table calls `independent_check.py` "written independently from NOTES.md only". Adding "by a separate AI instance" would match NOTES.md and the AI-use section.
- `CITATION.cff` (not asked, but checked): version 1.1.0 and the bound 0.68637 agree.

## Verdict for version 1.1.0

The proof (with the text changes of 1.1.0) is correct as far as I can check. Gaps G1 and G2 of the first review are closed. Both programs certify $F<0.68637$ for `c42_profile_0.68637.json`, with independent code and with bounds 0.6863615 and 0.6863660. Hence $\limsup R_n\le0.68637$, given Theorem A. The bug found by Ricardo Pinho is fixed. In both programs PASS now needs every hypothesis, checked by tests that `python -O` cannot remove. The remaining remarks (R1–R5, W1–W6) are about robustness and wording; none of them affects the claim.
