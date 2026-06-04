# Heap / Priority Queue Cheatsheet

Fast revision for the last 10 minutes before practice or an interview.

## Core Definitions

A binary heap is a complete tree stored in an array that satisfies parent-child priority order. Push and pop are O(log n), peek is O(1).

## Complexity Table

| Operation or Pattern | Complexity |
|---|---:|
| Peek | O(1) |
| Push | O(log n) |
| Pop | O(log n) |
| Heapify n items | O(n) |
| Keep top k | O(n log k) |

## Space Table

| Case | Complexity |
|---|---:|
| Heap of k items | O(k) |
| Heap of all candidates | O(n) |
| Lazy deletion map | O(n) worst case |

## Pattern Summary

| Pattern | Use When |
|---|---|
| Top K Heap | Use for kth largest, top frequencies, and closest points. |
| K-way Merge | Use for merging sorted lists, arrays, or streams. |
| Two Heaps | Use for streaming median and balancing lower/upper partitions. |
| Lazy Deletion Heap | Use when arbitrary deletion from a heap would be expensive. |
| Dijkstra Frontier | Use for non-negative weighted shortest paths. |

## Recognition Hints

Look for top k, kth largest, smallest next item, streaming median, merge sorted lists, scheduling by priority, shortest path frontier, or repeated min or max selection.

## Templates

### Top K Heap

```text
heap = []
for item in items:
    push item
    if len(heap) > k: pop worst among kept
```

### K-way Merge

```text
push first item from each source
while heap:
    value, source = heappop(heap)
    push next from same source
```

### Two Heaps

```text
lower = max_heap
upper = min_heap
rebalance so sizes differ by at most one
```

### Lazy Deletion Heap

```text
delayed[value] += 1
while heap and delayed[top(heap)]:
    delayed[top(heap)] -= 1
    pop(heap)
```

## Common Traps

- Sorting every iteration instead of using a heap.
- Using max-heap logic in a min-heap language without negating keys carefully.
- Forgetting tie-breakers for stable ordering.
- Leaving stale entries without validating them on pop.

## Interview Reminders

- Say the brute force approach first in one or two sentences.
- State the invariant before coding.
- Test one normal case, one smallest case, and one adversarial case.
- Include auxiliary space, not only input and output size.
- Mention when the pattern assumptions would fail.

## Final Checklist

- [ ] I can define the topic in plain language.
- [ ] I can identify at least three recognition signals.
- [ ] I can write the main template from memory.
- [ ] I can explain time and space complexity.
- [ ] I can name two common mistakes and how to avoid them.

---

## Navigation

[Previous](README.md) | [Home](../README.md) | [Next](PATTERNS.md)
