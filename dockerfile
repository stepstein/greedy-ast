# ----- 1  Basis: schlankes Debian + Python 3.12 ---------------
FROM python:3.12-slim

# ----- 2  Systempakete (nur falls Numpy/Numba compiliert) ------
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential gcc gfortran \
    && rm -rf /var/lib/apt/lists/*

# ----- 3  Quellcode kopieren -----------------------------------
WORKDIR /app
COPY . /app

# ----- 4  Python-Abhängigkeiten --------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ----- 5  Default-Kommando (kann man beim Aufruf überschreiben)-
CMD ["python", "benchmarks.py", "100000000"]
