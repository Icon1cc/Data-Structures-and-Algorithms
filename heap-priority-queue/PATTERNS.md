# Heap / Priority Queue Patterns

PATTERNS.md is the most important file in this topic. Use it before practice to learn recognition signals, invariants, and interview explanations.

## Pattern Selection Table

| Pattern | Strongest Signal | Avoid When |
|---|---|---|
| Top K Heap | top k | Do not heap all n items if k is small and only k results are needed |
| K-way Merge | k sorted | Do not push every item upfront if sources can be advanced lazily |
| Two Heaps | median | Do not let heap sizes drift beyond one |
| Lazy Deletion Heap | stale | Do not trust heap top until stale entries are pruned |
| Dijkstra Frontier | shortest path | Do not use when negative edges are present |

## Pattern: Top K Heap

### Beginner Intuition

Keep only the k best candidates seen so far.

### When To Use It

Use for kth largest, top frequencies, and closest points.

### When Not To Use It

Do not heap all n items if k is small and only k results are needed.

### Recognition Signals

- top k
- kth
- closest
- frequent

### Example Problems

- Kth Largest Element in an Array
- K Closest Points to Origin

### Common Mistakes

- Using a max-heap of size k for "k largest"; the correct structure is a min-heap, where the top is the worst kept item to evict.
- Comparing tuples in Python without a stable secondary key; equal first values force a node-comparison error in some payloads.
- Pushing all n items first, then popping k; this works but costs O(n log n) instead of O(n log k).

### Pseudocode Or Template

```text
heap = []
for item in items:
    push item
    if len(heap) > k: pop worst among kept
```

### Complexity Notes

O(n log k) time, O(k) space.

### Interview Explanation

The heap contains the best k candidates after each scan step.

## Pattern: K-way Merge

### Beginner Intuition

Use a heap containing the current head of each sorted source.

### When To Use It

Use for merging sorted lists, arrays, or streams.

### When Not To Use It

Do not push every item upfront if sources can be advanced lazily.

### Recognition Signals

- k sorted
- merge
- smallest head

### Example Problems

- Merge k Sorted Lists
- Find K Pairs with Smallest Sums

### Common Mistakes

- Pushing all n items into the heap upfront; the heap should hold at most one head per source at a time.
- Forgetting to push the next element from the source after popping; the merge stalls.
- Heaping `(value, node)` without a tiebreak index; equal values cause node comparisons that crash on linked-list nodes.

### Pseudocode Or Template

```text
push first item from each source
while heap:
    value, source = heappop(heap)
    push next from same source
```

### Complexity Notes

O(N log k) time, O(k) space.

### Interview Explanation

Only one candidate from each source is needed because each source is sorted.

## Pattern: Two Heaps

### Beginner Intuition

Maintain a max-heap for the lower half and min-heap for the upper half.

### When To Use It

Use for streaming median and balancing lower/upper partitions.

### When Not To Use It

Do not let heap sizes drift beyond one.

### Recognition Signals

- median
- lower half
- upper half
- stream

### Example Problems

- Find Median from Data Stream
- Sliding Window Median

### Common Mistakes

- Pushing directly to the side you want without normalizing through the other; always push to one heap, then transfer the top to the other before checking sizes.
- Allowing the lower heap to become smaller than the upper, which changes how the median is computed for odd lengths.
- For median over an even count, returning `lower.top()` instead of `(lower.top() + upper.top()) / 2`.

### Pseudocode Or Template

```text
lower = max_heap
upper = min_heap
rebalance so sizes differ by at most one
```

### Complexity Notes

O(log n) update, O(1) median.

### Interview Explanation

The partition invariant makes median retrieval immediate.

## Pattern: Lazy Deletion Heap

### Beginner Intuition

Mark stale items and discard them only when they reach the top.

### When To Use It

Use when arbitrary deletion from a heap would be expensive.

### When Not To Use It

Do not trust heap top until stale entries are pruned.

### Recognition Signals

- stale
- delayed deletion
- sliding median

### Example Problems

- Sliding Window Median
- Task Scheduler variants

### Common Mistakes

- Reading `heap.top()` without first cleaning stale entries; the answer reflects evicted items.
- Forgetting to decrement the `delayed` map after popping a stale entry, leaving phantom counts forever.
- Tracking staleness by index when the same value appears multiple times; key by `(value, expiry)` instead.

### Pseudocode Or Template

```text
delayed[value] += 1
while heap and delayed[top(heap)]:
    delayed[top(heap)] -= 1
    pop(heap)
```

### Complexity Notes

O(log n) amortized update, extra stale storage possible.

### Interview Explanation

Lazy deletion keeps heap operations cheap while preserving correctness at pop time.

## Pattern: Dijkstra Frontier

### Beginner Intuition

Use a min-heap to expand the next closest unsettled graph node.

### When To Use It

Use for non-negative weighted shortest paths.

### When Not To Use It

Do not use when negative edges are present.

### Recognition Signals

- shortest path
- non-negative
- frontier

### Example Problems

- Network Delay Time
- Path With Minimum Effort

### Common Mistakes

- Treating a popped distance as final without comparing to `best[node]`; stale entries must be skipped.
- Pushing on the relax step but never marking the node as settled; the heap fills with redundant entries (still correct but slow).
- Using Dijkstra with negative edges; the algorithm can lock in a non-optimal distance once a node is settled.

### Pseudocode Or Template

```text
push (0, source)
while heap:
    dist, node = heappop(heap)
    if dist != best[node]: continue
    relax neighbors
```

### Complexity Notes

O((V + E) log V) with adjacency list.

### Interview Explanation

The heap always gives the next cheapest candidate distance.

---

## Navigation

[Previous](CHEATSHEET.md) | [Home](../README.md) | [Next](easy.md)
