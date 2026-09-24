# Python Algorithm Lab

[![Tests](https://github.com/pralav-25/python-algorithm-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/pralav-25/python-algorithm-lab/actions/workflows/ci.yml)

Readable implementations of core algorithms, with executable examples and
independent regression tests. Python 3.11+; no runtime dependencies.

These modules are learning implementations. Their docstrings state the
input assumptions, tie behavior, and complexity. Import only the module you need.

Comparison-based routines require mutually comparable values with a consistent
total order; NaN is unsupported. String algorithms operate on Unicode code points,
without normalization. Graph vertices must be hashable. Numeric routines document
their accepted domains and validation behavior. Weighted path routines
raise `ValueError` if a computed cost cannot be represented as a finite number.

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

## Catalog (92 algorithms)

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
| [prime_sieve](algorithm_lab/prime_sieve.py) | Number theory | Sieve of Eratosthenes through an inclusive bound |
| [prime_factorization](algorithm_lab/prime_factorization.py) | Number theory | Exact trial-division factorization with multiplicities |
| [integer_sqrt](algorithm_lab/integer_sqrt.py) | Number theory | Exact floor square roots using integer Newton iteration |
| [fast_fibonacci](algorithm_lab/fast_fibonacci.py) | Number theory | Exact Fibonacci numbers by iterative fast doubling |
| [binomial_coefficient](algorithm_lab/binomial_coefficient.py) | Combinatorics | Exact combinations without factorial intermediates |
| [chinese_remainder](algorithm_lab/chinese_remainder.py) | Number theory | Merge modular constraints, including compatible non-coprime moduli |
| [reservoir_sample](algorithm_lab/reservoir_sample.py) | Sampling | Uniform samples from a stream without knowing its length |
| [running_stats](algorithm_lab/running_stats.py) | Streaming statistics | Welford mean and variance with validated atomic updates |
| [fenwick_tree](algorithm_lab/fenwick_tree.py) | Data structures | Point updates and half-open range sums in logarithmic time |
| [segment_tree](algorithm_lab/segment_tree.py) | Data structures | Iterative sum tree with point replacement and range queries |
| [sparse_table](algorithm_lab/sparse_table.py) | Data structures | Static range minima with constant-time queries |
| [lru_cache](algorithm_lab/lru_cache.py) | Data structures | Bounded least-recently-used cache with explicit eviction |
| [min_stack](algorithm_lab/min_stack.py) | Data structures | Stack with constant-time minimum tracking |
| [median_stream](algorithm_lab/median_stream.py) | Data structures | Exact streaming medians using two balanced heaps |
| [ring_buffer](algorithm_lab/ring_buffer.py) | Data structures | Fixed-capacity FIFO with explicit overflow and wraparound |
| [two_stack_queue](algorithm_lab/two_stack_queue.py) | Data structures | Unbounded FIFO from two stacks with amortized constant cost |
| [ordered_multiset](algorithm_lab/ordered_multiset.py) | Data structures | Sorted multiset with rank, selection and duplicate-aware removal |
| [rollback_disjoint_set](algorithm_lab/rollback_disjoint_set.py) | Data structures | Union by size with snapshots and rollback |
| [equal_range](algorithm_lab/equal_range.py) | Searching | Locate both boundaries of duplicate keys in sorted data |
| [rotated_search](algorithm_lab/rotated_search.py) | Searching | Binary search in rotated ascending sequences with distinct keys |
| [next_permutation](algorithm_lab/next_permutation.py) | Combinatorics | Lexicographic successor without mutating the input |
| [majority_element](algorithm_lab/majority_element.py) | Sequences | Boyer-Moore candidate voting with majority verification |
| [longest_unique_substring](algorithm_lab/longest_unique_substring.py) | Strings | Sliding window for the earliest longest substring without repeats |
| [longest_subarray_sum](algorithm_lab/longest_subarray_sum.py) | Sequences | Longest target-sum slice using first-seen prefix sums |
| [product_except_self](algorithm_lab/product_except_self.py) | Sequences | Division-free products with prefix and suffix accumulation |
| [next_greater](algorithm_lab/next_greater.py) | Sequences | Nearest strictly greater neighbors using a monotonic stack |
| [histogram_area](algorithm_lab/histogram_area.py) | Sequences | Largest rectangle in a histogram using a monotonic stack |
| [trapped_water](algorithm_lab/trapped_water.py) | Sequences | Two-pointer computation of water retained between bars |
| [z_function](algorithm_lab/z_function.py) | Strings | Linear-time prefix-match lengths at every text offset |
| [manacher](algorithm_lab/manacher.py) | Strings | Linear-time longest palindrome with separate odd and even radii |
| [suffix_array](algorithm_lab/suffix_array.py) | Strings | Suffix ordering by prefix doubling without copied suffix strings |
| [lcp_array](algorithm_lab/lcp_array.py) | Strings | Kasai longest-common-prefix array for adjacent sorted suffixes |
| [optimal_string_alignment](algorithm_lab/optimal_string_alignment.py) | Strings | Restricted edit distance including adjacent transpositions |
| [palindrome_partition](algorithm_lab/palindrome_partition.py) | Dynamic programming | Reconstruct a minimum-cardinality palindromic partition |
| [wildcard_match](algorithm_lab/wildcard_match.py) | Strings | Full-string wildcard matching with rolling dynamic programming |
| [anagram_groups](algorithm_lab/anagram_groups.py) | Strings | Stable grouping of words by exact character multiplicities |
| [minimum_window](algorithm_lab/minimum_window.py) | Strings | Smallest covering substring with multiplicity-aware sliding window |
| [aho_corasick](algorithm_lab/aho_corasick.py) | Strings | Multi-pattern search with failure links and overlapping matches |
| [bridges](algorithm_lab/bridges.py) | Graphs | Iterative low-link detection of critical undirected edges |
| [articulation_points](algorithm_lab/articulation_points.py) | Graphs | Iterative detection of vertices that disconnect an undirected graph |
| [eulerian_trail](algorithm_lab/eulerian_trail.py) | Graphs | Hierholzer traversal consuming every directed edge exactly once |
| [dag_shortest_paths](algorithm_lab/dag_shortest_paths.py) | Graphs | Topological shortest distances with signed integer edge costs |
| [max_flow](algorithm_lab/max_flow.py) | Graphs | Edmonds-Karp maximum flow with a reachable-side minimum-cut certificate |
| [bipartite_matching](algorithm_lab/bipartite_matching.py) | Graphs | Maximum-cardinality matching by iterative augmenting paths |
| [transitive_closure](algorithm_lab/transitive_closure.py) | Graphs | Reachability sets by iterative traversal from each vertex |
| [tree_diameter](algorithm_lab/tree_diameter.py) | Graphs | Longest path in a validated unweighted tree using two BFS passes |
| [find_directed_cycle](algorithm_lab/find_directed_cycle.py) | Graphs | Iterative DFS returning an explicit directed-cycle witness |
| [graph_condensation](algorithm_lab/graph_condensation.py) | Graphs | Collapse strongly connected components into an acyclic graph |
| [integer_partitions](algorithm_lab/integer_partitions.py) | Combinatorics | Lazy generation of nonincreasing integer partitions |
| [set_partitions](algorithm_lab/set_partitions.py) | Combinatorics | Canonical lazy partitions of a finite indexed set |

## Validation

Tests use standard-library oracles, exhaustive small cases, and seeded inputs.
Examples are checked with `doctest`. GitHub Actions runs tests on Python 3.11,
3.12, and 3.13. Each feature commit includes its implementation and tests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidance. Licensed under
the [MIT license](LICENSE).
