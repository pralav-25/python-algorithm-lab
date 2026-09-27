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

## Searching

- [Locate the first repeated timestamp](guides/binary_search.md)

## Selection

- [Select a median without sorting everything](guides/quickselect.md)

## Sequences

- [Find the strongest contiguous run](guides/max_subarray.md)
- [Answer repeated totals over fixed data](guides/prefix_sum.md)
- [Track rolling peak measurements](guides/sliding_window_max.md)
- [Match a pair to a fixed budget](guides/two_sum.md)

## Sorting

- [Sort measurements in a compact integer range](guides/counting_sort.md)
- [Extract maxima into their final sorted positions](guides/heap_sort.md)
- [Sort priorities while preserving arrival order](guides/merge_sort.md)
- [Sort signed identifiers one byte at a time](guides/radix_sort.md)
