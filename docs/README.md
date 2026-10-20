# Algorithm study guides

Worked examples connect the implementations to their invariants, tradeoffs, and edge cases.
Code blocks are copyable Python snippets. Guides that use interactive doctest prompts are
exercised by the standard unittest command. Each guide links to its implementation for the
full API and complexity contract.

Start with binary search, prefix sums, and merge sort; then compare the string-search
and dynamic-programming techniques. Use the topic lists to choose a focused lesson.

```bash
python -m unittest discover -s tests -v
# Check just one guide:
python -m doctest docs/guides/binary_search.md
```

These guides were prepared with AI assistance. New snippets follow the module examples and
can be run from the repository root.

## Algebra

- [Track volume scaling through elimination](guides/determinant.md)
- [Solve linear equations and verify the substitution](guides/gaussian_elimination.md)
- [Evaluate the unique low-degree curve through exact points](guides/lagrange_interpolation.md)
- [Jump to a distant term of a fixed recurrence](guides/linear_recurrence.md)
- [Count repeated transitions with matrix powers](guides/matrix_power.md)
- [Divide a polynomial while retaining an exact remainder](guides/polynomial_divmod.md)
- [Evaluate coefficients with Horner’s rule](guides/polynomial_evaluate.md)
- [Multiply polynomials by combining degree pairs](guides/polynomial_multiply.md)

## Backtracking

- [Prune a board search with occupied lines](guides/n_queens.md)

## Combinatorics

- [Count teams without enumerating them](guides/binomial_coefficient.md)
- [Allocate a fixed total under individual caps](guides/bounded_compositions.md)
- [Count valid balanced structures without listing them](guides/catalan_number.md)
- [Locate a selection in lexicographic enumeration](guides/combination_rank.md)
- [Jump directly to a ranked selection](guides/combination_unrank.md)
- [Count assignments where nobody keeps their own item](guides/derangements.md)
- [Enumerate bit patterns with one-bit transitions](guides/gray_code.md)
- [Split a total into unordered positive pieces](guides/integer_partitions.md)
- [Relabel a shrinking elimination circle](guides/josephus.md)
- [Enumerate distinct arrangements of repeated values](guides/multiset_permutations.md)
- [Advance one step in lexicographic order](guides/next_permutation.md)
- [Generate all fixed-size subset counts for one set](guides/pascal_row.md)
- [Encode a permutation with skipped factorial blocks](guides/permutation_rank.md)
- [Decode a rank into one ordered arrangement](guides/permutation_unrank.md)
- [Divide distinct positions into unlabeled groups](guides/set_partitions.md)
- [Count partitions with a fixed number of groups](guides/stirling_second.md)
- [Recover exact mask values from subset totals](guides/subset_mobius_transform.md)
- [Aggregate a value over every subset of a mask](guides/subset_zeta_transform.md)
- [Count ordered outcomes of identical numbered dice with a given total](guides/dice_sum_count.md)
- [Count tilings of a 2-by-n rectangle with unlabelled 2-by-1 dominoes](guides/domino_tilings.md)
- [Count unordered integer partitions of n into positive parts](guides/partition_count.md)

## Compression

- [Give frequent symbols shorter prefix codes](guides/huffman_codes.md)

## Data structures

- [Merge connectivity groups without enumerating them](guides/disjoint_set.md)
- [Adjust measurements while keeping fast prefix totals](guides/fenwick_tree.md)
- [Evict the entry untouched for the longest time](guides/lru_cache.md)
- [Keep an exact median between two balanced heaps](guides/median_stream.md)
- [Store the minimum alongside each stack prefix](guides/min_stack.md)
- [Track sorted values with duplicate-aware ranks](guides/ordered_multiset.md)
- [Reuse bounded storage as a queue wraps around](guides/ring_buffer.md)
- [Undo connectivity merges at a saved boundary](guides/rollback_disjoint_set.md)
- [Replace individual values and query interval totals](guides/segment_tree.md)
- [Precompute overlapping blocks for constant-time minima](guides/sparse_table.md)
- [Share word prefixes while preserving whole-word membership](guides/trie.md)
- [Reverse incoming items only when the front stack empties](guides/two_stack_queue.md)

## Dynamic programming

- [Respect limited quantities while maximizing value](guides/bounded_knapsack.md)
- [Find a minimum-coin payment when greed fails](guides/coin_change.md)
- [Count payments without counting coin order](guides/coin_change_count.md)
- [Count right-and-down routes around obstacles](guides/grid_paths.md)
- [Choose a valuable subset under a capacity limit](guides/knapsack.md)
- [Choose multiplication parentheses before multiplying](guides/matrix_chain.md)
- [Locate the largest all-one square](guides/maximal_square.md)
- [Use the fewest palindromic pieces](guides/palindrome_partition.md)
- [Choose cuts that sell the entire rod](guides/rod_cutting.md)
- [Track reachable totals with a bitset](guides/subset_sum.md)
- [Choose a cheapest route down a triangle](guides/triangle_min_path.md)
- [Segment text using the fewest dictionary words](guides/word_break.md)
- [Choose nonadjacent houses on a circle to maximize their total value](guides/circular_house_robber.md)
- [Choose nonadjacent houses on a line to maximize their total value](guides/house_robber.md)
- [Count decodings of ASCII digits into the symbols numbered 1 through 26](guides/decode_ways.md)
- [Count false and true evaluations over all full parenthesizations](guides/boolean_parenthesization.md)
- [Decide whether a string interleaves two strings in their original order](guides/interleaving_strings.md)
- [Find the minimum top-left to bottom-right path cost with right/down steps](guides/minimum_cost_path_grid.md)
- [Maximize coins earned by bursting balloons in any order](guides/burst_balloons.md)
- [Maximize value with unlimited copies of each item within a capacity](guides/unbounded_knapsack.md)
- [Minimize the absolute difference between sums of two complementary subsets](guides/minimum_partition_difference.md)
- [Minimize weighted successful-search comparisons in an ordered BST](guides/optimal_bst.md)
- [Return minimum worst-case drops needed to identify an egg-breaking floor](guides/egg_drop.md)

## Geometry

- [Keep only the outermost points of a cloud](guides/convex_hull.md)
- [Classify points with a boundary-aware crossing test](guides/point_in_polygon.md)
- [Sum signed edge contributions to an exact area](guides/polygon_area.md)
- [Count overlapping rectangular coverage only once](guides/rectangle_union_area.md)
- [Distinguish crossings, contact, and collinear overlap](guides/segments_intersect.md)

## Graphs

- [Find single vertices that disconnect a network](guides/articulation_points.md)
- [Guide a grid search with Manhattan distance](guides/astar_grid.md)
- [Relax signed edges and detect reachable negative cycles](guides/bellman_ford.md)
- [Recover the fewest-edge route through a directed graph](guides/bfs_shortest_path.md)
- [Split a network into two conflict-free sides](guides/bipartite_coloring.md)
- [Reassign earlier choices to maximize compatible pairs](guides/bipartite_matching.md)
- [Locate edges with no alternate connection](guides/bridges.md)
- [Group vertices by undirected reachability](guides/connected_components.md)
- [Settle signed path costs in dependency order](guides/dag_shortest_paths.md)
- [Explore one branch before returning to alternatives](guides/depth_first_search.md)
- [Expand the cheapest unsettled route first](guides/dijkstra.md)
- [Traverse every directed edge exactly once](guides/eulerian_trail.md)
- [Return a concrete witness of cyclic dependencies](guides/find_directed_cycle.md)
- [Allow one more intermediate vertex at each stage](guides/floyd_warshall.md)
- [Collapse mutually reachable groups into a DAG](guides/graph_condensation.md)
- [Increase network throughput through residual routes](guides/max_flow.md)
- [Connect all vertices with minimum total edge weight](guides/minimum_spanning_tree.md)
- [Find the nearest starting point in one traversal](guides/multi_source_bfs.md)
- [Resolve ranked preferences without blocking pairs](guides/stable_matching.md)
- [Group vertices that can mutually reach one another](guides/strongly_connected_components.md)
- [Schedule every dependency before its dependents](guides/topological_sort.md)
- [Precompute which destinations every vertex can reach](guides/transitive_closure.md)
- [Choose a vertex that balances the remaining components](guides/tree_centroids.md)
- [Find a longest tree route with two breadth-first searches](guides/tree_diameter.md)
- [Maximize the weakest edge along a route](guides/widest_path.md)
- [Prioritize free edges with a double-ended queue](guides/zero_one_bfs.md)

## Intervals

- [Intersect two sorted coverage maps](guides/interval_intersection.md)
- [Find the busiest coordinate with endpoint events](guides/interval_overlap_peak.md)
- [Fit the greatest number of appointments](guides/interval_scheduling.md)
- [Combine closed coverage ranges](guides/merge_intervals.md)
- [Cover a target range using the fewest available spans](guides/minimum_interval_cover.md)

## Number theory

- [Combine repeating schedules with compatible offsets](guides/chinese_remainder.md)
- [Express an exact rational through Euclidean quotients](guides/continued_fraction.md)
- [Build rational approximations from successive prefixes](guides/continued_fraction_convergents.md)
- [Build divisor lists for a whole interval](guides/divisor_sieve.md)
- [Count the invertible residue classes](guides/euler_totient.md)
- [Generate reduced fractions in increasing order](guides/farey_sequence.md)
- [Recover a certificate for the greatest common divisor](guides/extended_gcd.md)
- [Advance a recurrence by doubling its index](guides/fast_fibonacci.md)
- [Certify an exact floor root of any positive degree](guides/integer_nth_root.md)
- [Bound a square root without floating-point rounding](guides/integer_sqrt.md)
- [Record square-free factor parity](guides/mobius_sieve.md)
- [Undo multiplication in modular arithmetic](guides/modular_inverse.md)
- [Exponentiate while keeping intermediate values bounded](guides/modular_power.md)
- [Find the cycle length of repeated modular multiplication](guides/multiplicative_order.md)
- [Decompose an integer into prime multiplicities](guides/prime_factorization.md)
- [Enumerate primes by crossing out composites](guides/prime_sieve.md)
- [Find primes inside a narrow interval](guides/segmented_sieve.md)
- [Locate a positive fraction by mediant comparisons](guides/stern_brocot_path.md)
- [Count trailing zero digits of n! represented in an arbitrary base](guides/trailing_factorial_zeros.md)
- [Decide whether n=a**b for integers a>=2 and b>=2](guides/is_perfect_power.md)
- [Enumerate primitive positive Pythagorean triples with bounded hypotenuse](guides/pythagorean_triples.md)
- [Evaluate the Jacobi symbol (value/modulus) by quadratic reciprocity](guides/jacobi_symbol.md)
- [Find the smallest primitive root of an integer modulus](guides/primitive_root.md)
- [Format an integer in base 2 through 36 without a prefix](guides/base_conversion.md)
- [Return the exponent of a prime in n! using Legendre's formula](guides/legendre_exponent.md)
- [Return the exponent of the multiplicative group modulo n](guides/carmichael_function.md)

## Optimization

- [Allocate capacity by value density](guides/fractional_knapsack.md)
- [Optimize appointment value instead of appointment count](guides/weighted_interval_scheduling.md)

## Sampling

- [Choose uniformly from a stream of unknown length](guides/reservoir_sample.md)

## Searching

- [Locate the first repeated timestamp](guides/binary_search.md)
- [Count repeated keys with two binary boundaries](guides/equal_range.md)
- [Search a sorted cycle without unrotating it](guides/rotated_search.md)
- [Find the first match in a sorted sequence by exponential bracketing](guides/exponential_search.md)
- [Find the first match in ascending sorted data with square-root jumps](guides/jump_search.md)
- [Find the first target occurrence by interpolating integer endpoints](guides/interpolation_search.md)
- [Select the zero-based kth value from the merge of two sorted sequences](guides/kth_two_sorted.md)

## Selection

- [Select a median without sorting everything](guides/quickselect.md)

## Sequences

- [Allow a best run to cross the sequence boundary](guides/circular_max_subarray.md)
- [Find a rectangle spanning several bars](guides/histogram_area.md)
- [Measure how far a ranking is from sorted](guides/inversion_count.md)
- [Explain each position’s contribution to ranking disorder](guides/inversion_vector.md)
- [Recover an increasing trend followed by a decline](guides/longest_bitonic_subsequence.md)
- [Recover an increasing progression with gaps](guides/longest_increasing_subsequence.md)
- [Find a longest target-sum slice with signed values](guides/longest_subarray_sum.md)
- [Separate a majority from a mere plurality](guides/majority_element.md)
- [Keep both extremes when signs can flip](guides/max_product_subarray.md)
- [Find the strongest contiguous run](guides/max_subarray.md)
- [Advance through layers of reachable positions](guides/minimum_jumps.md)
- [Find the first later improvement for every position](guides/next_greater.md)
- [Answer repeated totals over fixed data](guides/prefix_sum.md)
- [Exclude each factor without dividing by it](guides/product_except_self.md)
- [Track rolling peak measurements](guides/sliding_window_max.md)
- [Track rolling low measurements](guides/sliding_window_min.md)
- [Count every target-sum slice, including overlapping ones](guides/subarray_sum_count.md)
- [Compute the volume between retaining walls](guides/trapped_water.md)
- [Match a pair to a fixed budget](guides/two_sum.md)
- [Count nonempty contiguous subarrays whose XOR equals target](guides/subarray_xor_count.md)
- [Return (maximum_sum, start_index) among all windows of the requested size](guides/max_sum_fixed_window.md)
- [Return a new list rotated right by an integer number of steps](guides/rotate_sequence.md)
- [Return half-open indices of the longest subarray with equal zeros and ones](guides/longest_balanced_binary.md)
- [Return half-open indices of the shortest subarray with sum at least target](guides/min_length_subarray_sum.md)
- [Return the largest adjacent gap in the sorted order of signed integers](guides/maximum_gap.md)
- [Return the largest h with at least h citation counts greater than or equal to h](guides/h_index.md)
- [Return the length of the longest consecutive run in an integer iterable](guides/longest_consecutive.md)
- [Return the minimum absolute difference between two distinct input positions](guides/minimum_pair_difference.md)
- [Return the minimum number of arbitrary pair swaps to sort distinct integers](guides/minimum_swaps_sort.md)
- [Return the smallest positive integer absent from the supplied values](guides/smallest_missing_positive.md)
- [Return unique sorted 3-tuples summing to target, in lexicographic order](guides/three_sum.md)
- [Return unique sorted 4-tuples summing to target, in lexicographic order](guides/four_sum.md)

## Sorting

- [Sort measurements in a compact integer range](guides/counting_sort.md)
- [Extract maxima into their final sorted positions](guides/heap_sort.md)
- [Sort priorities while preserving arrival order](guides/merge_sort.md)
- [Separate equal keys during partition sorting](guides/quick_sort.md)
- [Sort signed identifiers one byte at a time](guides/radix_sort.md)
- [Insertion sort returning a new ascending list](guides/insertion_sort.md)
- [Merge two ascending iterables into a new list, retaining duplicates](guides/merge_sorted.md)
- [Return a three-way partition of integer values around pivot](guides/dutch_partition.md)

## Statistics

- [Measure uncertainty after normalizing category weights](guides/entropy.md)
- [Fit a monotone sequence by pooling violations](guides/isotonic_regression.md)
- [Compare distributions through their shared mixture](guides/jensen_shannon_divergence.md)
- [Compare rankings while accounting for ties](guides/kendall_tau.md)
- [Accumulate paired variation in one pass](guides/online_covariance.md)
- [State the interpolation convention behind a quantile](guides/percentile.md)
- [Normalize large scores without exponential overflow](guides/softmax.md)
- [Choose a center under unequal observation counts](guides/weighted_median.md)

## Streaming statistics

- [Track mean and variance without storing observations](guides/running_stats.md)

## Strings

- [Search many patterns in a single pass](guides/aho_corasick.md)
- [Group words by character multiplicity](guides/anagram_groups.md)
- [Check nested bracket structure with a stack](guides/balanced_brackets.md)
- [Count unique strings rather than index selections](guides/count_distinct_subsequences.md)
- [Return the operations behind an edit distance](guides/edit_script.md)
- [Find overlapping text matches without rescanning](guides/kmp_search.md)
- [Measure shared prefixes between neighboring suffixes](guides/lcp_array.md)
- [Count insertions, deletions, and substitutions](guides/levenshtein.md)
- [Keep shared content while allowing skipped characters](guides/longest_common_subsequence.md)
- [Find an uninterrupted shared text fragment](guides/longest_common_substring.md)
- [Expand around the center of a mirror](guides/longest_palindrome.md)
- [Keep a mirror while allowing deleted characters](guides/longest_palindromic_subsequence.md)
- [Maintain a window with no repeated characters](guides/longest_unique_substring.md)
- [Locate a longest balanced parentheses span](guides/longest_valid_parentheses.md)
- [Reuse mirrored palindrome radii](guides/manacher.md)
- [Cover a required multiset in the shortest span](guides/minimum_window.md)
- [Allow one adjacent-character transposition](guides/optimal_string_alignment.md)
- [Use rolling hashes without trusting collisions](guides/rabin_karp.md)
- [Compress runs without ambiguous digit parsing](guides/run_length_encoding.md)
- [Merge two ordered sequences with minimal repetition](guides/shortest_common_supersequence.md)
- [Index suffixes without storing every substring](guides/suffix_array.md)
- [Match an entire name with star and question mark](guides/wildcard_match.md)
- [Reuse a prefix-match window across a string](guides/z_function.md)
- [Compute unrestricted unit-cost Damerau-Levenshtein distance](guides/damerau_levenshtein.md)
- [Count index selections whose characters form a target subsequence](guides/target_subsequence_count.md)
- [Count nonempty palindromic substrings by their start and end positions](guides/palindrome_substring_count.md)
- [Count segmentations of text into dictionary words](guides/word_break_count.md)
- [Find a longest substring occurring at least twice, allowing overlaps](guides/longest_repeated_substring.md)
- [Find exact substring matches using Sunday's look-ahead shifts](guides/sunday_search.md)
- [Find exact substring matches with Boyer-Moore-Horspool shifts](guides/boyer_moore_horspool.md)
- [Match an entire string against literals, dot wildcards and star repetition](guides/regex_match.md)
- [Return the fewest inserted characters needed to make a palindrome](guides/minimum_insertions_palindrome.md)
- [Return the length of a subsequence repeated at distinct aligned indices](guides/longest_repeating_subsequence.md)
- [Return the optimal global alignment score with linear gap penalties](guides/needleman_wunsch.md)
- [Return the optimal local alignment score with linear gap penalties](guides/smith_waterman.md)
