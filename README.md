# Composite-Displacement Sieve (`greedy-ast`)

Reference implementation of the *Greedy–Ast* branch sieve from  
> “The 6k±1 Composite–Displacement Sieve: Formal Analysis and Efficient Implementation”.

## Quick start

## Reproducibility

| Artifact | Link | Notes |
|----------|------|-------|
| **CI status** | ![CI](https://github.com/stepstein/greedy-ast/actions/workflows/benchmark.yml/badge.svg?branch=dev) | Table-1-Benchmark wird bei jedem Push neu ausgeführt |
| **Docker image** | `ghcr.io/stepsteine/greedy-ast-sieve:latest` | Komplett lauffähig:  `docker run --rm ghcr.io/stepstein/greedy-ast:latest` |
| **Dataset (≤ 10⁸)** | [`primes6.csv.gz`](https://github.com/stepstein/greedy-ast/raw/main/primes6.csv.gz) (20 MiB, Git LFS) | 5 761 453 Zeilen, Spalten **prime,gap** |

### SHA-256 checksum

```bash
shasum -a 256 primes6.csv.gz
# => 79510561b0dad05a9ac91f6b9c00e723ab8409dc1f339ff86991d094646fad6d  primes6.csv.gz

```bash
pip install -r requirements.txt
python benchmarks.py 100000000  # reproduces Table-1 row for 1e8
---

### Dataset (primes6.csv.gz)

* Range: 5 ≤ p ≤ 10^8, p ≡ 1 or 5 (mod 6)
* Lines: 5 761 454 (1 header + 5 761 453 primes)
* SHA-256:  79510561b0dad05a9ac91f6b9c00e723ab8409dc1f339ff86991d094646fad6d
* Download:  
  ```bash
  git lfs install
  git clone https://github.com/stepstein/greedy-ast-sieve.git
  cd greedy-ast-sieve && git lfs pull