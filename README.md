# Turán's pure power sum constant: C42 ≤ 0.6865

**Claim.** $\displaystyle\limsup_{n\to\infty} R_n \le 0.6865$, where

$$R_n=\inf_{z_1=1,\ z_2,\dots,z_n\in\mathbb C}\ \max_{1\le k\le n}\Bigl|\sum_{j=1}^n z_j^k\Bigr| .$$

This is constant **C42** in the [Optimization Constants repository](https://github.com/teorth/optimizationproblems), which uses the equivalent normalization $\max_j|z_j|=1$ (Lemma 1 in NOTES.md). It is also [Erdős problem #519](https://www.erdosproblems.com/519).

**Previous bounds:**
- best refereed: $0.69368$ (Harcos, reported in Biró 2000);
- best claimed: $0.6873358063$ (Koshta 2026, unrefereed).

**Status.** Unrefereed. Made with substantial help from AI models (see [AI use](#ai-use)).

**Author:** Vasileios Bakeas, Department of Mechanical Engineering, University of Thessaly, Volos, Greece (bakeasb@gmail.com)

## The argument in four lines

1. **Harcos's linearization (exact, every n).** Prescribe the first $\lfloor n/2\rfloor$ power sums freely. The remaining ones can then be chosen with a common modulus $F_n$ (an explicit number) so that $z=1$ is in the tuple. Hence $R_n\le\max(T,F_n)$, where $T$ is the largest prescribed modulus.
2. **The prescribed sums.** Here $s_k=T\,e^{i\varphi(k/n)}$, with $T=0.6865$ and a piecewise-linear phase $\varphi$ with 24 pieces (`c42_profile_0.6865.json`).
3. **Theorem A (proved in NOTES.md).** $F_n\to F$, where $F$ is given by an explicit linear integral equation. The proof uses only that $\sup|d|<1$, i.e. that a certain convolution operator is a contraction.
4. **Certified computation.** `rigorous_limit.py` shows, in Arb ball arithmetic, that $F\le0.686221<0.6865$. Hence $\limsup R_n\le0.6865$.

When the phase is constant, Theorem A reduces exactly to Harcos's limit formula (0.693676). The earlier 2026 certificates keep the phase constant on a first block of length $\tau n$. Here it varies from the start.

## Verify

```bash
pip install python-flint==0.9.0 numpy
python rigorous_limit.py c42_profile_0.6865.json 640        # about 10 seconds, prints PASS
```

`expected_output_M640.txt` has the output we obtained ($F\le0.686221$).

Optional floating-point cross-checks (not part of the proof):
- `python crosscheck/limit_direct.py`: a different solver of the limit equation. It also reproduces Harcos's 0.693676.
- `python crosscheck/finite_n.py`: the exact finite-$n$ construction up to $n=4\cdot10^6$. Its values approach the same limit, 0.68620.

## Files

| File | Contents |
|---|---|
| `NOTES.md` | statement, complete proof (Lemmas 1–3, Theorem A), and exactly what the program checks |
| `c42_profile_0.6865.json` | the certificate: $T$ and the 25 phase values (exact decimals) |
| `rigorous_limit.py` | rigorous checker (python-flint / Arb) |
| `expected_output_M640.txt` | its output |
| `crosscheck/` | floating-point cross-checks |

## Related

Rigorous upper bounds for $R_n$ at specific $n$ (300 to $10^6$), by the same author: [turan-power-sum-certificates](https://github.com/Bakeas/turan-power-sum-certificates), DOI [10.5281/zenodo.23806909](https://doi.org/10.5281/zenodo.23806909).

## AI use

The construction, the proof, the code and the text were produced with substantial help from AI models (Claude Opus 5.5 and Claude Sonnet 5.5, Anthropic), directed by the author, who also ran and checked the computations. The proof has not yet been reviewed by a professional mathematician. Corrections are very welcome (GitHub issue or email).

## License

- Code: MIT (`LICENSE`).
- Text and data: CC BY 4.0.
