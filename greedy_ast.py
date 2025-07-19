#!/usr/bin/env python3
"""
greedy_ast.py – Reference implementation of the 6k±1 Composite-Displacement
sieve (“Greedy-Ast”).  Counts candidates that survive Selberg-equivalent
branch elimination up to a given limit x.

Usage
-----
$ python greedy_ast.py 100000000        # counts up to 1e8
"""

from math import isqrt
from typing import Generator, List
import sys

import numpy as np


# ---------------------------------------------------------------------------
#  Helper: primes generator restricted to 6k±1  (plus 2, 3 for completeness)
# ---------------------------------------------------------------------------
def primes6_upto(limit: int) -> Generator[int, None, None]:
    """Yield all primes ≤ limit in increasing order.

    Fast NumPy implementation of a wheel-2 Eratosthenes:
    only indices representing 6k±1 are actually stored.
    """
    if limit >= 2:
        yield 2
    if limit >= 3:
        yield 3

    size = limit // 3 + 1  # stores numbers 6k±1 up to 'limit'
    sieve = np.ones(size, dtype=np.bool_)

    # classic Pritchard linear wheel trick
    for i, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        p = 3 * i + 1 | 1        # maps index→number (gives 6k±1)
        if p * p > limit:
            break
        step = 2 * p
        sieve[(p * p) // 3 :: step] = False
        sieve[(p * (p - 2 * (i & 1) + 4)) // 3 :: step] = False

    # emit survivors
    idx = np.nonzero(sieve)[0]
    for i in idx:
        yield 3 * i + 1 | 1


# ---------------------------------------------------------------------------
#  Greedy-Ast main routine
# ---------------------------------------------------------------------------
def _bitmap_index(n: int, lo: int) -> int:
    """Return bitmap index for candidate number n (n ≡ 1 or 5 mod 6)."""
    return ((n - lo) // 6) * 2 + (0 if n % 6 == 1 else 1)


def greedy_ast_count(x: int, block: int = 5_000_000) -> int:
    """Count Selberg-remainder candidates ≤ x using the Greedy-Ast sieve."""
    if x < 5:
        return 0

    z = int(x ** (1 / 3))                       # sieve level
    actives: List[int] = [p for p in primes6_upto(z) if p > 3]

    count = 0
    # iterate over [lo, hi) blocks; each holds 'block' six-numbers
    for lo in range(5, x + 1, block * 6):
        hi = min(lo + block * 6, x + 1)

        # conservative size: two candidates per six-numbers window
        size = ((hi - lo + 5) // 6) * 2
        bitmap = np.ones(size, dtype=np.bool_)

        for p in actives:
            # -------- branch 1: n = p^2 + 2pk --------------------------------
            k_start = max(0, (lo - p * p + 2 * p - 1) // (2 * p))
            n = p * p + 2 * p * k_start
            while n < hi:
                if n % 6 in (1, 5):
                    bitmap[_bitmap_index(n, lo)] = False
                n += 2 * p

            # -------- branch 2: n = p^2 + 4pk --------------------------------
            k_start = max(0, (lo - p * p + 4 * p - 1) // (4 * p))
            n = p * p + 4 * p * k_start
            while n < hi:
                if n % 6 in (1, 5):
                    bitmap[_bitmap_index(n, lo)] = False
                n += 4 * p

        count += bitmap.sum()

    return int(count)


# ---------------------------------------------------------------------------
#  Command-line entry point
# ---------------------------------------------------------------------------
def _main(argv: List[str]) -> None:
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python greedy_ast.py <limit>", file=sys.stderr)
        sys.exit(1)

    limit = int(argv[1])
    from time import perf_counter

    t0 = perf_counter()
    c = greedy_ast_count(limit)
    dt = perf_counter() - t0
    print(f"x={limit:_}  c={c:_}  {dt:.2f}s")


if __name__ == "__main__":
    _main(sys.argv)
