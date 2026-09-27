# Separate a majority from a mere plurality

[Guide index](../README.md) · [Implementation](../../algorithm_lab/majority_element.py)

## Reasoning

Cancel pairs of different values while maintaining one candidate. If a strict majority exists, cancellation cannot remove all of its excess occurrences. The surviving candidate still needs a second counting pass: cancellation alone also produces a candidate when no strict majority exists.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.majority_element import majority_element
>>> votes = ["yes", "no", "yes", "yes", "abstain"]
>>> majority_element(votes)
'yes'
>>> assert votes.count(majority_element(votes)) > len(votes) / 2
>>> majority_element([None, 1, None]) is None
True

```

## Boundary to remember

A majority occurs more than half the time, not merely more often than every competitor. None is valid data, so absence is signaled with ValueError rather than a sentinel value.
