# C42 ≤ 0.68637: proof and computer verification

**Main result.** For Turán's pure power sum problem,
$$\limsup_{n\to\infty} R_n \;\le\; 0.68637 ,\qquad R_n=\inf_{z_1=1,\;z_2,\dots,z_n\in\mathbb C}\ \max_{1\le k\le n}\ \Bigl|\sum_{j=1}^n z_j^k\Bigr| .$$

**Status.** Not peer reviewed; written with AI assistance (see the end of the file).

**Versions.**
- Version 1.1.0 (31 Oct 2026) proves the bound $0.68637$ with the profile `c42_profile_0.68637.json`. It also fixes a bug in `rigorous_limit.py`, found by Ricardo Pinho: version 1.0.0 did not check that the lower bound for the denominator in (8) is positive, so a profile for which that bound is negative could get a false `PASS`. The program now prints `FAIL` in that case. For both profiles in this repository the bound is about $0.570$, so their results are not affected. `independent_check.py` already made this check.
- Version 1.0.0 (30 Oct 2026) proved the weaker bound $0.6865$ with the profile `c42_profile_0.6865.json`. That profile is kept in the repository, and its numbers are also given in Section 4.

The mathematics of the proof is the same for both. In version 1.1.0 its text was made more complete, following the first review in `AI_REVIEW.md`: Theorem A now assumes $a\ge0$, $X$ consists of measurable functions, $d(0)=0$ is a stated convention, Lemma 2 is stated for $n\ge2$, the proof of (B1) is written out in full, and (C4) has a remark on the value $\tilde\rho(\frac12)$. After the second review (also in `AI_REVIEW.md`), both programs were made stricter on their input: they also stop if the profile does not have exactly 25 phases with the knots $j/48$, or if a computed bound is not finite (`rigorous_limit.py` with a `FAIL` message, `independent_check.py` with an `AssertionError`). In both programs every failure now ends with exit code 1. These checks do not change any number.

**What the proof consists of:**
- A complete proof of a limit theorem (Theorem A below).
- One inequality, $F < 0.68637$, about the solution of an explicit integral equation. This inequality is verified in ball arithmetic (Arb, via python-flint) by two independently written programs, `rigorous_limit.py` and `independent_check.py`. Their outputs are $F\le0.6863660$ and $F\le0.6863615$.

No other unverified step is used.

Notation: $s_k(z)=\sum_j z_j^k$. Powers $t^{w}$ with $t>0$, $w\in\mathbb C$ mean $e^{w\log t}$.

---

## 1. Normalization

**Lemma 1.** Let $R'_n$ be the infimum of $\max_{k\le n}|s_k(z)|$ over all $z\in\mathbb C^n$ with $\max_j|z_j|=1$. Then $R'_n=R_n$. In particular $C_{42}=\limsup R_n$ in either normalization.

*Proof.*
- ($R_n\le R'_n$.) If $\max_j|z_j|=|z_{j_0}|=1$, put $w_j=z_j/z_{j_0}$. Then $w_{j_0}=1$, and $s_k(w)=z_{j_0}^{-k}s_k(z)$ has the same modulus as $s_k(z)$.
- ($R'_n\le R_n$.) If $z_1=1$, let $\lambda=\max_j|z_j|=|z_{j_0}|\ge1$ and put $w_j=z_j/z_{j_0}$. Then $\max_j|w_j|=1$ and $|s_k(w)|=\lambda^{-k}|s_k(z)|\le|s_k(z)|$. $\square$

## 2. The construction for a fixed n (Harcos's linearization)

For complex numbers $s_1,\dots,s_K$, define the formal power series
$$A(x)=\exp\Bigl(-\sum_{k=1}^{K}\frac{s_k}{k}x^k\Bigr)=\sum_{m\ge0}\alpha_m x^m,\qquad P_m=\alpha_0+\dots+\alpha_m\quad\Bigl(\text{so }\sum_m P_mx^m=\frac{A(x)}{1-x}\Bigr).$$

**Lemma 2.** Let $n\ge2$ and $\lfloor n/2\rfloor\le K<n$. Let $s_1,\dots,s_K\in\mathbb C$, and put $D_n=\sum_{k=K+1}^{n}|P_{n-k}|/k$; note $D_n\ge 1/n>0$ because $P_0=1$. Then there are $z_1=1,z_2,\dots,z_n\in\mathbb C$ such that
- $s_k(z)=s_k$ for $1\le k\le K$;
- $|s_k(z)|=|P_n|/D_n$ for $K<k\le n$.

Consequently $R_n\le\max\bigl(\max_{k\le K}|s_k|,\ |P_n|/D_n\bigr)$.

*Proof.*

**Step 1: choose the remaining power sums.** For $K<k\le n$ put $\sigma_k=\lambda u_k$, where $\lambda=P_n/D_n$, and $u_k=\overline{P_{n-k}}/|P_{n-k}|$ if $P_{n-k}\ne0$, $u_k=1$ otherwise. Put $\sigma_k=s_k$ for $k\le K$. Then
$$\sum_{k=K+1}^{n}\frac{\sigma_k}{k}P_{n-k}=\lambda D_n=P_n .$$

**Step 2: build the tuple.** Let $W(x)=\sum_{m=0}^n w_mx^m$ be the truncation to degree $\le n$ of $\exp(-\sum_{k=1}^n\sigma_kx^k/k)$. Since $w_0=1$, the polynomial $x^nW(1/x)$ is monic of degree $n$. Call its roots (with multiplicity) $z_1,\dots,z_n$. Then $W(x)=\prod_j(1-z_jx)$.

**Step 3: the power sums are the $\sigma_k$.** Taking logarithms of power series with constant term 1 gives $-\sum_k s_k(z)x^k/k\equiv-\sum_{k\le n}\sigma_kx^k/k \pmod{x^{n+1}}$. So $s_k(z)=\sigma_k$ for all $k\le n$.

**Step 4: $W(1)=0$.**
- Every product of two monomials $x^k,x^{k'}$ with $k,k'\ge K+1$ has degree $\ge2K+2>n$. Hence, modulo $x^{n+1}$,
$$\exp\Bigl(-\sum_{k\le n}\frac{\sigma_k}{k}x^k\Bigr)\equiv A(x)\Bigl(1-\sum_{k=K+1}^n\frac{\sigma_k}{k}x^k\Bigr).$$
- Comparing coefficients, $w_m=\alpha_m-\sum_{K<k\le m}(\sigma_k/k)\alpha_{m-k}$.
- Summing over $m\le n$,
$$W(1)=P_n-\sum_{k=K+1}^n(\sigma_k/k)P_{n-k}=0 .$$

So $1$ is one of the $z_j$; renumber so that $z_1=1$. $\square$

For a constant first block, Lemma 2 is the argument in G. Harcos's note "On a result of András Biró".

## 3. The profile, and the limit theorem

**The profile.**
- Fix $T>0$, knots $u_j=j/48$ ($j=0,\dots,24$), and real numbers $\psi_0,\dots,\psi_{24}$.
- Let $\varphi:[0,\tfrac12]\to\mathbb R$ be the piecewise-linear function with $\varphi(u_j)=\psi_j$, with slopes $\beta_j=48(\psi_{j+1}-\psi_j)$.
- Put $g(u)=Te^{i\varphi(u)}$, $\gamma=g(0)$ and $a=\operatorname{Re}\gamma$.
- Define
$$d(u)=\gamma-g(u)\quad(0<u\le\tfrac12),\qquad d(u)=\gamma\quad(u>\tfrac12),\qquad \kappa=\sup_{0<u\le1}|d(u)| .$$
We also put $d(0)=0$ (its limit). Single points do not affect any of the integrals below.

**The construction.** For $n\ge2$, apply Lemma 2 with $K=\lfloor n/2\rfloor$ and $s_k=g(k/n)$ ($1\le k\le K$; note $k/n\le\tfrac12$). Since $|s_k|=T$,
$$R_n\le\max(T,F_n),\qquad F_n=|P_n|/D_n. \tag{1}$$

**Theorem A.** Assume $\kappa<1$ and $a\ge0$. (Then automatically $a\le|\gamma|=T\le\kappa<1$, because $|d|=T$ on $(\frac12,1]$.)
1. The equation
$$t\,\rho(t)=d(t)+\int_0^t d(u)\,\rho(t-u)\,du\qquad(0<t\le1) \tag{2}$$
has exactly one bounded solution $\rho$ on $(0,1]$.
2. Put
$$p(t)=t^{-\gamma}+\int_0^t (t-v)^{-\gamma}\rho(v)\,dv,\qquad F=\frac{|p(1)|}{\int_0^{1/2}|p(t)|\,\frac{dt}{1-t}} .$$
Then the denominator of $F$ is positive and finite, and $F_n\to F$ as $n\to\infty$.
3. Hence $\limsup_n R_n\le\max(T,F)$.

The proof takes the rest of this section. Throughout, $\Lambda=\max_j|\beta_j|$ and $M=\max(T\Lambda,2T)$. For $0<u\le\frac12$,
$$|d(u)|=T|1-e^{i(\varphi(u)-\varphi(0))}|\le T\Lambda u,$$
and for $u>\frac12$, $|d(u)|=T\le2Tu$. Hence
$$|d(u)|\le Mu \text{ on }(0,1], \qquad |d|\le\kappa .\tag{3}$$

### Step 1: exact discrete identities

Put $c_k=1-s_k$ for $k\le K$ and $c_k=1$ for $k>K$. Since $-\log(1-x)=\sum_k x^k/k$,
$$\sum_m P_mx^m=\exp\Bigl(\sum_{k\ge1}\frac{c_k}{k}x^k\Bigr).$$
Write $c_k=(1-\gamma)+d_k$. Then $d_k=\gamma-g(k/n)=d(k/n)$ for $k\le K$, and $d_k=\gamma=d(k/n)$ for $k>K$ (because $k>K$ implies $k/n>\frac12$). So
$$d_k=d(k/n)\quad\text{for every }k\ge1, \tag{4}$$
and
$$\sum_m P_mx^m=(1-x)^{\gamma-1}D(x),\qquad (1-x)^{\gamma-1}=\sum_{j\ge0}a_jx^j,\quad a_j=\frac{\Gamma(j+1-\gamma)}{\Gamma(1-\gamma)\,j!},$$
where $D(x)=\exp(\sum_k d_kx^k/k)=\sum_m\delta_mx^m$. Here $\delta_0=1$, and $m\delta_m=\sum_{k=1}^m d_k\delta_{m-k}$ (from $xD'=(\sum_kd_kx^k)D$). Therefore
$$P_j=\sum_{i=0}^{j}a_{j-i}\,\delta_i . \tag{5}$$

### Step 2: the continuous problem

Let $X$ be the bounded Borel-measurable functions on $(0,1]$ with the sup norm (a Banach space). Put
$$(\mathcal Kf)(t)=\frac1t\int_0^t d(u)f(t-u)\,du .$$
- $\|\mathcal Kf\|\le\kappa\|f\|$.
- $\mathcal Kf$ is continuous on $(0,1]$, since $d*f$ is the convolution of a bounded function with a bounded function on $[0,1]$.
- (2) reads $\rho=d(t)/t+\mathcal K\rho$, and $d(t)/t$ is bounded by (3).

Since $\kappa<1$, there is a unique bounded solution, the Neumann series. It satisfies $\|\rho\|\le B:=M/(1-\kappa)$.

**Regularity of $\rho$.**
- $d(t)/t$ is uniformly continuous on $(0,\frac12]$: it extends continuously to $0$ with value $-iT\beta_0e^{i\psi_0}$. It is also uniformly continuous on $(\frac12,1]$.
- $|\mathcal K\rho(t)|\le MBt/2$, and $\mathcal K\rho=(d*\rho)/t$ is continuous.

Hence $\rho$ is uniformly continuous on $(0,\frac12]$ and on $(\frac12,1]$. It has a jump only at $\frac12$, and $\rho$ is left-continuous there.

**The function $p$.**
- $t\mapsto\int_0^t u^{-\gamma}\rho(t-u)\,du$ is continuous on $[0,1]$, since it is the convolution of $u^{-\gamma}\in L^1$ with a bounded function. So $p$ is continuous on $(0,1]$.
- $|p(t)|\ge t^{-a}-Bt^{1-a}/(1-a)>0$ for small $t$, so the denominator of $F$ is positive.
- It is finite because $|p(t)|\le t^{-a}+B/(1-a)$ and $a<1$.

### Step 3: the discrete solution converges to ρ

Let $\rho_n(m)=n\,\delta_m$ and $t_m=m/n$. By (4), the recursion for $\delta_m$ reads
$$t_m\rho_n(m)=d(t_m)+\frac1n\sum_{k=1}^{m-1}d(t_k)\,\rho_n(m-k)\qquad(1\le m\le n). \tag{6}$$

**Uniform bound.** Since $|d|\le\kappa$, $|d(t_m)|\le Mt_m$ and $\frac1n\sum_{k<m}|d(t_k)|\le\kappa t_m$, induction gives $|\rho_n(m)|\le B$.

**Error recursion.** Let $e_m=\rho_n(m)-\rho(t_m)$. Subtracting (2) at $t=t_m$ from (6),
$$t_me_m=\frac1n\sum_{k=1}^{m-1}d(t_k)e_{m-k}+\tau_m,\qquad \tau_m=\frac1n\sum_{k=1}^{m-1}f_m(t_k)-\int_0^{t_m}f_m(u)\,du,$$
where $f_m(u)=d(u)\rho(t_m-u)$. So
$$|e_m|\le\kappa\max_{l<m}|e_l|+|\tau_m|/t_m,\qquad\text{hence}\qquad \max_{m\le n}|e_m|\le\frac{\sup_m|\tau_m|/t_m}{1-\kappa}.$$

**Bounding $\tau_m$.** Write
$$\tau_m=\sum_{k=1}^{m-1}\int_{t_{k-1}}^{t_k}\bigl(f_m(t_k)-f_m(u)\bigr)\,du-\int_{t_{m-1}}^{t_m}f_m .$$
- The last integral is at most $MBt_m/n$ in modulus, by (3).
- The function $f_m$ is a product of $d$, which is continuous on $(0,\frac12]$ and on $(\frac12,1]$, and $u\mapsto\rho(t_m-u)$, which has at most one jump. So at most two cells contain a discontinuity, and they occur only when $t_m>\frac12$. On each of these two cells the oscillation of $f_m$ is at most $2\kappa B$.
- On every other cell the oscillation is at most $B\,\omega_d(1/n)+\kappa\,\omega_\rho(1/n)$. Here $\omega_d$ and $\omega_\rho$ are the moduli of uniform continuity of $d$ and $\rho$ on their two pieces.

Dividing by $t_m$ (and using $t_m>\frac12$ when there are discontinuous cells):
$$\sup_m|\tau_m|/t_m\le B\omega_d(1/n)+\kappa\omega_\rho(1/n)+\frac{MB+8\kappa B}{n}\longrightarrow0 .$$
Therefore
$$\max_{1\le m\le n}|\rho_n(m)-\rho(m/n)|\to0 . \tag{7}$$

### Step 4: asymptotics of $P_j$

Put $\eta_l=\Gamma(1-\gamma)\,a_l\,l^{\gamma}=\Gamma(l+1-\gamma)\,l^{\gamma}/\Gamma(l+1)$ for $l\ge1$. The classical asymptotic $\Gamma(l+\alpha)/\Gamma(l+\beta)\sim l^{\alpha-\beta}$ gives $\eta_l\to1$. Put $C_\eta=\sup_l|\eta_l|<\infty$.

Let $\Pi_n(j)=\Gamma(1-\gamma)\,n^{\gamma}P_j$. By (5),
$$\Pi_n(j)=\eta_j\Bigl(\frac jn\Bigr)^{-\gamma}+\frac{\Gamma(1-\gamma)n^{\gamma}}{n}\rho_n(j)+\frac1n\sum_{l=1}^{j-1}\eta_l\Bigl(\frac ln\Bigr)^{-\gamma}\rho_n(j-l)\qquad(1\le j\le n).$$
Here the middle term is the term $l=0$; it has modulus $\le|\Gamma(1-\gamma)|Bn^{a-1}\to0$.

**(B2) Domination.** Since $v^{-a}$ is decreasing, $\frac1n\sum_{l=1}^{j-1}(l/n)^{-a}\le\int_0^{j/n}v^{-a}dv$. Hence, for $1\le j\le n$ and $t=j/n$,
$$|\Pi_n(j)|\le C\,t^{-a},\qquad C=C_\eta+|\Gamma(1-\gamma)|B+\frac{C_\eta B}{1-a}.$$

**(B1) Convergence.** For every $\varepsilon>0$,
$$\sup_{\varepsilon n\le j\le n}|\Pi_n(j)-p(j/n)|\to0 .$$
*Proof.* Let $t=j/n\in[\varepsilon,1]$ and fix $\delta\in(0,\varepsilon/2)$. Split
$$p(t)=t^{-\gamma}+I_{\le\delta}(t)+I_{>\delta}(t),\qquad I_{\le\delta}=\int_0^{\delta}u^{-\gamma}\rho(t-u)\,du,\quad I_{>\delta}=\int_\delta^{t}u^{-\gamma}\rho(t-u)\,du .$$
Split the last sum in $\Pi_n(j)$ the same way: $\Sigma_{\le\delta}$ (over $1\le l\le\delta n$) and $\Sigma_{>\delta}$ (over $\delta n<l\le j-1$). Then:

1. **First term.** $|\eta_j(j/n)^{-\gamma}-t^{-\gamma}|=|\eta_j-1|\,t^{-a}\le|\eta_j-1|\,\varepsilon^{-a}\to0$ uniformly, since $j\ge\varepsilon n$.
2. **Middle term.** It tends to $0$ (shown above).
3. **Near part.** $|\Sigma_{\le\delta}|\le C_\eta B\,\delta^{1-a}/(1-a)$ and $|I_{\le\delta}|\le B\,\delta^{1-a}/(1-a)\le C_\eta B\,\delta^{1-a}/(1-a)$. Here $C_\eta\ge1$, since $\eta_l\to1$.
4. **Replacing $\rho_n$ by $\rho$.** Let $\Sigma'$ be $\Sigma_{>\delta}$ with $\rho_n(j-l)$ replaced by $\rho((j-l)/n)$. Then $|\Sigma_{>\delta}-\Sigma'|\le C_\eta\max_m|e_m|\cdot\frac1n\sum_{l\le n}(l/n)^{-a}\le C_\eta\max_m|e_m|/(1-a)\to0$ by (7).
5. **Replacing $\eta_l$ by $1$.** Let $\Sigma''$ be $\Sigma'$ with $\eta_l$ replaced by $1$. Then $|\Sigma'-\Sigma''|\le\sup_{l>\delta n}|\eta_l-1|\cdot B/(1-a)\to0$.
6. **Riemann sum.** $\Sigma''=\frac1n\sum_{\delta n<l\le j-1}(l/n)^{-\gamma}\rho(t-l/n)$ is a right-endpoint Riemann sum, with cells of width $1/n$, for $I_{>\delta}=\int_\delta^tu^{-\gamma}\rho(t-u)\,du$.
   - Take $n\ge2/\delta$. Then every cell lies in $[\delta/2,1]$, where $|u^{-\gamma}|\le(\delta/2)^{-a}$.
   - The two end cells contribute at most $2(\delta/2)^{-a}B/n$.
   - On every other cell, the oscillation of $u\mapsto u^{-\gamma}\rho(t-u)$ is at most $B\,\omega_1(1/n)+(\delta/2)^{-a}\omega_\rho(1/n)$. Here $\omega_1$ is the modulus of continuity of $u^{-\gamma}$ on $[\delta/2,1]$, and $\omega_\rho$ is as in Step 3.
   - The exception is the at most one cell that contains the jump of $\rho(t-\cdot)$ (at $u=t-\frac12$). There the oscillation is at most $2(\delta/2)^{-a}B$, and the contribution is at most $2(\delta/2)^{-a}B/n$.
   - Hence $|\Sigma''-I_{>\delta}|\to0$ uniformly in $t\in[\varepsilon,1]$.

Therefore $\limsup_n\sup_{\varepsilon n\le j\le n}|\Pi_n(j)-p(j/n)|\le2C_\eta B\,\delta^{1-a}/(1-a)$ for every small $\delta>0$. Letting $\delta\to0$ proves (B1). $\square$

### Step 5: conclusion

Since $|\Gamma(1-\gamma)n^{\gamma}|=|\Gamma(1-\gamma)|n^{a}$, (1) gives
$$F_n=\frac{|\Pi_n(n)|}{\frac1n\sum_{j=0}^{L}|\Pi_n(j)|/(1-j/n)},\qquad L=n-K-1=\lceil n/2\rceil-1 .$$

**Numerator.** $\Pi_n(n)\to p(1)$ by (B1).

**Denominator.**
- The term $j=0$ equals $|\Gamma(1-\gamma)|n^{a-1}\to0$.
- The terms $j\ge1$ equal $\int_0^{L/n}h_n(t)\,dt$, where $h_n(t)=|\Pi_n(\lceil nt\rceil)|/(1-\lceil nt\rceil/n)$.
- By (B1) and the continuity of $p$, $h_n(t)\to|p(t)|/(1-t)$ for every $t\in(0,\frac12)$.
- By (B2), $h_n(t)\le2C\,t^{-a}$, which is integrable.
- Since $L/n\to\frac12$, dominated convergence gives that the denominator converges to $\int_0^{1/2}|p(t)|\,dt/(1-t)>0$.

Hence $F_n\to F$. With (1), $\limsup R_n\le\max(T,F+\epsilon)$ for every $\epsilon>0$. $\blacksquare$

**Sanity check (Harcos's case).** If $\varphi\equiv\psi_0$ is constant, then $d=0$ on $(0,\frac12]$. So $\rho=0$ there and $\rho(t)=\gamma/t$ on $(\frac12,1]$. With $w=-\gamma$,
$$p(1)=1-w\int_0^{1/2}\frac{t^{w}}{1-t}\,dt,\qquad \int_0^{1/2}|p|\frac{dt}{1-t}=\int_0^{1/2}\frac{|t^{w}|}{1-t}\,dt .$$
This is exactly Harcos's limit formula, which gives $0.693676$ for $w=-0.43246-0.54237i$.

## 4. The profile used, and the certified inequality F < T

**The profile.** The profile is in `c42_profile_0.68637.json` (SHA-256 `dcea4edbec1d5935f2f04d4d1b5b8379e2d2d7d78072a1f089c7abbe11ded395`):
- $T=0.68637$;
- $\psi_0,\dots,\psi_{24}$ as exact decimal numbers.

Its properties (computed in ball arithmetic):
- $a=\operatorname{Re}\gamma=0.16609\ldots\in(0,1)$.
- $\max_j|\psi_j-\psi_0|=0.7753<\pi$. So on $(0,\frac12]$, $|d(u)|=2T|\sin((\varphi(u)-\psi_0)/2)|$ is largest at a knot, and is at most $0.5190$.
- On $(\frac12,1]$, $|d|=T$. Hence $\kappa=T=0.68637<1$.
- All slopes $\beta_j$ are nonzero ($1.20\le|\beta_j|\le5.82$). This is not used in the proof. It is needed only by `rigorous_limit.py`, whose closed-form moments divide by $\beta_j$ (`independent_check.py` does not need it).

So Theorem A applies, and it remains to show $F<T$.

**Lemma 3 (a posteriori bound).** Let $\tilde\rho$ be any bounded measurable function on $(0,1]$. Put
$$R(t)=d(t)+\int_0^t d(u)\tilde\rho(t-u)\,du-t\tilde\rho(t).$$
If $\sup_t|R(t)/t|<\infty$, then
$$\|\rho-\tilde\rho\|_\infty\le\frac{\sup_{0<t\le1}|R(t)/t|}{1-\kappa}.$$

*Proof.* Subtracting, $e=\rho-\tilde\rho$ satisfies $e=\mathcal Ke+R/t$, so $\|e\|\le\kappa\|e\|+\|R/t\|$. $\square$

Put $\tilde p(t)=t^{-\gamma}+\int_0^t(t-v)^{-\gamma}\tilde\rho(v)\,dv$ and $\varepsilon=\|\rho-\tilde\rho\|_\infty$. Then
$$|p(t)-\tilde p(t)|\le\varepsilon\,t^{1-a}/(1-a),$$
so
$$F\le\frac{|\tilde p(1)|+\varepsilon/(1-a)}{\int_0^{1/2}|\tilde p|\frac{dt}{1-t}-\varepsilon\int_0^{1/2}\frac{t^{1-a}}{(1-a)(1-t)}dt}. \tag{8}$$

### What `rigorous_limit.py` computes

All quantities below are computed in Arb ball arithmetic (192 bits) from the exact inputs. The only floating-point step produces $\tilde\rho$, and $\tilde\rho$ may be any function.

**Grid.**
- $N=48M$ (so the knots and $\frac12$ are grid points), $h=1/N$, $t_i=ih$, $H=N/2$.
- $\tilde\rho$ is linear on each cell $[t_i,t_{i+1}]$, from a value $\tilde\rho_i^{+}$ to a value $\tilde\rho_{i+1}^{-}$. The two values at a node agree except at $i=H$, where a jump $J=\tilde\rho_H^+-\tilde\rho_H^-$ is allowed (the true $\rho$ jumps at $\frac12$).
- The values come from a floating-point collocation $R(t_i)=0$; then $\tilde\rho_0^+$, $\tilde\rho_i^\pm$ are rounded to exact binary numbers.
- Put $\sigma_i=(\tilde\rho_{i+1}^--\tilde\rho_i^+)/h$ (the slope on cell $i$) and $\Delta_k=\sigma_k-\sigma_{k-1}$.

**(C1) Nodal values of $R$.** On a cell, $d$ is $\gamma-Te^{i(\theta+\beta x)}$ or the constant $\gamma$. Its moments against $1-x/h$ and $x/h$ are computed in closed form. Then $R(t_i^\pm)$ is computed rigorously as a discrete convolution (`acb_poly` product).

**(C2) $R''$ inside cell $i$.** $R$ is $C^2$ there, and
$$R''(t)=d''(t)+d'(t)\tilde\rho(0)+\sigma_0d(t)+\sum_{1\le k\le i}\Delta_k\,d(t-t_k)+\mathbf 1_{i\ge H}\,J\,d'(t-\tfrac12)-2\sigma_i .$$
This follows from writing $\tilde\rho=\tilde\rho_c+J\mathbf 1_{(1/2,1]}$ with $\tilde\rho_c$ continuous, and differentiating $\int_0^td(u)\tilde\rho(t-u)\,du$ twice. Inside a cell no breakpoint of any $d(t-t_k)$ is crossed, because all breakpoints of $d$ are grid points. $R''$ is evaluated at the cell centre $t_c$.

**(C3) Bound on $R'''$.**
$$|R'''|\le B_3=T\beta^3+T\beta^2|\tilde\rho(0)|+T\beta\bigl(|\sigma_0|+\textstyle\sum_k|\Delta_k|\bigr)+|J|T\beta^2,\qquad \beta=\max_j|\beta_j|.$$
This uses $|d^{(r)}|\le T\beta^r$ on $(0,\frac12]$ and $d'=0$ on $(\frac12,1]$. Then $|R''|\le|R''(t_c)|+\tfrac h2B_3$ on the cell.

**(C4) Bound on $|R/t|$, cell by cell.**
- For $i\ge1$:
$$\sup_{[t_i,t_{i+1}]}|R/t|\le\frac{\max(|R(t_i^+)|,|R(t_{i+1}^-)|)+\frac{h^2}8\bigl(|R''(t_c)|+\frac h2B_3\bigr)}{t_i}.$$
  This is linear interpolation with the Peano-kernel error bound.
- For $i=0$: $R(0)=0$ and $R'(0^+)=d'(0)-\tilde\rho(0)$, so
$$|R/t|\le|R'(0^+)|+\tfrac h2\bigl(|R''(t_c)|+\tfrac h2B_3\bigr).$$
- At $t=\frac12$ both one-sided values $R(t_H^\pm)$ enter the bounds, so any convention for the value $\tilde\rho(\frac12)$ is covered.
- The maximum over all cells, divided by $1-\kappa$, is $\varepsilon$ (Lemma 3).

**(D1) Numerator.** $\tilde p(1)$ is computed exactly per cell from the moments of $u^{-\gamma}$ and $u^{1-\gamma}$ (closed form). The numerator of (8) is then bounded above.

**(D2) Denominator on $[0,t_*]$**, with $t_*=\lceil N/1000\rceil h$. Here $|\tilde p(t)|\ge t^{-a}-P_*t^{1-a}/(1-a)$, where $P_*$ is the largest $|\tilde\rho|$ at the nodes in $[0,t_*]$. The program checks that this is positive, then integrates it exactly (using $1/(1-t)\ge1$).

**(D3) Denominator on the cells of $[t_*,\frac12]$.**
- $\int|\tilde p|\frac{dt}{1-t}\ge\bigl|\int L\frac{dt}{1-t}\bigr|-\frac{1}{1-t_{k+1}}\int|\tilde p-L|$, where $L$ is the linear interpolant of $\tilde p$ between the nodes. The first integral is in closed form (logarithms).
- $\int_{\rm cell}|\tilde p-L|\le\frac{h^2}8\int_{\rm cell}|\tilde p''|$, with
$$\tilde p''(t)=\gamma(\gamma+1)t^{-\gamma-2}-\gamma\tilde\rho(0)t^{-\gamma-1}+\sigma_0t^{-\gamma}+\sum_{t_k<t}\Delta_k(t-t_k)^{-\gamma}\qquad(t<\tfrac12).$$
- Each term is integrated exactly in modulus. The singular terms $(t-t_k)^{-a}$ are integrable.
- Finally the $\varepsilon$-correction of (8) is subtracted, using $\int_0^{1/2}\frac{t^{1-a}}{(1-a)(1-t)}\le\frac{2\cdot2^{a-2}}{(1-a)(2-a)}$.

The program prints `PASS` only if the lower bound for the denominator is certainly positive and the resulting upper bound for $F$ is certainly smaller than $T$, both as comparisons of balls. The other hypotheses it uses are checked as well: exactly 25 phases with the knots $j/48$, $0<a<1$, $|\psi_j-\psi_0|<3$ (for the bound on $\kappa$), $\kappa<1$, $\beta_j\ne0$, the positivity in (D2), and finite bounds. If one of them fails, the program stops with `FAIL` and exit code 1.

### Output of `rigorous_limit.py` (python-flint 0.9.0, Linux, Python 3.13)

Profile `c42_profile_0.68637.json` ($T=0.68637$):

| $M$ | $N$ | $\sup\lvert R/t\rvert$ | $\varepsilon$ | upper bound for $\lvert p(1)\rvert$ | lower bound for $\int_0^{1/2}\lvert p\rvert/(1-t)$ | $F\le$ | result |
|---:|---:|---|---|---|---|---|---|
| 1280 | 61 440 | 4.22e-7 | 1.35e-6 | 0.391303 | 0.570105 | 0.6863687 | PASS |
| 2560 | 122 880 | 1.06e-7 | 3.37e-7 | 0.391302 | 0.570106 | **0.6863660** | PASS |

The margin is $T-F\ge4\cdot10^{-6}$. It is small, but this is a certified inequality between balls, not a floating-point comparison. Floating point gives $F\approx0.6863601$ (Section 5).

Profile `c42_profile_0.6865.json` ($T=0.6865$, version 1.0.0):

| $M$ | $N$ | $\sup\lvert R/t\rvert$ | $\varepsilon$ | upper bound for $\lvert p(1)\rvert$ | lower bound for $\int_0^{1/2}\lvert p\rvert/(1-t)$ | $F\le$ | result |
|---:|---:|---|---|---|---|---|---|
| 320 | 15 360 | 6.76e-6 | 2.16e-5 | 0.391152 | 0.569973 | 0.686264 | PASS |
| 640 | 30 720 | 1.70e-6 | 5.40e-6 | 0.391133 | 0.569980 | 0.686221 | PASS |

**A second, independent checker.** `independent_check.py` was written by a separate AI instance (Claude Code, Claude Opus 5.5) from this file only, before it saw `rigorous_limit.py`. It uses the same principle (Lemma 3 and (8)), but a different implementation:
- the convolutions are computed through the "ramp" form $\tilde\rho(v)=\tilde\rho(0)+\sigma_0v+\sum_k\Delta_k(v-t_k)_++J\mathbf 1_{v>1/2}$ and closed-form antiderivatives;
- $\sup|R''|$ is enclosed cell by cell, with no global bound on $R'''$;
- the cut near $0$ is smaller.

For the profile with $T=0.68637$ it gives $F\le0.6863647$ at $M=1280$ and $F\le0.6863615$ at $M=2560$, both PASS. `rigorous_limit.py` gives $0.6863687$ and $0.6863660$. The two programs agree on $\sup|R/t|$ to four significant digits and on the bound for $|p(1)|$ to seven decimals. Its bounds for $F$ are slightly smaller, because its cut near $0$ is smaller. For the version-1.0.0 profile it gives $F\le0.6862175$ at $M=640$, against $0.6862204$ from `rigorous_limit.py`. On Harcos's constant-phase profile, whose exact value $0.6936763$ is known, it gives upper bounds that decrease towards that value as $M$ grows. Its referee report is in `AI_REVIEW.md`. Its remarks (the hypothesis $a\ge0$, measurability, the convention $d(0)=0$, the details of (B1)) are incorporated in this version. Later the author added a few input checks to it (see Versions); its computation is unchanged.

The two programs are independent code, but they follow the same mathematical route, Lemma 3 and (8). A mistake shared by Lemma 3 or (8) would not be caught by running both. Both are proved above, and the reviewer re-derived them by hand.

Hence $F<0.68637=T$, and by Theorem A, $\limsup_n R_n\le0.68637$. $\blacksquare$

## 5. Independent numerical cross-checks (floating point, not part of the proof)

- **Direct solver.** A solver for the equation $tp(t)=\int_0^tc(u)p(t-u)\,du$ (with $c=1-g$ on $[0,\frac12]$, $c=1$ after) gives $F=0.68636008$ for the profile with $T=0.68637$, and $F=0.68620112$ for the version-1.0.0 profile. The same solver reproduces Harcos's $0.693676$ for a constant phase.
- **Finite $n$.** The exact construction of Section 3 (with $K=\lfloor n/2\rfloor$) gives $F_n=0.6864165$, $0.6863783$, $0.6863660$ for $n=2.5\cdot10^5$, $10^6$, $4\cdot10^6$, for the profile with $T=0.68637$. These values approach the same limit $0.68636$ from above.
- **The checker's error bound.** Inside the sampled cells, the true residual $|R/t|$ computed by adaptive quadrature never exceeds the checker's cell bound. At the worst cell (just after the first knot) the two are $4.17\cdot10^{-4}$ and $4.22\cdot10^{-4}$ (profile $T=0.68637$, $M=40$).
- **The best value of this family.** Minimizing $\max(T,F)$ over profiles, in floating point and directly in the limit, gives about $0.6863655$ with the 24 equal pieces used here, and about $0.686361$ with knots that are finer near $0$. (The profile of this repository has $F\approx0.6863601<T$. Lowering $T$ to the optimum would leave no room for the certified error bound.) These optimal values are not claimed. The claim $0.68637$ is within $10^{-5}$ of the first one.

## 6. Relation to earlier work

- Biró (2000) proved $\limsup R_n<1$. Harcos's computation, reported there, gives $0.69368$; the short proof is in Harcos's note.
- The 2026 certificates in the Optimization Constants repository (Griego, Röhrig, Plata, Pinho, Koshta) refine a block construction whose first block has a constant phase.
- The present construction lets the phase vary from the start: "first-block cut-off $\tau=0$". The limit is described by the integral equation (2) instead of correction terms.
- Theorem A is self-contained and does not use those works.

## Acknowledgement

We thank Ricardo Pinho for reading the code carefully and for reporting the missing check of the denominator (see Versions).

## AI use

The construction, the proof, the code and this text were produced with substantial help from AI models (Claude Opus 5.5 and Claude Sonnet 5.5, Anthropic), directed by the author, who also ran and checked the computations. The proof was also checked by a separate AI instance (`AI_REVIEW.md`), but it has not yet been reviewed by a professional mathematician. Corrections are very welcome.
