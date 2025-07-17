# Composite-Displacement Sieve (`greedy-ast`)

Reference implementation of the *Greedy–Ast* branch sieve from  
> “The 6k±1 Composite–Displacement Sieve: Formal Analysis and Efficient Implementation”.

## Quick start
```bash
pip install -r requirements.txt
python benchmarks.py 100000000  # reproduces Table-1 row for 1e8
---

## 3  Dataset („first 10¹⁰ primes in 6k±1“)

> **Realität-Check**:  
> *10 billion* primes ≈ primes ≤ 1.05 × 10¹¹ → **≈ 455 MiB** gzipped → GitHub-Limit überschritten.  
> Lösung 👉 split in 100 × 4.6 MiB-Chunks *oder* extern hosten (Zenodo, Figshare, G-Drive).  
> Für den ersten Review genügt meist ein kleinerer Schnappschuss (z. B. alle ≤ 10⁹).

### Script zum Erstellen

```python
# make_dataset.py
import csv, gzip
from greedy_ast import primes6_upto

def main(limit=10_000_000_000):   # 10^10
    last = 5
    with gzip.open("primes6.csv.gz", "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["prime", "gap"])
        for p in primes6_upto(limit):
            if p % 6 in (1,5):
                w.writerow([p, p - last])
                last = p

if __name__ == "__main__":
    main()
