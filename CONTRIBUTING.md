# Contributing

Each module demonstrates one algorithm with a small public API. Keep the runtime
standard-library only and compatible with Python 3.11 or later.

Document input assumptions, tie behavior, return values, complexity, and a runnable
example. Prefer explicit exceptions to silently converting malformed inputs.
Cover empty inputs, duplicates, boundaries, and independently computed results.
For randomized algorithms, inject a `random.Random` instance so tests are repeatable.

Run from the repository root:

```bash
python -m pip install -e '.[dev]'
python -m unittest discover -s tests -v
python -m doctest algorithm_lab/*.py
ruff check .
ruff format --check .
```

Small seeded cases can be compared with a brute-force oracle. Keep them bounded so
the full suite stays fast. Do not base correctness on a single timing measurement
or a probabilistic assertion. Add each new module to the README catalog.
