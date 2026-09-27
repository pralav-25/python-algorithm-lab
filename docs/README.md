# Algorithm study guides

Worked examples connect the implementations to their invariants, tradeoffs, and edge cases.
The examples are executable: the standard unittest command checks every guide with doctest.
Each guide links to its implementation for the full API and complexity contract.

Start with binary search, prefix sums, and merge sort; then compare the string-search
and dynamic-programming techniques. Use the topic lists to choose a focused lesson.

```bash
python -m unittest discover -s tests -v
# Check just one guide:
python -m doctest docs/guides/binary_search.md
```

These guides were prepared with AI assistance and verified against executable examples.

## Combinatorics

- [Count teams without enumerating them](guides/binomial_coefficient.md)
- [Count valid balanced structures without listing them](guides/catalan_number.md)
- [Count assignments where nobody keeps their own item](guides/derangements.md)
- [Split a total into unordered positive pieces](guides/integer_partitions.md)
- [Advance one step in lexicographic order](guides/next_permutation.md)
- [Generate all fixed-size subset counts for one set](guides/pascal_row.md)
- [Divide distinct positions into unlabeled groups](guides/set_partitions.md)

## Dynamic programming

- [Find a minimum-coin payment when greed fails](guides/coin_change.md)
- [Count right-and-down routes around obstacles](guides/grid_paths.md)
- [Choose a valuable subset under a capacity limit](guides/knapsack.md)
- [Choose multiplication parentheses before multiplying](guides/matrix_chain.md)
- [Use the fewest palindromic pieces](guides/palindrome_partition.md)
- [Track reachable totals with a bitset](guides/subset_sum.md)

## Intervals

- [Fit the greatest number of appointments](guides/interval_scheduling.md)
- [Combine closed coverage ranges](guides/merge_intervals.md)

## Number theory

- [Combine repeating schedules with compatible offsets](guides/chinese_remainder.md)
- [Recover a certificate for the greatest common divisor](guides/extended_gcd.md)
- [Advance a recurrence by doubling its index](guides/fast_fibonacci.md)
- [Bound a square root without floating-point rounding](guides/integer_sqrt.md)
- [Exponentiate while keeping intermediate values bounded](guides/modular_power.md)
- [Decompose an integer into prime multiplicities](guides/prime_factorization.md)
- [Enumerate primes by crossing out composites](guides/prime_sieve.md)

## Searching

- [Locate the first repeated timestamp](guides/binary_search.md)
- [Count repeated keys with two binary boundaries](guides/equal_range.md)
- [Search a sorted cycle without unrotating it](guides/rotated_search.md)

## Selection

- [Select a median without sorting everything](guides/quickselect.md)

## Sequences

- [Find a rectangle spanning several bars](guides/histogram_area.md)
- [Measure how far a ranking is from sorted](guides/inversion_count.md)
- [Recover an increasing progression with gaps](guides/longest_increasing_subsequence.md)
- [Find a longest target-sum slice with signed values](guides/longest_subarray_sum.md)
- [Separate a majority from a mere plurality](guides/majority_element.md)
- [Find the strongest contiguous run](guides/max_subarray.md)
- [Find the first later improvement for every position](guides/next_greater.md)
- [Answer repeated totals over fixed data](guides/prefix_sum.md)
- [Exclude each factor without dividing by it](guides/product_except_self.md)
- [Track rolling peak measurements](guides/sliding_window_max.md)
- [Compute the volume between retaining walls](guides/trapped_water.md)
- [Match a pair to a fixed budget](guides/two_sum.md)

## Sorting

- [Sort measurements in a compact integer range](guides/counting_sort.md)
- [Extract maxima into their final sorted positions](guides/heap_sort.md)
- [Sort priorities while preserving arrival order](guides/merge_sort.md)
- [Sort signed identifiers one byte at a time](guides/radix_sort.md)

## Strings

- [Search many patterns in a single pass](guides/aho_corasick.md)
- [Group words by character multiplicity](guides/anagram_groups.md)
- [Check nested bracket structure with a stack](guides/balanced_brackets.md)
- [Find overlapping text matches without rescanning](guides/kmp_search.md)
- [Measure shared prefixes between neighboring suffixes](guides/lcp_array.md)
- [Count insertions, deletions, and substitutions](guides/levenshtein.md)
- [Keep shared content while allowing skipped characters](guides/longest_common_subsequence.md)
- [Find an uninterrupted shared text fragment](guides/longest_common_substring.md)
- [Expand around the center of a mirror](guides/longest_palindrome.md)
- [Maintain a window with no repeated characters](guides/longest_unique_substring.md)
- [Reuse mirrored palindrome radii](guides/manacher.md)
- [Cover a required multiset in the shortest span](guides/minimum_window.md)
- [Allow one adjacent-character transposition](guides/optimal_string_alignment.md)
- [Use rolling hashes without trusting collisions](guides/rabin_karp.md)
- [Compress runs without ambiguous digit parsing](guides/run_length_encoding.md)
- [Index suffixes without storing every substring](guides/suffix_array.md)
- [Match an entire name with star and question mark](guides/wildcard_match.md)
- [Reuse a prefix-match window across a string](guides/z_function.md)
