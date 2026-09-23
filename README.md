# Python Algorithm Lab

Readable implementations of core algorithms, with executable examples and
independent regression tests. Python 3.11+; no runtime dependencies.

These modules are learning implementations. Their docstrings state the
input assumptions, tie behavior, and complexity. Import only the module you need.

```python
from algorithm_lab.binary_search import binary_search

assert binary_search([1, 3, 3, 8], 3) == 1
```

## Run locally

```bash
python -m unittest discover -s tests -v
python -m doctest algorithm_lab/*.py
```

Optional installation: `python -m pip install -e .`. For linting and formatting,
install `.[dev]` and run `ruff check .` and `ruff format --check .`.

## Catalog (9 algorithms)

| Module | Topic | What it demonstrates |
| --- | --- | --- |
| [binary_search](algorithm_lab/binary_search.py) | Searching | First matching index in a sorted sequence |
| [quickselect](algorithm_lab/quickselect.py) | Selection | Zero-based order statistics with three-way partitioning |
| [merge_sort](algorithm_lab/merge_sort.py) | Sorting | Stable sorting with an optional key function |
| [counting_sort](algorithm_lab/counting_sort.py) | Sorting | Integer sorting with a bounded value range |
| [heap_sort](algorithm_lab/heap_sort.py) | Sorting | Comparison sorting with an explicit binary max heap |
| [radix_sort](algorithm_lab/radix_sort.py) | Sorting | Stable byte-wise sorting of signed arbitrary-size integers |
| [two_sum](algorithm_lab/two_sum.py) | Sequences | Find original indices of an integer pair with a target sum |
| [max_subarray](algorithm_lab/max_subarray.py) | Sequences | Kadane maximum sum with original slice boundaries |
| [prefix_sum](algorithm_lab/prefix_sum.py) | Sequences | Immutable preprocessing for constant-time range sums |

## Validation

Tests use standard-library oracles, exhaustive small cases, and seeded inputs.
Examples are checked with `doctest`. GitHub Actions runs tests on Python 3.11,
3.12, and 3.13. Each feature commit includes its implementation and tests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidance. Licensed under
the [MIT license](LICENSE).
