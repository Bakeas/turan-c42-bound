# Referee review of NOTES.md (C42 ≤ 0.6865)

*Written by a separate AI instance (Claude Code, Claude Opus 5.5) on the first draft of NOTES.md. It is not a human referee report. Gap G1, gap G2 and the minor remarks M1–M3 have since been addressed in NOTES.md.*

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

