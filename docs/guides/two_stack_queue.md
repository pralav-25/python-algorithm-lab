# Reverse incoming items only when the front stack empties

[Guide index](../README.md) · [Implementation](../../algorithm_lab/two_stack_queue.py)

## Reasoning

Enqueue appends to an incoming stack. When the outgoing stack is empty,
moving every incoming item to it reverses their order, placing the oldest at
the top. Items already waiting in outgoing must be served before another
transfer. Each item moves at most once, so operations are amortized O(1)
despite occasional O(n) transfers.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.two_stack_queue import TwoStackQueue
>>> queue = TwoStackQueue()
>>> queue.enqueue("first")
>>> queue.enqueue("second")
>>> queue.peek()
'first'
>>> queue.enqueue("third")
>>> queue.dequeue(), queue.dequeue(), queue.dequeue()
('first', 'second', 'third')
>>> len(queue)
0
>>> queue.enqueue(None)
>>> queue.dequeue() is None
True

```

## Boundary to remember

peek can trigger an internal transfer but never removes an item. Empty
peek and dequeue operations raise IndexError. The queue has no fixed capacity
and stores arbitrary objects; total space is O(n). A latency-sensitive caller
should remember that amortized constant time permits occasional linear work.
