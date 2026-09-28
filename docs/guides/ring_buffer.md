# Reuse bounded storage as a queue wraps around

[Guide index](../README.md) · [Implementation](../../algorithm_lab/ring_buffer.py)

## Reasoning

A fixed array stores the queue with a head position and current size.
The next append position is (head + size) modulo capacity. Removing an item
advances the head instead of shifting the remaining items, so both operations
take O(1) time. Storage remains O(capacity), including after many wraparounds.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.ring_buffer import RingBuffer
>>> buffer = RingBuffer(2)
>>> buffer.append(None)
>>> buffer.append("next")
>>> buffer.popleft() is None
True
>>> buffer.append("last")
>>> buffer.to_list()
['next', 'last']
>>> buffer.append("too much")
Traceback (most recent call last):
...
OverflowError: buffer is full
>>> buffer.to_list()
['next', 'last']

```

## Boundary to remember

Full buffers reject appends without discarding queued data. Empty reads
raise IndexError. None is an ordinary stored value; occupancy is tracked
separately. to_list returns a FIFO snapshot in O(n) time. For an unbounded
queue compare the [two-stack queue](two_stack_queue.md).
