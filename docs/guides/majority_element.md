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

## Practice exercise

Distinguish a leading ballot option with exactly half the votes from a strict majority. Add one matching vote and verify the decision changes.

```pycon
>>> from collections import Counter
>>> from algorithm_lab.majority_element import majority_element
>>> ballots = ["approve", "reject", "approve", "defer", "reject", "approve"]
>>> counts = Counter(ballots)
>>> max(counts, key=counts.get), counts["approve"], len(ballots)
('approve', 3, 6)
>>> majority_element(ballots)
Traceback (most recent call last):
...
ValueError: no strict majority
>>> ballots.append("approve")
>>> majority_element(ballots)
'approve'
>>> assert 2 * ballots.count("approve") > len(ballots)

```

Three of six votes are exactly half, even though approve leads every other option. Candidate cancellation may still end with approve, so verification must reject it. The added ballot makes four of seven votes, crossing the strict threshold.
