import numpy as np
from typing import Generator, List

# ---------- primes6 generator ----------
def primes6_upto(limit: int) -> Generator[int, None, None]:
    if limit >= 2: yield 2
    if limit >= 3: yield 3
    size = limit // 3 + 1
    sieve = np.ones(size, dtype=np.bool_)
    for i, is_prime in enumerate(sieve):
        if not is_prime: continue
        p = 3 * i + 1 | 1
        if p * p > limit: break
        step = 2 * p
        sieve[(p * p) // 3 :: step] = False
        sieve[(p * (p - 2 * (i & 1) + 4)) // 3 :: step] = False
    for i in np.nonzero(sieve)[0]:
        yield 3 * i + 1 | 1

# ---------- bitmap helper ----------
def _bitmap_index(n: int, lo: int) -> int:
    return ((n - lo) // 6) * 2 + (0 if n % 6 == 1 else 1)

# ---------- main routine ----------
def greedy_ast_count(x: int, block: int = 5_000_000) -> int:
    if x < 5: return 0
    z = int(x ** (1 / 3))
    actives: List[int] = [p for p in primes6_upto(z) if p > 3]
    total = 0
    for lo in range(5, x + 1, block * 6):
        hi = min(lo + block * 6, x + 1)
        size = ((hi - lo + 5) // 6) * 2
        bitmap = np.ones(size, dtype=np.bool_)
        for p in actives:
            # branch 1
            k = max(0, (lo - p * p + 2 * p - 1) // (2 * p))
            n = p * p + 2 * p * k
            while n < hi:
                if n % 6 in (1, 5):
                    bitmap[_bitmap_index(n, lo)] = False
                n += 2 * p
            # branch 2
            k = max(0, (lo - p * p + 4 * p - 1) // (4 * p))
            n = p * p + 4 * p * k
            while n < hi:
                if n % 6 in (1, 5):
                    bitmap[_bitmap_index(n, lo)] = False
                n += 4 * p
        total += bitmap.sum()
    return int(total)
