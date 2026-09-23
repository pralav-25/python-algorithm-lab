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

## Catalog (42 algorithms)

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
| [sliding_window_max](algorithm_lab/sliding_window_max.py) | Sequences | Window maxima using a monotonic deque |
| [longest_increasing_subsequence](algorithm_lab/longest_increasing_subsequence.py) | Sequences | Reconstruct one strictly increasing subsequence |
| [merge_intervals](algorithm_lab/merge_intervals.py) | Intervals | Union of overlapping closed integer intervals |
| [interval_scheduling](algorithm_lab/interval_scheduling.py) | Intervals | Maximum-cardinality selection of compatible activities |
| [inversion_count](algorithm_lab/inversion_count.py) | Sequences | Count out-of-order pairs using merge-based accumulation |
| [kmp_search](algorithm_lab/kmp_search.py) | Strings | Find overlapping matches with a prefix-function automaton |
| [rabin_karp](algorithm_lab/rabin_karp.py) | Strings | Rolling-hash substring search with exact collision checks |
| [levenshtein](algorithm_lab/levenshtein.py) | Strings | Edit distance with linear working memory |
| [longest_common_subsequence](algorithm_lab/longest_common_subsequence.py) | Strings | Dynamic-programming reconstruction of a common subsequence |
| [longest_palindrome](algorithm_lab/longest_palindrome.py) | Strings | Expand around centers to find a palindromic substring |
| [trie](algorithm_lab/trie.py) | Data structures | Prefix dictionary with insertion, deletion, and completions |
| [run_length_encoding](algorithm_lab/run_length_encoding.py) | Strings | Lossless run encoding with bounded decoding |
| [balanced_brackets](algorithm_lab/balanced_brackets.py) | Strings | Stack-based matching for parentheses, brackets, and braces |
| [bfs_shortest_path](algorithm_lab/bfs_shortest_path.py) | Graphs | Shortest unweighted paths with predecessor reconstruction |
| [depth_first_search](algorithm_lab/depth_first_search.py) | Graphs | Iterative DFS preorder without recursion limits |
| [connected_components](algorithm_lab/connected_components.py) | Graphs | Undirected components including isolated and neighbor-only vertices |
| [topological_sort](algorithm_lab/topological_sort.py) | Graphs | Kahn ordering with explicit directed-cycle detection |
| [dijkstra](algorithm_lab/dijkstra.py) | Graphs | Nonnegative weighted shortest paths with arbitrary vertex labels |
| [bellman_ford](algorithm_lab/bellman_ford.py) | Graphs | Shortest paths with negative edges and reachable-cycle detection |
| [floyd_warshall](algorithm_lab/floyd_warshall.py) | Graphs | All-pairs shortest distances with negative-cycle detection |
| [minimum_spanning_tree](algorithm_lab/minimum_spanning_tree.py) | Graphs | Kruskal tree or forest with stable edge selection |
| [disjoint_set](algorithm_lab/disjoint_set.py) | Data structures | Union-find with path compression and component sizes |
| [strongly_connected_components](algorithm_lab/strongly_connected_components.py) | Graphs | Iterative Kosaraju decomposition of directed cycles |
| [bipartite_coloring](algorithm_lab/bipartite_coloring.py) | Graphs | Two-color undirected graphs or detect an odd cycle |
| [astar_grid](algorithm_lab/astar_grid.py) | Graphs | Optimal four-neighbor grid paths with a Manhattan heuristic |
| [coin_change](algorithm_lab/coin_change.py) | Dynamic programming | Minimum-coin change with an actual combination |
| [knapsack](algorithm_lab/knapsack.py) | Dynamic programming | 0/1 knapsack with selected original item indices |
| [subset_sum](algorithm_lab/subset_sum.py) | Dynamic programming | Bounded bitset reachability for nonnegative integer subsets |
| [matrix_chain](algorithm_lab/matrix_chain.py) | Dynamic programming | Optimal parenthesization of compatible matrix products |
| [longest_common_substring](algorithm_lab/longest_common_substring.py) | Strings | Longest contiguous common text with deterministic ties |
| [grid_paths](algorithm_lab/grid_paths.py) | Dynamic programming | Count exact right-and-down paths around obstacles |
| [extended_gcd](algorithm_lab/extended_gcd.py) | Number theory | Bezout coefficients for signed arbitrary-size integers |
| [modular_power](algorithm_lab/modular_power.py) | Number theory | Exponentiation by squaring under a positive modulus |

## Validation

Tests use standard-library oracles, exhaustive small cases, and seeded inputs.
Examples are checked with `doctest`. GitHub Actions runs tests on Python 3.11,
3.12, and 3.13. Each feature commit includes its implementation and tests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidance. Licensed under
the [MIT license](LICENSE).
