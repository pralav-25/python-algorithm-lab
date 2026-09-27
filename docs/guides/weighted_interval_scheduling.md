# Optimize appointment value instead of appointment count

[Guide index](../README.md) · [Implementation](../../algorithm_lab/weighted_interval_scheduling.py)

## Reasoning

For each interval in finish-time order, compare skipping it with taking its value plus the best compatible earlier solution. Binary search finds the last interval that can precede it. This dynamic program handles the case where one valuable long booking beats several short bookings.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.weighted_interval_scheduling import weighted_interval_scheduling
>>> bookings = [(0, 2, 3), (2, 4, 3), (0, 4, 10), (4, 5, 2)]
>>> value, chosen = weighted_interval_scheduling(bookings)
>>> value, chosen
(12, [2, 3])
>>> assert sum(bookings[i][2] for i in chosen) == value
>>> weighted_interval_scheduling([(0, 1, -5)])
(0, [])

```

## Boundary to remember

Earliest-finish greedy scheduling maximizes count, not value. Returned indices refer to the original input and are listed chronologically; negative-value bookings may all be skipped.
