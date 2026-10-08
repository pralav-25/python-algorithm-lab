# Find the busiest coordinate with endpoint events

[Guide index](../README.md) · [Implementation](../../algorithm_lab/interval_overlap_peak.py)

## Reasoning

Starting an interval adds one active item and ending it removes one. Sweeping coordinates in order turns overlap counting into a running total of these events. Combining events at the same coordinate respects half-open boundaries and identifies the earliest coordinate achieving the maximum.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.interval_overlap_peak import interval_overlap_peak
>>> interval_overlap_peak([(0, 4), (2, 6), (4, 7)])
(2, 2)
>>> interval_overlap_peak([(0, 2), (2, 4)])
(1, 0)
>>> interval_overlap_peak([(5, 8), (5, 8)])
(2, 5)
>>> interval_overlap_peak([])
(0, None)

```

## Boundary to remember

An interval ending at a coordinate does not overlap one beginning there. This differs from closed-interval union and intersection, where shared endpoints count as contact.

## Practice exercise

Find the busiest integer time in a schedule where one booking ends exactly when two others begin. Verify the peak by counting active bookings at every candidate time.

```pycon
>>> from algorithm_lab.interval_overlap_peak import interval_overlap_peak
>>> bookings = [(-3, 1), (-1, 2), (1, 4), (1, 3)]
>>> peak = interval_overlap_peak(bookings)
>>> peak
(3, 1)
>>> occupancy = {time: sum(start <= time < stop for start, stop in bookings) for time in range(-3, 4)}
>>> maximum = max(occupancy.values())
>>> assert peak == (maximum, min(time for time, count in occupancy.items() if count == maximum))

```

At time 1 the first booking has ended, leaving three active bookings rather than four. The maximum can only change at an endpoint, and the brute-force integer counts independently check both the overlap count and its earliest location.
