# Heap / Priority Queue Patterns

This file is the main pattern-recognition reference for heap / priority queue. Each pattern explains why it works, when it fits, when to avoid it, and how to start coding it.

## Pattern: Top K

### Intuition

Keep only the best k candidates in a heap or bucket structure.

### When To Use It

Use for kth largest, top frequent, ranking, and nearest points.

### When Not To Use It

Do not use if the full sorted order is required.

### Recognition Signals

- top k
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Kth Largest Element in an Array
- Find Median from Data Stream

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
for item in items:
    push item
    if heap size > k: pop worst
```

## Pattern: K-way Merge

### Intuition

Use a heap of current heads from sorted sources and push the successor from the source you popped.

### When To Use It

Use for merging k lists, k sorted arrays, and smallest range problems.

### When Not To Use It

Do not use if sources are unsorted.

### Recognition Signals

- k-way merge
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Find Median from Data Stream
- Merge k Sorted Lists

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
push first item from each source
while heap: pop best and push next from same source
```

## Pattern: Two Heaps

### Intuition

Keep lower and upper halves balanced so the median or middle boundary is available.

### When To Use It

Use for running median and sliding median.

### When Not To Use It

Do not ignore lazy deletion when old values leave a sliding window.

### Recognition Signals

- two heaps
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Merge k Sorted Lists
- Kth Largest Element in an Array

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
low = max_heap; high = min_heap
rebalance sizes after every update
```

## Pattern: Scheduling by Priority

### Intuition

Use one priority for availability and another for which job should run next.

### When To Use It

Use for CPU tasks, meeting rooms, servers, and cooldown scheduling.

### When Not To Use It

Do not use a single heap when time and priority are separate concerns.

### Recognition Signals

- scheduling by priority
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Kth Largest Element in an Array
- Find Median from Data Stream

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
move available tasks into ready heap
if ready: run best
else: advance time
```

## Pattern: Greedy Heap

### Intuition

Use a heap to repeatedly choose the best available candidate as constraints evolve.

### When To Use It

Use for refueling, hiring, capital growth, and worker selection.

### When Not To Use It

Do not use if a sorted scan already provides a proof and simpler state.

### Recognition Signals

- greedy heap
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Find Median from Data Stream
- Merge k Sorted Lists

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
sort events
for event in events:
    add newly available candidates
    choose best from heap
```

## Pattern: Lazy Deletion

### Intuition

Mark entries as deleted and remove them only when they reach the heap top.

### When To Use It

Use when a heap needs arbitrary deletion but the language heap cannot delete by handle.

### When Not To Use It

Do not forget to prune before every peek or pop.

### Recognition Signals

- lazy deletion
- constraints match the invariant
- brute force repeats the same decision

### Problem Examples

- Merge k Sorted Lists
- Kth Largest Element in an Array

### Common Mistakes

- Starting to code before defining state.
- Updating the answer before the invariant is valid.
- Forgetting edge cases that break the pattern.

### Reusable Template Or Pseudocode

```text
while heap top is marked stale:
    decrement stale count
    pop heap
```
---

## Navigation

[Previous](../heap-priority-queue/CHEATSHEET.md) | [Home](../README.md) | [Next](../heap-priority-queue/easy.md)
