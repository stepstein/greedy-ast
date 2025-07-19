# Composite-Displacement Sieve (`greedy-ast`)

Reference implementation of the *Greedy–Ast* branch sieve from  
> “The 6k±1 Composite–Displacement Sieve: Formal Analysis and Efficient Implementation”.

## Quick start

## Reproducibility

| Artifact | Link | Notes |
|----------|------|-------|
| **CI status** | [![CI](https://github.com/stepstein/greedy-ast/actions/workflows/benchmark.yml/badge.svg)](https://github.com/stepstein/greedy-ast/actions) | Table-1-Benchmark wird bei jedem Push neu ausgeführt |
| **Docker image** | `ghcr.io/stepsteine/greedy-ast:latest` | Completely runnable:  `docker run --rm ghcr.io/stepstein/greedy-ast:latest` |
| **Dataset (≤ 10⁸)** | [`primes6.csv.gz`](https://github.com/stepstein/greedy-ast/raw/main/primes6.csv.gz) (20 MiB, Git LFS) | 5 761 453 Zeilen, Spalten **prime,gap** |

### SHA-256 checksum primes6.csv.gz
79510561b0dad05a9ac91f6b9c00e723ab8409dc1f339ff86991d094646fad6d  primes6.csv.gz

### Brief explanation 

greedy_ast without parameters counts up to 1e8 <br>
```
$ docker run –rm ghcr.io/stepstein/greedy-ast:latest
```

greedy_ast with its own limit<br>
```
$ docker run –rm ghcr.io/stepstein/greedy-ast:latest  python benchmarks.py 1000000000
```

 