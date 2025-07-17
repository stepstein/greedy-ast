import numpy as np
from math import isqrt

def primes6_upto(limit):
    """Yield all primes ≤ limit that are 6k±1 (plus 2 & 3)."""
    if limit >= 2:
        yield 2
    if limit >= 3:
        yield 3
    sieve = np.ones(limit // 3 + 1, dtype=np.bool_)
    for i, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        p = 3 * i + 1 | 1          # 6k±1 mapping
        if p * p > limit:
            break
        step = 2 * p
        sieve[(p * p) // 3 :: step] = False
        sieve[(p * (p - 2 * (i & 1) + 4)) // 3 :: step] = False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            yield 3 * i + 1 | 1

def greedy_ast_count(x, block=5_000_000):
    z = int(x ** (1/3))
    actives = [p for p in primes6_upto(z) if p > 3]  # skip 2,3
    count = 0
    for lo in range(5, x + 1, block * 6):
        hi = min(lo + block * 6, x + 1)
        size = (hi - lo) // 6 * 2          # number of 6k±1 slots
        bitmap = np.ones(size, dtype=np.bool_)
        for p in actives:
            step2 = (2 * p) // 6
            step4 = (4 * p) // 6
            seed = (p * p - lo) // 6
            bitmap[seed % step2 :: step2] = False
            bitmap[seed % step4 :: step4] = False
        count += bitmap.sum()
    return count
